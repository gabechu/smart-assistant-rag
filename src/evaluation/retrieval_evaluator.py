from src.data.evaluation_data_loader import RetrievalEvaluationDataLoader
from src.retrieval.base_search import BaseSearch


class RetrievalEvaluator:
    def __init__(self, retrieval_search: BaseSearch) -> None:
        self._retrieval_search = retrieval_search
        self._eval_data_loader = RetrievalEvaluationDataLoader()

    def _mean_reciprocal_rank(self, retrieved_docs: list[str], relevant_docs: list[str]) -> float:
        for i, doc in enumerate(retrieved_docs):
            if doc in relevant_docs:
                return 1 / (i + 1)
        return 0.0

    def _precision_at_k(self, retrieved_docs: list[str], relevant_docs: list[str], k: int) -> float:
        retrieved_at_k = retrieved_docs[:k]
        relevant_at_k = [doc for doc in retrieved_at_k if doc in relevant_docs]
        return len(relevant_at_k) / k

    def _recall_at_k(self, retrieved_docs: list[str], relevant_docs: list[str], k: int) -> float:
        retrieved_at_k = retrieved_docs[:k]
        relevant_at_k = [doc for doc in retrieved_at_k if doc in relevant_docs]
        return len(relevant_at_k) / len(relevant_docs)

    def evaluate(self, k: int) -> list[dict[str, float]]:
        eval_data = self._eval_data_loader.evaluation_data

        results = []
        for instance in eval_data:
            retrieved_docs = self._retrieval_search.search(instance["query"])
            relevant_docs = instance["relevant_docs"]
            results.append(
                {
                    "Precision@k": self._precision_at_k(retrieved_docs, relevant_docs, k),
                    "Recall@k": self._recall_at_k(retrieved_docs, relevant_docs, k),
                    "MRR": self._mean_reciprocal_rank(retrieved_docs, relevant_docs),
                }
            )
        return results
