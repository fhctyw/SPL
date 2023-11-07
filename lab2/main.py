from .tools.base_menu import BaseMenu
from .components.operators import *
from .components.user import User
from .src.calc import Calculator

def user_auth(m, p: Calculator):
    user_name = input('Enter user name: ')
    for user in p.users:
        if user.name == user_name:
            p.current_user = user
            return
    
    float_precision = int(input('Enter float precision: '))
    p.current_user = User(user_name, float_precision)
    p.users.append(p.current_user)

def list_users(m, p: Calculator):
    for user in p.users:
        print(user.name)

def user_info(m, p: Calculator):
    if p.current_user == None:
        print('You should authorize to see user\'s info')
        return
    else:
        print(f'User name: {p.current_user.name}\n' + 
              f'User float precision: {p.current_user.float_precision}\n' + 
              'User memory: ')
        for index_memory in range(len(p.current_user.memory)):
            print(f'm{index_memory} = ' + str(p.current_user.memory[index_memory]))
        print("History: ")
        for note in p.current_user.history:
            print(note)

def do_math(m, p: Calculator):
    while True:
        current_operation = input(f'Choose operation({p.list_sign}): ')
        for operation in p.operations:
            if operation.sign == current_operation:
                p.current_operation = operation
                break
        
        if p.current_operation == None:
            raise "This operation is not available"
        
        input1 = input('Enter first number or m{memory index}: ')
        if input1[0] == 'm':
            index = int(input1[1:]) - 1
            if index < 0 and index >= len(p.current_user.memory):
                break
            p.number1 = p.current_user.memory[index]
        else:
            p.number1 = float(input1)
        input2 = input('Enter second number or m{memory index}: ')
        if input2[0] == 'm':
            index = int(input2[1:]) - 1
            if index < 0 and index >= len(p.current_user.memory):
                break
            p.number2 = p.current_user.memory[index]
        else:
            p.number2 = float(input2)
        
        p.number1 = round(p.number1, p.current_user.float_precision)
        p.number2 = round(p.number2, p.current_user.float_precision)
        p.result = round(p.current_operation.calc(p.number1, p.number2), p.current_user.float_precision)      
        note = str(p.number1) + ' ' + str(p.current_operation.sign) + ' ' + str(p.number2) + ' = ' + str(p.result)
        print(note)
        p.current_user.history.append(note)
        is_memorize = input("Wanna memorize a result? y/n: ")
        if is_memorize == 'y':
            p.current_user.memory.append(p.result)
        p.current_operation = None
        p.number1 = None
        p.number2 = None
        p.result = None
        repeat = input('Wanna do again? y/n: ').lower()
        if repeat == 'n':
            break

def main():
    
    calc = Calculator()
    calc.menu.add_option(BaseMenu.Option(user_auth, 'Auth'))
    calc.menu.add_option(BaseMenu.Option(list_users, 'List users'))
    calc.menu.add_option(BaseMenu.Option(user_info, 'User\'s Info'))
    calc.menu.add_option(BaseMenu.Option(do_math, 'Do math'))
    
    calc.run()

if '__main__' == __name__:
    main()