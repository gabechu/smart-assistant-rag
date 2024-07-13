from src.generation.openai_generation import OpenaiGeneration
from src.pipelines.rag_pipeline import RagPipeline
from src.retrieval.vector_search import VectorSearch
from src.vector_models.openai_vector_model import OpenaiVectorModel


class OpenaiRetrievalOpenaiGenerationPipeline:
    def __init__(self) -> None:
        vector_model = OpenaiVectorModel(model_name="text-embedding-3-small")
        retrieval = VectorSearch(vector_model=vector_model, top_k=20)
        generation = OpenaiGeneration(model_name="gpt-4o")

        self._rag_pipeline = RagPipeline(retrieval=retrieval, generation=generation)

    def generate_response(self, query: str) -> None:
        self._rag_pipeline.generate_response(query=query)
