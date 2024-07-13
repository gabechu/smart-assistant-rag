from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt


class BaseVectorModel(ABC):
    @abstractmethod
    def encode(self, texts: list[str]) -> npt.NDArray[np.float32]: ...
