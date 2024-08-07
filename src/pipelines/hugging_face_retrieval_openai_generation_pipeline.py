from src.generation.openai_generation import OpenaiGeneration
from src.pipelines.rag_pipeline import RagPipeline
from src.retrieval.vector_search import VectorSearch
from src.vector_models.hugging_face_vector_model import HuggingFaceVectorModel


class HuggingFaceRetrievalOpenaiGenerationPipeline(RagPipeline):
    def __init__(self) -> None:
        vector_model = HuggingFaceVectorModel(model_name="sentence-transformers/all-MiniLM-L6-v2")
        retrieval = VectorSearch(vector_model=vector_model, top_k=20)
        generation = OpenaiGeneration(model_name="gpt-4o")

        super().__init__(retrieval=retrieval, generation=generation)
