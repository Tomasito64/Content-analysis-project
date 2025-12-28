from interview_coder.llm_client import code_segment
from interview_coder.schema import THEMES

segment = "Je manque souvent de temps pour faire mon travail correctement. Les délais sont trop serrés."
print(code_segment(segment, THEMES))
