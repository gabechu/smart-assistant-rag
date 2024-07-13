import numpy as np
import numpy.typing as npt
import torch
from transformers import AutoModel, AutoTokenizer

from src.vector_models.base_vector_model import BaseVectorModel


class HuggingFaceVectorModel(BaseVectorModel):
    def __init__(self, model_name: str) -> None:
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._model = AutoModel.from_pretrained(model_name)

    def encode(self, texts: list[str]) -> npt.NDArray[np.float32]:
        inputs = self._tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = self._model(**inputs)
        # apply mean pooling: avg the hidden states of all tokens
        embeddings = model_output.last_hidden_state.mean(dim=1)
        np_embeddings: npt.NDArray[np.float32] = embeddings.numpy()
        return np_embeddings
