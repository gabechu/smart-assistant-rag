import os

import numpy as np
from openai import OpenAI
import numpy.typing as npt
from src.vector_models.base_vector_model import BaseVectorModel


class OpenaiVectorModel(BaseVectorModel):
    def __init__(self, model_name: str, batch_size: int = 48) -> None:
        self._client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self._model_name = model_name
        self._batch_size = batch_size

    def _get_embedding(self, texts: list[str]) -> npt.NDArray[np.float32]:
        texts = [text.replace("\n", " ") for text in texts]
        response = self._client.embeddings.create(input=texts, model=self._model_name)
        return np.array([data.embedding for data in response.data])

    def encode(self, texts: list[str]) -> npt.NDArray[np.float32]:
        all_embeddings = []
        for i in range(0, len(texts), self._batch_size):
            batch_texts = texts[i : i + self._batch_size]
            batch_embeddings = self._get_embedding(batch_texts)
            all_embeddings.append(batch_embeddings)
        return np.vstack(all_embeddings)
