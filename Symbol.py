from enum import Enum

class Symbol(Enum):
    LEFT_BRACKET = "("
    RIGHT_BRACKET = ")"
    DIVIDE = "/"
    TIMES = "*"
    PLUS = "+"
    MINUS = "-"

    def __str__(self):
        return self.value
    