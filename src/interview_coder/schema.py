from dataclasses import dataclass
from typing import List

@dataclass
class Theme:
    """
    Représente un thème d'analyse de contenu.
    """
    name: str
    description: str

THEMES: List[Theme] = [
    Theme(
        name="Charge de travail",
        description="Intensité, volume, rythme, pression temporelle."
    ),
    Theme(
        name="Autonomie",
        description="Marges de manœuvre, liberté d'organisation, initiative."
    ),
    Theme(
        name="Soutien managérial",
        description="Aide, écoute, reconnaissance de la hiérarchie."
    ),
    Theme(
        name="Soutien des collègues",
        description="Entraide, coopération, collectif de travail."
    ),
    Theme(
        name="Reconnaissance et justice",
        description="Équité, valorisation, reconnaissance du travail fourni."
    ),
    Theme(
        name="Conflits de rôle",
        description="Injonctions contradictoires, ambiguïtés de rôle."
    ),
    Theme(
        name="Sens du travail",
        description="Utilité perçue, valeurs, cohérence du travail."
    ),
    Theme(
        name="Ressources et organisation",
        description="Moyens matériels, outils, processus, organisation."
    ),
    Theme(
        name="Communication",
        description="Circulation de l'information, coordination."
    ),
    Theme(
        name="Climat et conflits",
        description="Tensions relationnelles, conflits ouverts ou latents."
    ),
    Theme(
        name="Santé et stress",
        description="Fatigue, stress, atteintes à la santé."
    ),
    Theme(
        name="Leviers et solutions",
        description="Propositions d'amélioration, pistes d'action."
    ),
    Theme(
        name="Qualité empéchée",
        description="Manque de moyens pour faire un travail de qualité."
    ),
    Theme(
        name="Neutre",
        description="Pas de lien direct avec les situations de travail."
    ),
]
