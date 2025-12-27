import sys
sys.path.append("src")

from interview_coder.schema import THEMES

def main():
    print("Nombre de thèmes :", len(THEMES))
    print("Premier thème :", THEMES[0].name)
    print("Description :", THEMES[0].description)

if __name__ == "__main__":
    main()
