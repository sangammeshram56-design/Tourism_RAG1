import requests

from app.config import (
    NUGEN_API_KEY,
    NUGEN_LLM_MODEL
)


NUGEN_COMPLETION_URL = (
    "https://api.nugen.in/api/v3/inference/completions"
)


def generate_answer(prompt):

    headers = {
        "Authorization": f"Bearer {NUGEN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": NUGEN_LLM_MODEL,
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.2,
        "stream": True
    }

    response = requests.post(
        NUGEN_COMPLETION_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return extract_answer(data)


def extract_answer(data):

    if "choices" in data:

        choice = data["choices"][0]

        if "text" in choice:
            return choice["text"].strip()

        if "message" in choice:
            return choice[
                "message"
            ]["content"].strip()

    if "text" in data:
        return data["text"].strip()

    raise ValueError(
        f"Unexpected Nugen response: {data}"
    )