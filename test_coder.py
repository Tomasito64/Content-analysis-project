import sys
sys.path.append("src")

from interview_coder.coder import prepare_coding, available_theme_names

def main():
    text = """Je manque souvent de temps pour faire mon travail correctement.
Mon manager est à l'écoute, mais les délais sont très serrés.
Cela génère beaucoup de stress !"""

    print("Thèmes autorisés :", available_theme_names())

    coded = prepare_coding(text)
    print("Nb segments :", len(coded))

    for item in coded:
        print("-", item.segment, "| theme_principal =", item.theme_principal)

if __name__ == "__main__":
    main()
