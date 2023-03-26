# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# exercise 1.1
def name_age():
    name = input("enter name: ")
    age = input("enter age: ")
    print(f'Hello {name}. Your age is: {age}')
    return name+age

# exercise 1.2
def swap_integers(num1, num2):
    print(f'num1={num1}, num2={num2}')
    num3 = num1
    num1 = num2
    num2 = num3
    print(f'num1={num1}, num2={num2}')
    # alternative: return str(num1)+num2
    # alternative: return f'{num1}{num2}'
    return num1 + num2

# exercise 1.3
def check_numbers(num1, num2):
    print(f'num1={num1}, num2={num2}')
    result1 = num1 % 6 == 0 or num2 % 6 == 0
    if result1:
        print("At least one number is divisible by 6")
    result2 = num1 % 10 != 0 and num2 % 10 != 0
    if result2:
        print("Both numbers are not divisible by 10")
    return result1 and result2

# exercise 1.4
def sum_up(num1, num2):
    print(f'num1={num1}, num2={num2}')
    if num2 < num1:
        return 0
    if num1 < 0 or num2 < 0:
        return 0
    result = num1
    x = num1
    while x < num2:
        x = x + 1
        result = result + x
    return result

# exercise 1.5
def area (r):
    pi = 3.142
    return pi * r * r
def circle_area(r1, r2, r3):
    a1 = area (r1)
    a2 = area (r2)
    a3 = area (r3)
    return r1 + r2 + r3

# exercise 1.6
def check_string(text):
    textc = text.capitalize()
    result = textc.startswith("A") or textc.endswith("a")
    return result

# exercise 1.7
def triangle(rows):
    x = 1
    while x <= rows:
        print("* "*x)
        x = x + 1

if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        print("exercise 1:")
        print (name_age())
    elif exercise == '2':
        print("exercise 2:")
        n1 = input("enter number 1: ")
        n2 = input("enter number 2: ")
        print(swap_integers(n1, n2))
    elif exercise == '3':
        print("exercise 3:")
        n1 = int(input("enter number 1: "))
        n2 = int(input("enter number 2: "))
        print(check_numbers(n1, n2))
    elif exercise == '4':
        print("exercise 4:")
        n1 = int(input("enter number 1: "))
        n2 = int(input("enter number 2: "))
        print(sum_up(n1, n2))
    elif exercise == '5':
        print("exercise 5:")
        r1 = float(input("enter number 1: "))
        r2 = float(input("enter number 2: "))
        r3 = float(input("enter number 3: "))
        print(circle_area(r1, r2, r3))
    elif exercise == '6':
        print("exercise 6:")
        text = input("enter text: ")
        print(check_string(text))
    elif exercise == '7':
        print("exercise 7:")
        nr = int(input("enter number: "))
        (triangle(nr))
    else:
        print(f"unknown exercise {exercise}")