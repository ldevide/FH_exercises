# TEST -> questions on paper + loop: we have to say what it does !!!
# everything in python is an object

class Car():
    _colour = ''
    def __init__(self, brand):
    # def __init__(self, brand, colour):
        self.my_brand = brand
        # self.my_colour = colour
        # pass
# as soon as we create an object the init structure is activated

my_car = Car('Toyota')
my_car2 = Car('Ford')

print(my_car.my_brand)
print(my_car2.my_brand)

print (F"The colour of the car is {my_car._colour}")
my_car._colour = 'red'
print (F"The colour of the car is {my_car._colour}")



class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def makes_noise(self):
        print("Hello I'm a student")
        # NotImplementedError

    #def get_colour(self):
    def __str__(self):
        return f"Hello I'm a student with the id {self.id} and my name is {my_student.first_name} {my_student.last_name}"

    def __len__(self):
        return self.id

my_person = Person('Lea', 'Devide')
print(f"The name of my person is {my_person.first_name} {my_person.last_name}")

class Student(Person):
    _colour = 'blue'
    def __init__(self, first_name, last_name, id: int):
        Person.__init__(self, first_name, last_name)
        self.id = id

my_student = Student(first_name='Maria', last_name='Poljak', id='1')
print(f"The name of my student is {my_student.first_name} {my_student.last_name}")

my_student.makes_noise()


print(f"My id is {my_student.id}")

#def test()

my_list = list([1, 2, 3])
print(my_list)
print(my_student)

print(len(my_list))
#print(len(my_student))

#print(my_student.get_colour())



# EXERCISE class Dish;
print("EXERECISE Class Dish:")
class Dish():
    is_clean = False
    # _is_clean = False
    def __init__(self, name):
        self.name = name

    def clean(self):
        self.is_clean = True

    def __str__(self):
        if self.is_clean:
            return f"The dish {self.name} is clean."
        else:
            return f"The dish {self.name} is not clean."

plate = Dish('plate')
print(plate.name)
#print(plate.is_clean)
print(plate)

# EXERCISE Plate, Cup, Pan and Pot:

cup = Dish('cup')
print(cup.name)
print(cup)
pan = Dish('pan')
print(pan.name)
print(pan)
pot = Dish('pot')
print(pot.name)
print(pot)