from chunker_strategy import (
    FixedSizeChunker,
    SentenceChunker,
    RecursiveChunker,
)


def test_fixed_size_chunker():
    chunker = FixedSizeChunker(5)

    result = chunker.chunk("HelloWorld")

    assert result == ["Hello", "World"]


def test_sentence_chunker():
    chunker = SentenceChunker()

    result = chunker.chunk(
        "Hello world. Python is awesome."
    )

    assert result == [
        "Hello world",
        "Python is awesome",
    ]


def test_recursive_chunker():
    chunker = RecursiveChunker()

    text = (
        "one two three four five "
        "six seven eight nine ten"
    )

    result = chunker.chunk(text)

    assert len(result) == 2