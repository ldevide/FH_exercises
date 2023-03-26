my_list = [1, 2, 3, 4, 5, 6]

#for i in my_list:
  #  print(i)
    # print(i >= 3)
  #  if i >= 3:
     #   my_list.remove(i)
      #  print(f'{i} inside if')
     #   print(i >= 3)
    # print(my_list)

#for i in my_list:
 #   print(i)
  #  print(i >= 1)
   # if i >= 1:
    #    my_list.remove(i)
     #   print(f'{i} inside if')
      #  print(i >= 1)
    #print(my_list)

my_list = [2, 4, 8, 6]

my_list.sort()
# sorts in the same list

#print(my_list)

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
#print(x)
# sorts in a new list

my_tuple = ('cat', 'dog', 'bird')
#print(my_tuple)
def Reverse(my_tuple):

    new_tup = my_tuple[::-1]
    return new_tup

#print(Reverse(my_tuple))
# slicing: we create a new tuple and assign it


my_set = {'cat', 'DOG', 'cat'}

# list [], tuple (), set {} ???

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#z = x.difference(y)

#print(z)

#x.difference_update(y)

#print(x)


#z = x.intersection(y)

#print(z)

#x.intersection_update(y)

#print(x)


# Dictionary Exercise:
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}


element = fruits.pop('banana')
print(element)

fruits.popitem()
print(fruits)