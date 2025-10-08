from dataclasses import dataclass

import tiktoken


@dataclass
class Tokenizer:
    """
    A simple tokenizer class that splits text into tokens based on whitespace.
    """
    encoding: str

    def tokenize(self, text: str) -> list[int]:
        """
        Tokenizes the input text into a list of tokens.
        """
        encoder = tiktoken.get_encoding(encoding_name=self.encoding)
        return encoder.encode(text)

    def count_tokens(self, text: str) -> int:
        return len(self.tokenize(text))