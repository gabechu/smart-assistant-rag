from abc import ABC, abstractmethod


class BaseSearch(ABC):
    def __init__(self, top_k: int) -> None:
        self._top_k = top_k
        self._documents: list[str] | None = None

    @property
    def documents(self) -> list[str]:
        if self._documents is None:
            raise ValueError("Documents have not been set.")
        return self._documents

    @documents.setter
    def documents(self, new_documents: list[str]) -> None:
        self._documents = new_documents

    def has_documents(self) -> bool:
        return self._documents is not None

    @abstractmethod
    def search(self, query: str) -> list[str]: ...
