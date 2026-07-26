import time


class ResponseMetrics:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            return 0.0

        return round(time.perf_counter() - self.start_time, 3)

    @staticmethod
    def estimate_tokens(text: str) -> int:
        """
        Approximate token count.
        """
        return max(1, len(text.split()) * 4 // 3)

    @staticmethod
    def estimate_cost(tokens: int) -> float:
        """
        Rough cost estimate.
        (Educational purposes only)
        """
        return round(tokens * 0.00000035, 6)