import json
from functools import cached_property
from pathlib import Path


from src.retrieval.base_search import BaseSearch


class RetrievalEvaluator:
    def __init__(self, retrieval_search: BaseSearch) -> None:
        self._retrieval_search = retrieval_search

    @property
    def evaluation_file_path(self) -> Path:
        base_path = Path(__file__).parent.parent.parent
        return base_path / "tests" / "fake_data.json"

    @cached_property
    def _evaluation_instances(self) -> list[dict]:
        with open(self.evaluation_file_path) as f:
            data = json.loads(f.read())
        return data["queries"]

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
        results = []
        for instance in self._evaluation_instances:
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
