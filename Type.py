from enum import Enum

class Type(Enum):
    STRING = "string"
    NUMBER = "number"
    SYMBOL = "symbol"
    INVALID = "invalid"

    def __str__(self):
        return self.value
    