import Type
import Symbol
import BadTypeException

class Entry:
    
    def __init__(self, num = None, sign = None, input_str = None):
        self.num = None
        self.sign = None
        self.input = None
        self.input_str = None
        self.value_string = None
        self.entry_type = Type.INVALID

        if isinstance(num, float):
            self.num = num
            self.entry_type = Type.NUMBER
            self.value_string = str(num)

        elif isinstance(sign, Symbol):
            self.sign = sign
            if sign != Symbol.INVALID:
                self.entry_type = Type.SYMBOL
            self.value_string = str(sign)
        
        elif isinstance(input_str, str):
            self.input = input
            self.entry_type = Type.STRING
            self.value_string = input_str
        
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