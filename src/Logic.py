class Logic:
    
    def __init__(self):
        self.map_op_to_state = {
            "+": "ADD",
            "-": "SUBTRACT",
            "/":"DIVIDE",
            "x": "MULTIPLY",
            "=": "EQUAL",
        }
        self.reset()

    def reset(self):
        self.STATE = "START"
        self.first_value = 0
        self.second_value = 0
        self.output = 0

    def get_mapping(self):
        return self.map_op_to_state

    def START(self, x, *args):
        return x

    def set_operation(self, op):
        self.STATE = self.map_op_to_state[op]      
        
    def set_value(self, i):
        if self.STATE == "START":
            self.first_value = self.first_value * 10 + i
        else:
            self.second_value = self.second_value * 10 + i
            
    def calulate(self, x, op, y):
        self.method = getattr(self, op)
        self.output =  self.method(x, y)
        
    def ADD(self, x, y):
        return x + y
    
    def SUBTRACT(self, x, y):
        return x - y

    def DIVIDE(self, x, y):
        try:
            m =  x / y
        except ZeroDivisionError:
            m = x
        return m
    
    def MULTIPLY(self, x , y):
        print(x, y)
        return x * y

    def EQUAL(self, *args):
        self.STATE = "START"
        return self.output

    def execute(self, in_data: str) -> str: 
        _ins = self.parse_input(in_data)
        if len(_ins) == 0:
            self.output = 0
        else: 
            [self.calculate(_in) for _in in _ins]
        data = str(self.output)
        self.reset()
        return data

    def calculate(self, in_data):
        try:
            in_data = int(in_data)
            self.set_value(in_data)
        except ValueError:
            self.set_operation(in_data)
            self.first_value = self.output
            self.second_value = 0
        self.calulate(self.first_value, self.STATE, self.second_value)

    def parse_input(self, text: str) -> list:
        print(text)
        data =  [txt for txt in text]
        print(data)
        return data