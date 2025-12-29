import json
import requests
from interview_coder.schema import CodingResult

OLLAMA_URL = "http://localhost:11434"
MODEL = "mistral"


def ask_llm(prompt: str, timeout_s: int = 3000) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1
        }
    }

    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=timeout_s,
        )
        r.raise_for_status()
        return r.json()["response"]

    except requests.exceptions.ReadTimeout as e:
        raise RuntimeError(
            f"Ollama a dépassé {timeout_s}s. "
            "Essaie un prompt plus court ou augmente le timeout."
        ) from e

    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(
            "Impossible de joindre Ollama sur http://localhost:11434. "
            "Vérifie qu'Ollama est lancé."
        ) from e


def code_segment(segment: str, themes: list[str]) -> CodingResult:
    prompt = (
        "Tu es un assistant d'analyse de contenu.\n"
        "Retourne UNIQUEMENT un objet JSON valide, sans aucun texte autour.\n"
        "Le JSON doit respecter exactement ce schéma :\n"
        '{ "themes": [string], "rationale": string }\n\n'
        f"Liste des thèmes autorisés : {themes}\n\n"
        f"Segment : {segment}\n"
    )

    raw = ask_llm(prompt).strip()

    # Extraction défensive du JSON
    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError(f"Réponse non JSON :\n{raw}")

    data = json.loads(raw[start : end + 1])

    # Validation stricte via Pydantic
    return CodingResult(**data)

