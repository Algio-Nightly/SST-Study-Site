"""
Comprehensive Multi-Correct Quiz Definitions for Lectures 09 through 13
Aggregates modular quiz definitions from quiz_l09, quiz_l10, quiz_l11, quiz_l12, and quiz_l13.
Every question is a 5-option multi-correct question with 2 to 5 correct answers.
"""

from typing import Dict, Any
from quiz_l09 import QUIZ_L09
from quiz_l10 import QUIZ_L10
from quiz_l11 import QUIZ_L11
from quiz_l12 import QUIZ_L12
from quiz_l13 import QUIZ_L13

def get_lectures_09_to_13_quizzes() -> Dict[str, Any]:
    return {
        "lecture-09": QUIZ_L09,
        "lecture-10": QUIZ_L10,
        "lecture-11": QUIZ_L11,
        "lecture-12": QUIZ_L12,
        "lecture-13": QUIZ_L13,
    }
