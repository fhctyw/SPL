"""Module for math"""
import math
import logging

available_operators = ['+', '-', '*', '/', '^', 'sqrt', '%']

def calculator():
    """Function for standard calculator"""
    memory = None
    history = []

    # Loop for endless calculations
    while True:
        logging.info(msg="Calculator has been started")

        try:
            num1 = float(input("Enter first number: "))
        except ValueError as ve:
            print("Invalid first number. Please enter a number.")
            logging.error(ve)
            continue
        logging.info(msg=f"First number - {num1}.")

        try:
            num2 = float(input("Enter second number: "))
        except ValueError as ve:
            print("Invalid second number. Please enter a number.")
            logging.error(ve)
            continue
        logging.info(msg=f"Second number - {num2}")

        operator = input(f"Enter operator ({','.join(available_operators)}): ")

        # Checking the operator and performing calculations
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2
            elif operator == "^":
                result = num1 ** num2
            elif operator == "sqrt":
                result = math.sqrt(num1)
            elif operator == "%":
                result = num1 % num2
            else:
                raise ValueError("Invalid operator.")
        except ValueError as e:
            print(f"Error: {e}")
            continue
        logging.info(msg=f"Result - {result}.")

        # Display result
        print(f"Result: {result}")

        # Save to history
        if operator == "sqrt":
            history.append(f"√{num1} = {result}")
        else:
            history.append(f"{num1} {operator} {num2} = {result}")
        logging.info(msg="History saved.")

        # Memory functions
        mem_action = input("Do you want to save result to memory (Y/N)? ").lower()
        if mem_action == "y":
            memory = result
            print("Result saved to memory.")
            logging.info(msg=f"Save {memory} in memory")
        elif mem_action == "n" and memory is not None:
            retrieve_mem = input("Retrieve value from memory (Y/N)? ").lower()
            if retrieve_mem == "y":
                print(f"Memory value: {memory}")

        # User preferences
        decimal_places = \
            input("Enter the number of decimal places for display (default is full precision): ")
        if decimal_places.isdigit():
            print(f"Result (rounded): {round(result, int(decimal_places))}")

        # Display history
        view_history = input("View calculation history (Y/N)? ").lower()
        if view_history == "y":
            print("Calculation History:")
            for item in history:
                print(item)

        # Repeat calculation
        repeat = input("Do another calculation? (Y/N): ").lower()
        if repeat != "y":
            print("Exiting calculator.")
            break

    logging.info(msg="Calculator has been finished")

if '__main__' == __name__:
    calculator()
    