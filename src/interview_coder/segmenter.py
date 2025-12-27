from typing import List
import re

def segment_text(text: str) -> List[str]:
    """
    Découpe un texte d'entretien en segments (phrases).
    
    Paramètres
    ----------
    text : str
        Texte brut de l'entretien.

    Retour
    ------
    List[str]
        Liste de segments textuels nettoyés.
    """

    if not text or not isinstance(text, str):
        return []

    # Nettoyage simple
    cleaned = text.strip()

    # Découpage naïf par ponctuation finale
    raw_segments = re.split(r"[.!?]\s+", cleaned)

    # Nettoyage final
    segments = [
        seg.strip()
        for seg in raw_segments
        if len(seg.strip()) > 3
    ]

    return segments