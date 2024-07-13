import numpy as np

from src.retrieval.base_search import BaseSearch
from src.utils import batch_cosine_similarity
from src.vector_models.base_vector_model import BaseVectorModel


class VectorSearch(BaseSearch):
    def __init__(self, vector_model: BaseVectorModel) -> None:
        self.vector_model = vector_model
        super().__init__()

    def _compute_document_embeddings(self, documents: list[str]) -> np.ndarray:
        return self.vector_model.encode(documents)

    def search(self, query: str, top_k: int = 5) -> list[str]:
        if self.documents is None:
            raise ValueError("Documents are not set. Please load the documents before searching.")

        query_embedding = self.vector_model.encode([query])
        document_embeddings = self._compute_document_embeddings(self.documents)

        similarities = batch_cosine_similarity(query_embedding[0], document_embeddings)
        ranked_indices = np.argsort(similarities)[::-1][:top_k]

        return [self.documents[i] for i in ranked_indices]
