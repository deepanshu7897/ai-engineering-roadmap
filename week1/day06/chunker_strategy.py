from abc import ABC, abstractmethod


class Chunker(ABC):
    @abstractmethod
    def chunk(self, text: str):
        pass


class FixedSizeChunker(Chunker):
    def __init__(self, size: int = 20):
        self.size = size

    def chunk(self, text: str):
        return [
            text[i:i + self.size]
            for i in range(0, len(text), self.size)
        ]


class SentenceChunker(Chunker):
    def chunk(self, text: str):
        return [
            sentence.strip()
            for sentence in text.split(".")
            if sentence.strip()
        ]


class RecursiveChunker(Chunker):
    def chunk(self, text: str):
        words = text.split()
        chunks = []

        for i in range(0, len(words), 5):
            chunks.append(" ".join(words[i:i + 5]))

        return chunks


class TextProcessor:
    def __init__(self, chunker: Chunker):
        self.chunker = chunker

    def process(self, text: str):
        return self.chunker.chunk(text)


if __name__ == "__main__":
    text = (
        "Python is great for AI. "
        "Design patterns improve maintainability. "
        "Strategy pattern allows flexibility."
    )

    strategies = [
        FixedSizeChunker(25),
        SentenceChunker(),
        RecursiveChunker(),
    ]

    for strategy in strategies:
        processor = TextProcessor(strategy)

        print(f"\nUsing {strategy.__class__.__name__}")
        for chunk in processor.process(text):
            print(chunk)