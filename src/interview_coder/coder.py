from dataclasses import dataclass
from typing import List, Optional

from interview_coder.segmenter import segment_text
from interview_coder.schema import Theme, THEMES


@dataclass
class CodedSegment:
    """
    Résultat de codage pour un segment.
    Pour l'instant : codage vide (pas d'IA).
    """
    segment: str
    theme_principal: Optional[str] = None
    themes_secondaires: List[str] = None
    justification: Optional[str] = None
    extrait: Optional[str] = None

    def __post_init__(self) -> None:
        # Évite le piège Python des valeurs par défaut mutables (list)
        if self.themes_secondaires is None:
            self.themes_secondaires = []


def available_theme_names() -> List[str]:
    """
    Retourne la liste des noms de thèmes autorisés.
    """
    return [t.name for t in THEMES]


def prepare_coding(text: str) -> List[CodedSegment]:
    """
    Segmente un entretien et prépare une liste d'objets CodedSegment.
    (Aucun codage automatique encore.)
    """
    segments = segment_text(text)
    return [CodedSegment(segment=s) for s in segments]
