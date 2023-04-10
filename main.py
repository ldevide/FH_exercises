# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# exercise 3.1
def count_vowels(text):
    if type(text) != str:
        return 42
    result = 0
    vowels = 'AaEeIiOoUu'
    for letter in text:
        if letter in vowels:
            result = result + 1
    return result

# exercise 3.2
def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    result = 0
    for index in range(len(text1)):
        if text1[index] != text2[index]:
            result = result + 1
    return result

# exercise 3.3
class Vehicle():
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type
    def __str__(self):
        return f'Color: {self.color}, Fuel Type: {self.fuel_type}'

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        Vehicle.__init__(self, color, fuel_type)
        self.doors = doors
    def __str__(self):
        return Vehicle.__str__(self)+f', Doors: {self.doors}'

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        Vehicle.__init__(self, color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return Vehicle.__str__(self)+f', Passengers: {self.passengers}'

# exercise 3.4
class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
        return f'{self.name}, {self.author}'

# exercise 3.5
class BookShelf():
    def __init__(self):
        self.books = []
    def add_book_list(self,books):
        for book in books:
            if type(book) == Book:
                self.books.append(book)

    def books_by_author(self, author):
        result = []
        for book in self.books:
            if author == book.author:
               result.append(book.name)
        return result

    def get_books(self):
        result = []
        for book in self.books:
            result.append(book.name)
        return result

    def clear_shelf(self):
        self.books = []


if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        print("exercise 1:")
        text = input("enter a string: ")
        print(count_vowels(text))
        number = int(input("enter a number: "))
        print(count_vowels(number))
    elif exercise == '2':
        print("exercise 2:")
        text1 = input("enter a string: ")
        text2 = input("enter a string: ")
        print(hamming(text1, text2))
    elif exercise == '3':
        print("exercise 3:")
        my_car = Car("red", "petrol", 5)
        my_bus = Bus("blue", "diesel", 42)
        print(my_car)
        print(my_bus)
    elif exercise == '4':
        print("exercise 4:")
        my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
        print(my_book)
    elif exercise == '5':
        print("exercise 5:")
        my_shelf = BookShelf()
        my_shelf.add_book_list([Book("AAA", "BB CC"), Book("DDD", "EE FF"), Book("GGG", "EE FF"), Car("red", "petrol", 5)])
        print(my_shelf.books_by_author("EE FF"))
        print(my_shelf.get_books())
        my_shelf.add_book_list([Book("HHH", "II JJ")])
        print(my_shelf.get_books())
        my_shelf.clear_shelf()
        print(my_shelf.books_by_author("EE FF"))
        print(my_shelf.get_books())
    else:
        print(f"unknown exercise {exercise}")