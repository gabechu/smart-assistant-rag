import numpy as np

from src.retrieval.base_search import BaseSearch
from src.utils import batch_cosine_similarity
from src.vector_models.base_vector_model import BaseVectorModel


class VectorSearch(BaseSearch):
    def __init__(self, vector_model: BaseVectorModel, top_k: int = 20) -> None:
        self._vector_model = vector_model
        super().__init__(top_k=top_k)

    def search(self, query: str) -> list[str]:
        if self.documents is None:
            raise ValueError("Documents are not set. Please load the documents before searching.")

        query_embedding = self._vector_model.encode([query])  # dim (1, size)
        document_embeddings = self._vector_model.encode(self.documents[:100])  # (num_docs, size)
        similarities = batch_cosine_similarity(query_embedding[0], document_embeddings)
        ranked_indices = np.argsort(similarities)[::-1][: self._top_k]

        return [self.documents[i] for i in ranked_indices]
