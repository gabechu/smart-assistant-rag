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
        self._retrieval = retrieval
        self._generation = generation
        self._split_chunk_size = split_chunk_size

    @classmethod
    def load_data_in_chunks(self, split_chunk_size: int) -> list[str]:
        text_splitter = TextSplitter(chunk_size=split_chunk_size)
        data_loader = PdfDataLoader()

        chunks = []
        for path in self._pdf_urls:
            pdf_documents = data_loader.load_data(path)
            doc_chunks = text_splitter.split_text(pdf_documents)
            chunks.extend(doc_chunks)
        return chunks

    def _load_documents_for_retrieval(self) -> list[str]:
        # TODO: track which document the split chunk is from
        if not self._retrieval.has_documents():
            chunks = self.load_data_in_chunks(self._split_chunk_size)
            self._retrieval.documents = chunks
        return self._retrieval.documents

    def generate_response(self, query: str) -> str:
        self._load_documents_for_retrieval()
        top_chunks = self._retrieval.search(query)

        context = "\n\n".join([f"Document {i + 1}: {doc}" for i, doc in enumerate(top_chunks)])
        prompt = (
            f"User query: {query}\n\n"
            f"Context from retrieved documents:\n{context}\n\n"
            f"Please generate a response based on the above query and context."
        )

        generated_text = self._generation.generate(prompt=prompt)

        return generated_text
