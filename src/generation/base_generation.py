from abc import ABC, abstractmethod


class BaseGeneration(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str: ...
