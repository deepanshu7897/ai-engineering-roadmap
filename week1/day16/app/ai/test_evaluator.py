from app.ai.evaluator import LLMEvaluator

evaluator = LLMEvaluator()

results = evaluator.evaluate()

print()

for result in results:

    print("=" * 80)

    print("Question:")
    print(result["question"])

    print()

    print("Score:")
    print(result["score"])

    print()

    print("Response:")
    print(result["response"])

    print()