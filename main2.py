# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# exercise 2.1
def count_integer(numbers, integer):
    result = 0
    for e in numbers:
        if integer == e:
            result = result + 1
    if result == 0:
        return 42
    return result

# exercise 2.2
def list_func(numbers, integer):
    result = False
    new_numbers = []
    for e in numbers:
        if e == integer:
            result = True
            new_numbers.append(6)
        else: new_numbers.append(e)
    unreversed = new_numbers.copy()
    new_numbers.reverse()
    if not result:
        empty_list = []
        return empty_list
    else:
        #print("Original list: ", numbers, "Unreversed list: ", unreversed, "Reversed list: ", new_numbers)
        print(new_numbers)
    return unreversed

# exercise 2.3
def compare_lists(list1, list2):
    list = []
    for e in list1:
        if e in list2:
            list.append(e)
    return list

# exercise 2.4
def remove_duplicates(lst):
   list = []
   for e in lst:
       if e not in list:
           list.append(e)
   return list

# exercise 2.5
def dict_func(dictionary):
    type = "unknown type"
    if "Type" in dictionary:
        type = dictionary["Type"]
    brand = "unknown brand"
    if "Brand" in dictionary:
        brand = dictionary["Brand"]
    price = "unknown price"
    if "Price" in dictionary:
        price = dictionary["Price"]
    print(f'You have a {type} from {brand} that costs {price}.')
    dictionary["OS"] = "Linux"
    print(dictionary)
    return dictionary


if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        print("exercise 1:")
        numbers = []
        s = input("enter a number or nothing: ")
        while s != "":
            numbers.append(int(s))
            s = input("enter a number or nothing: ")
        integer = int(input("enter number to search: "))
        print(count_integer(numbers, integer))
    elif exercise == '2':
        print("exercise 2:")
        numbers = []
        s = input("enter a number or nothing: ")
        while s != "":
            numbers.append(int(s))
            s = input("enter a number or nothing: ")
        integer = int(input("enter number to be replaced by 6: "))
        print(list_func(numbers, integer))
    elif exercise == '3':
        print("exercise 3:")
        list_one = []
        list_two = []
        s = input("first list - enter a string or nothing: ")
        while s != "":
            list_one.append(s)
            s = input("first list - enter a string or nothing: ")
        s = input("second list - enter a string or nothing: ")
        while s != "":
            list_two.append(s)
            s = input("second list - enter a string or nothing: ")
        print(compare_lists(list_one, list_two))
    elif exercise == '4':
        print("exercise 4:")
        lst = []
        s = input("enter a string or nothing: ")
        while s != "":
            lst.append(s)
            s = input("enter a string or nothing: ")
        print(remove_duplicates(lst))
    elif exercise == '5':
        print("exercise 5:")
        dictionary = {}
        type = input("input type or nothing: ")
        if type != "":
            dictionary["Type"] = type
        brand = input("input brand or nothing: ")
        if brand != "":
            dictionary["Brand"] = brand
        price = input("input price or nothing: ")
        if price != "":
            dictionary["Price"] = int(price)
        dict_func(dictionary)
    else:
        print(f"unknown exercise {exercise}")