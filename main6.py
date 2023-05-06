# exercise 6.1
def power(a, b):
    if a <= 0 or b <= 0:
        return -1
    if b == 1:
        return a
    return a * power(a, b - 1)


# exercise 6.2
def binary_search(numbers, num):
    if len(numbers) == 0: # if the list is empty, the element can't be found
        return -1
    position = len(numbers) // 2
    if numbers[position] == num: # if the element in the middle is the searched element - return it
        return num
    if num < numbers[position]: # if the searched element is smaller than the middle element:
        return binary_search(numbers[0:position], num) # - search in thr left part
    return binary_search(numbers[position+1:], num) # - otherwise search in the right part


if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        a = int(input("enter number a: "))
        b = int(input("enter number b: "))
        print(power(a, b))
    if exercise == '2':
        print(binary_search([5], 6))
        print(binary_search([2, 5, 7], 6))
        print(binary_search([2, 5, 7], 2))
        print(binary_search([2, 5, 7], 7))
        print(binary_search([2, 5, 7], 1))
        print(binary_search([2, 3, 5, 7], 7))
        print(binary_search([2, 3, 5, 7], 3))
    else:
        print(f"unknown exercise {exercise}")