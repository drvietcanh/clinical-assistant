"""
Antibiotics Education Module
Educational content: quizzes, case studies, learning paths
"""

try:
    from .quizzes import render_quizzes, get_quiz_questions
    from .case_studies import render_case_studies, get_case_studies
    __all__ = ['render_quizzes', 'get_quiz_questions', 'render_case_studies', 'get_case_studies']
except ImportError:
    __all__ = []
