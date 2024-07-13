import re
from io import BytesIO
from urllib.parse import urlparse

import requests
from pypdf import PdfReader


class PdfDataLoader:
    def _is_url(self, path: str) -> bool:
        parsed_url = urlparse(path)
        return parsed_url.scheme in ("http", "https")

    def _download_pdf(self, url: str) -> BytesIO:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        return BytesIO(response.content)

    def _preprocess_text(self, text: str) -> str:
        # Remove non-text elements (e.g., headers, footers)
        text = re.sub(r"\n+", "\n", text)  # Normalize newlines
        text = re.sub(r"\s+", " ", text)  # Normalize whitespace
        text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
        text = text.lower()  # Convert to lowercase
        return text

    def _extract_text_from_pdf(self, path: str) -> str:
        if self._is_url(path):
            pdf_stream = self._download_pdf(path)
        else:
            with open(path, "rb") as file:
                pdf_stream = BytesIO(file.read())

        reader = PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def load_data(self, path: str) -> str:
        raw_text = self._extract_text_from_pdf(path)
        return self._preprocess_text(raw_text)
