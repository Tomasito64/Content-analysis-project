# Content Analysis Project

This project provides a Python-based pipeline for qualitative content analysis of interview transcripts (French language).

It is designed for research and applied work in social and organizational psychology, with a focus on transparency, reproducibility, and data confidentiality.

## Prerequisites

-   Python 3.10 or higher
-   Git

## Prerequisites

## Installation

Clone the repository:

\`\`\`bash git clone https://github.com/Tomasito64/Content-analysis-project.git cd Content-analysis-project

python -m venv .venv call .venv\Scripts\activate.bat

pip install -e .

## Local LLM (Ollama)

Ce projet utilise un modèle de langage **local** via **Ollama**.  
Aucune donnée n’est envoyée vers un service externe.

### Installation (une seule fois)

1. Installer Ollama  
     https://ollama.com

2. Vérifier l’installation
```bash
ollama --version

ollama pull mistral

http://localhost:11434


# Project

+---Content_analysis_project \| dependency_links.txt \| PKG-INFO \| requires.txt \| SOURCES.txt \| top_level.txt \| ---interview_coder \| aggregate.py \| coder.py \| llm_client.py \| schema.py \| segmenter.py \| **init**.py \| ---**pycache** coder.cpython-310.pyc schema.cpython-310.pyc segmenter.cpython-310.pyc **init**.cpython-310.pyc