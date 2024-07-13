from src.data.pdf_data_loader import PdfDataLoader
from src.generation.base_generation import BaseGeneration
from src.preprocessing.text_splitter import TextSplitter
from src.retrieval.base_search import BaseSearch


class RagPipeline:
    _pdf_urls = [
        "https://www.nrma.com.au/sites/nrma/files/nrma/policy_booklets/nrma-car-pds-1023-east.pdf",
        "https://www.allianz.com.au/openCurrentPolicyDocument/POL011BA/$File/POL011BA.pdf",
    ]

    def __init__(self, retrieval: BaseSearch, generation: BaseGeneration, split_chunk_size: int = 100) -> None:
        self._data_loader = PdfDataLoader()
        self._retrieval = retrieval
        self._generation = generation
        self._text_splitter = TextSplitter(chunk_size=split_chunk_size)

    def _load_data(self) -> list[str]:
        # TODO: track which document the split chunk is from
        if not self._retrieval.has_documents():
            chunks = []
            for path in self._pdf_urls:
                pdf_documents = self._data_loader.load_data(path)
                doc_chunks = self._text_splitter.split_text(pdf_documents)
                chunks.extend(doc_chunks)
            self._retrieval.documents = chunks
        return self._retrieval.documents

    def generate_response(self, query: str) -> None:
        self._load_data()
        top_chunks = self._retrieval.search(query)
        context = " ".join(top_chunks)
        self._generation.generate(prompt=query + " " + context)
