import re

from fastapi import HTTPException


class Guardrails:

    def __init__(self):

        self.max_prompt_length = 2000

        self.blocked_patterns = [
            r"ignore previous instructions",
            r"forget previous instructions",
            r"system prompt",
            r"reveal your prompt",
            r"jailbreak",
            r"act as",
            r"developer mode",
            r"sudo",
            r"drop table",
            r"delete from",
            r"truncate table",
            r"<script>",
            r"</script>",
        ]

    def validate_prompt(self, prompt: str):

        if not prompt.strip():
            raise HTTPException(
                status_code=400,
                detail="Prompt cannot be empty.",
            )

        if len(prompt) > self.max_prompt_length:
            raise HTTPException(
                status_code=400,
                detail="Prompt too long.",
            )

    def detect_prompt_injection(self, prompt: str):

        prompt = prompt.lower()

        for pattern in self.blocked_patterns:

            if re.search(pattern, prompt):

                raise HTTPException(
                    status_code=400,
                    detail="Potential prompt injection detected.",
                )

    def check(self, prompt: str):

        self.validate_prompt(prompt)
        self.detect_prompt_injection(prompt)