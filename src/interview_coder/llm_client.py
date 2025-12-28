import requests

OLLAMA_URL = "http://localhost:11434"
MODEL = "mistral"

def ask_llm(prompt: str, timeout_s: int = 300) -> str:
    payload = {"model": MODEL, "prompt": prompt, "stream": False}
    try:
        r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=timeout_s)
        r.raise_for_status()
        return r.json()["response"]
    except requests.exceptions.ReadTimeout as e:
        raise RuntimeError(
            f"Ollama a dépassé {timeout_s}s. "
            "Essaye un prompt plus court ou augmente le timeout."
        ) from e
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(
            "Impossible de joindre Ollama sur http://localhost:11434. "
            "Vérifie qu'Ollama est lancé."
        ) from e
