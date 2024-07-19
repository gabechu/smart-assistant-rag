import os

from openai import OpenAI

from src.generation.base_generation import BaseGeneration


class OpenaiGeneration(BaseGeneration):
    def __init__(self, model_name: str) -> None:
        self._client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self._model_name = model_name

    def generate(self, prompt: str) -> str:
        stream = self._client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}], model=self._model_name, stream=True
        )

        response = []
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                response.append(content)
        return "".join(response)
