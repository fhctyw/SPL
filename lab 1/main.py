# User class who has memory, history, float precision
class User:
    def __init__(self, name: str, float_precision: int) -> None:
        self.name: str = name
        self.history: list[str] = []
        self.memory: list[float] = []
        self.float_precision = float_precision

# Operator class for implementation operation in Calculator class
# Required: sign, calculation method
class Operator:
    def __init__(self, sign) -> None:
        self.sign = sign

    def calc(self, number1: float, number2: float) -> float:
        raise "Method is not implemented"

class PlusOperator(Operator):
    def __init__(self) -> None:
        super().__init__('+')

    def calc(self, number1: float, number2: float) -> float:
        return number1 + number2

class MinusOperator(Operator):
    def __init__(self) -> None:
        super().__init__('-')

    def calc(self, number1: float, number2: float) -> float:
        return number1 - number2

class MultOperator(Operator):
    def __init__(self) -> None:
        super().__init__('*')

    def calc(self, number1: float, number2: float) -> float:
        return number1 * number2

class DivOperator(Operator):
    def __init__(self) -> None:
        super().__init__('/')

    def calc(self, number1: float, number2: float) -> float:
        return number1 / number2

# Calculator class which has run method that starts loop 
class Calculator:
    def __init__(self, operations = None, users = None) -> None:

        self.operations: list[Operator] = operations if operations else []
        self.users: list[User] = users if users else []

        self.current_user = None
        self.current_operation = None
            
        self.number1 = None
        self.number2 = None
            
        self.result = None

    @property
    def list_sign(self):
        return ", ".join([op.sign for op in self.operations]) if hasattr(self.operations, '__iter__') else self.operations[0]

    def user_auth(self):
        user_name = input('Enter user name: ')
        for user in self.users:
            if user.name == user_name:
                self.current_user = user
                return
        
        float_precision = int(input('Enter float precision: '))
        self.current_user = User(user_name, float_precision)
        self.users.append(self.current_user)

    def run(self):
        self.user_auth()

        while True:
            print('1. Auth\n\
2. List users\n\
3. User\'s Info\n\
4. Do math\n\
0. Exit')

            choice = int(input('Choose actions: '))
            
            match choice:
                case 1:
                    self.user_auth()
                case 2:
                    for user in self.users:
                        print(user.name)
                case 3:
                    if self.current_user == None:
                        print('You should authorize to see user\'s info')
                        break
                    else:
                        print(f'User name: {self.current_user.name}\n' + 
                              f'User float precision: {self.current_user.float_precision}\n' + 
                              'User memory: ')
                        for index_memory in range(len(self.current_user.memory)):
                            print(f'm{index_memory} = ' + str(self.current_user.memory[index_memory]))
                        print("History: ")
                        for note in self.current_user.history:
                            print(note)
                case 4: 
                    while True:
                        current_operation = input(f'Choose operation({self.list_sign}): ')
                        for operation in self.operations:
                            if operation.sign == current_operation:
                                self.current_operation = operation
                                break
                        
                        if self.current_operation == None:
                            raise "This operation is not available"
                        
                        input1 = input('Enter first number or m{memory index}: ')
                        if input1[0] == 'm':
                            index = int(input1[1:]) - 1
                            if index < 0 and index >= len(self.current_user.memory):
                                break
                            self.number1 = self.current_user.memory[index]
                        else:
                            self.number1 = float(input1)

                        input2 = input('Enter second number or m{memory index}: ')
                        if input2[0] == 'm':
                            index = int(input2[1:]) - 1
                            if index < 0 and index >= len(self.current_user.memory):
                                break
                            self.number2 = self.current_user.memory[index]
                        else:
                            self.number2 = float(input2)
                        


                        self.number1 = round(self.number1, self.current_user.float_precision)
                        self.number2 = round(self.number2, self.current_user.float_precision)

                        self.result = round(self.current_operation.calc(self.number1, self.number2), self.current_user.float_precision)      
                        note = str(self.number1) + ' ' + str(self.current_operation.sign) + ' ' + str(self.number2) + ' = ' + str(self.result)
                        print(note)
                        self.current_user.history.append(note)

                        is_memorize = input("Wanna memorize a result? y/n: ")
                        if is_memorize == 'y':
                            self.current_user.memory.append(self.result)

                        self.current_operation = None
                        self.number1 = None
                        self.number2 = None
                        self.result = None

                        repeat = input('Wanna do again? y/n: ').lower()

                        if repeat == 'n':
                            break
                case 0:
                    break
            print()
            
def main():
    calculator = Calculator([PlusOperator(), MinusOperator(), MultOperator(), DivOperator()])
    calculator.run()

if '__main__' == __name__:
    main()