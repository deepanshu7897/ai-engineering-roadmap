import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        text = text.replace("\x00", "")
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"-\s+", "", text)
        text = text.strip()

        return text