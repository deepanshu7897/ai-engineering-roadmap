from app.ai.gemini_client import GeminiClient
from app.ai.evaluation_data import EVALUATION_DATASET


class LLMEvaluator:
    def __init__(self):
        self.client = GeminiClient()

    def keyword_score(
        self,
        response: str,
        expected_keywords: list[str],
    ) -> float:

        response = response.lower()

        matches = 0

        for keyword in expected_keywords:
            if keyword.lower() in response:
                matches += 1

        return matches / len(expected_keywords)

    def evaluate(self):

        results = []

        for sample in EVALUATION_DATASET:

            response = self.client.generate(sample["question"])

            score = self.keyword_score(
                response=response,
                expected_keywords=sample["expected_keywords"],
            )

            results.append(
                {
                    "question": sample["question"],
                    "score": round(score, 2),
                    "response": response,
                }
            )

        return results