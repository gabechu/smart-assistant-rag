import json
from pathlib import Path
from functools import cached_property
from abc import ABC, abstractmethod


class BaseEvaluationDataLoader(ABC):
    @property
    @abstractmethod
    def evaluation_file_path(self) -> Path: ...

    @cached_property
    @abstractmethod
    def evaluation_data(self) -> list: ...


class RagEvaluationDataLoader(BaseEvaluationDataLoader):
    @property
    def evaluation_file_path(self) -> Path:
        base_path = Path(__file__).parent.parent.parent
        return base_path / "tests" / "rag_evaluation_data.json"

    @cached_property
    def evaluation_data(self) -> list[dict]:
        with open(self.evaluation_file_path) as f:
            data = json.loads(f.read())
        return data["queries"]
