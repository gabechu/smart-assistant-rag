from abc import ABC, abstractmethod

import numpy as np


class BaseVectorModel(ABC):
    @abstractmethod
    def encode(self, texts: list[str]) -> np.ndarray:
        pass
