from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, Field, validator
from pydantic import BaseModel, Field, field_validator


# -------------------------
# Référentiel théorique
# -------------------------

@dataclass
class Theme:
    """
    Représente un thème d'analyse de contenu.
    """
    name: str
    description: str


THEMES: List[Theme] = [
    Theme("Charge de travail", "Intensité, volume, rythme, pression temporelle."),
    Theme("Autonomie", "Marges de manœuvre, liberté d'organisation, initiative."),
    Theme("Soutien managérial", "Aide, écoute, reconnaissance de la hiérarchie."),
    Theme("Soutien des collègues", "Entraide, coopération, collectif de travail."),
    Theme("Reconnaissance et justice", "Équité, valorisation, reconnaissance."),
    Theme("Conflits de rôle", "Injonctions contradictoires, ambiguïtés de rôle."),
    Theme("Sens du travail", "Utilité perçue, valeurs, cohérence du travail."),
    Theme("Ressources et organisation", "Moyens matériels, outils, processus."),
    Theme("Communication", "Circulation de l'information, coordination."),
    Theme("Climat et conflits", "Tensions relationnelles, conflits."),
    Theme("Santé et stress", "Fatigue, stress, atteintes à la santé."),
    Theme("Leviers et solutions", "Pistes d'amélioration, actions possibles."),
    Theme("Qualité empêchée", "Empêchement de faire un travail de qualité."),
    Theme("Neutre", "Pas de lien direct avec le travail."),
]

# Liste des noms autorisés (pour l'IA)
THEME_NAMES = [t.name for t in THEMES]


# -------------------------
# Schéma de sortie IA
# -------------------------


class CodingResult(BaseModel):
    themes: List[str] = Field(..., description="Liste des thèmes identifiés")
    justification: str = Field(..., description="Justification du codage")

    @field_validator("themes")
    @classmethod
    def validate_themes(cls, v: List[str]) -> List[str]:
        invalid = [t for t in v if t not in THEME_NAMES]
        if invalid:
            raise ValueError(f"Thèmes non autorisés : {invalid}")
        return v

