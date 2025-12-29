from interview_coder.llm_client import code_segment
from interview_coder.schema import THEMES

segment = "Je manque souvent de temps pour faire mon travail correctement. Les délais sont trop serrés. Nous sommes trop peux nombreuses pour pouvoir faire un travail qualitatif. J'aime beaucoup la couleur rouge."
print(code_segment(segment, THEMES))
