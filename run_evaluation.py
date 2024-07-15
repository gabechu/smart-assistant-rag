from src.evaluation.retrieval_evaluator import RetrievalEvaluator
from src.pipelines.rag_pipeline import RagPipeline
from src.retrieval.vector_search import VectorSearch
from src.vector_models.hugging_face_vector_model import HuggingFaceVectorModel


vector_model = HuggingFaceVectorModel(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_search = VectorSearch(vector_model, top_k=20)
vector_search.documents = RagPipeline.load_data_in_chunks(100)

evaluator = RetrievalEvaluator(vector_search)
results = evaluator.evaluate(2)
print(results)
