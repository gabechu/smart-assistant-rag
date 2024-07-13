import tiktoken


class TextSplitter:
    def __init__(self, chunk_size: int = 100) -> None:
        self._chunk_size = chunk_size
        self._tokenizer = tiktoken.get_encoding("o200k_base")

    def split_text(self, text: str) -> list[str]:
        tokens = self._tokenizer.encode(text)
        chunks = []
        for i in range(0, len(tokens), self._chunk_size):
            chunk_tokens = tokens[i : i + self._chunk_size]
            chunk_text = self._tokenizer.decode(chunk_tokens)
            chunks.append(chunk_text)
        return chunks
