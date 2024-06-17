def clear():
    import os
    os.system('cls')


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1 / n2

operations ={'+': add,
             '-': subtract,
             '*': multiply,
             '/': divide,
            }

from calculator_logo import logo 
def calculator():
    print (logo)
    num1 = float(input("What's the first number?: "))
    for operand in operations:
        print(operand)
    end = True
    while end:
        operand_symbol = input("Pick an operand from above: ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operand_symbol]
        answer = calculation(num1,num2)
        print(f"{num1} {operand_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start another calculation.: ")=="y":
            num1 = answer
        else:
            end = False
            clear()
            calculator() ## recursion
calculator()

