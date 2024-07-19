import time
from functools import cached_property

import evaluate
from evaluate import EvaluationModule

from src.data.evaluation_data_loader import RagEvaluationDataLoader
from src.pipelines.rag_pipeline import RagPipeline


class RagEvaluator:
    def __init__(self, rag_pipeline: RagPipeline) -> None:
        self._rag_pipeline = rag_pipeline
        self._eval_data_loader = RagEvaluationDataLoader()

    @cached_property
    def _bleu(self) -> EvaluationModule:
        return evaluate.load("bleu")

    def relevance_score(self, reference: str, generated: str) -> float:
        result = self._bleu.compute(predictions=[generated], references=[reference])
        return result["bleu"]

    def diversity_score(self, generated: str) -> float:
        # Example using distinct-n metric for diversity
        n = 2
        ngrams: set = set()

        tokens = generated.split()
        ngrams.update(zip(*[tokens[i:] for i in range(n)]))
        return len(ngrams) / len(tokens) if tokens else 0

    def speed_score(self, start_time: float, end_time: float) -> float:
        return end_time - start_time

    def evaluate_responses(self):
        eval_data = self._eval_data_loader.evaluation_data

        for instance in eval_data:
            start_time = time.time()
            generated = self._rag_pipeline.generate_response(instance["query"])
            reference = instance["reference"]
            end_time = time.time()

            relevance = self.relevance_score(reference, generated)
            diversity = self.diversity_score(generated)
            speed = self.speed_score(start_time, end_time)

            print(f"Query: {instance['query']}")
            print(f"Reference: {reference}")
            print(f"Generated: {generated}")
            print(f"Relevance Score (BLEU): {relevance:.4f}")
            print(f"Diversity Score: {diversity:.4f}")
            print(f"Speed Score (Time): {speed:.4f} seconds")
