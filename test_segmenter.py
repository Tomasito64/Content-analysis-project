import sys
sys.path.append("src")

from interview_coder.segmenter import segment_text

def main():
    text = """Je manque souvent de temps pour faire mon travail correctement.
Mon manager est à l'écoute, mais les délais sont très serrés.
Cela génère beaucoup de stress !"""

    segments = segment_text(text)

    for s in segments:
        print("-", s)

if __name__ == "__main__":
    main()

