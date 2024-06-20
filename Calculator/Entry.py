from Enums import Symbol, Type
from CustomExceptions import BadTypeException 

class Entry:
    # Constructor for all possible instances of Entry
    def __init__(self, num = None, sign = None, input_str = None):
        self.num = None
        self.sign = None
        self.input = None
        self.input_str = None
        self.value_string = None
        self.entry_type = Type.INVALID

    # Sets values for every possible argument type (Float, Symbol, String)
        if isinstance(num, float):
            self.num = num
            self.entry_type = Type.NUMBER
            self.value_string = str(num)
        elif isinstance(sign, Symbol):
            self.sign = sign
            if sign == Symbol.INVALID:
                raise 
            self.entry_type = Type.SYMBOL    
            self.value_string = str(sign)
        elif isinstance(input_str, str):
            self.input = input
            self.entry_type = Type.STRING
            self.value_string = input_str

    # Getters for all instances of Entry    
    def get_type(self):
        return self.entry_type
    def get_num(self):
        if self.entry_type != Type.NUMBER:
            raise BadTypeException("Bad Type: The 'Float' value doesn't exist for this item")
        return self.num
    def get_sign(self):
        if self.entry_type != Type.SYMBOL:
            raise BadTypeException("Bad Type: The 'Sign' value doesn't exist for this item")
        return self.sign
    def get_string(self):
        if self.entry_type != Type.STRING:
            raise BadTypeException("Bad Type: The 'String' value doesn't exist for this item")
        return self.input
    

    # Function to determine if two Entries are equal
    def __eq__(self, other):
        if not isinstance(other, Entry):
            return False
        elif self.type == other.type:
            if self.type == Type.NUMBER:
                return self.num == other.num
            elif self.type == Type.SYMBOL:
                return self.sign == other.sign
            elif self.type == Type.STRING:
                return self.string == other.string
        return False
    
    # Assigns a unique hashcode to each Entry
    def __hash__(self):
        prime = 31
        result = 0
        if self.type == Type.NUMBER:
            result = prime + hash(self.num)
        elif self.type == Type.SYMBOL:
            result = prime + hash(self.sign)
        elif self.type == Type.STRING:
            result = prime + hash(self.input)
        return result