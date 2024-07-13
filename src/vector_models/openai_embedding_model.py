import os

import numpy as np
import openai

from src.vector_models.base_vector_model import BaseVectorModel


class OpenaiEmbeddingModel(BaseVectorModel):
    def __init__(self, model_name: str) -> None:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        self._model_name = model_name

    def encode(self, texts: list[str]) -> np.ndarray:
        response = openai.embeddings.create(input=texts, model=self._model_name)
        embeddings = [np.array(embedding) for embedding in response.data]
        return np.array(embeddings)
