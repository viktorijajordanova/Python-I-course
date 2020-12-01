"""Funkcii"""
"""Domasni"""

list1 = [1,2,3,4,5,6]
for l in range(0, len(list1)):
    if l%3 == 0:
        print(list1[l])


cTuple = ("lemon", "blueberry", "strawberry", "apple", "orange")

if "orange" in cTuple:
    print(cTuple.index("orange"))


dict = {

    "city" : "New York",
    "country":"New York",
    "population": 7000000,
    "coastline": "east"

}
#
for item in dict.items():
    print(item)

for value in dict.values():
    print(value)

for key in dict.keys():
    print(key)


def favourite_book(book):
    print ("My favourite book is " + book)


favourite_book("Myths")
favourite_book("Luna")


def name(first_name, last_name):
    print("My first name is " + first_name + " and my last name is " + last_name)


name("Viktorija", "Jordanova")


def display_message():
    print("This chapter is about functions in Python")


display_message()

# Funkcija so koja se presmetuva suma na elementi vo lista, lista da bide vlezen parametar i so int ili so float

def suma(list):
    print(sum(list))


suma([1,5,6,8,9,2])


def t_shirt(size, message):
    print("This T-Shirt is size " + size + " and the message says: " + message)


t_shirt("M", "I love Python")

def make_shirt(size, text):
    print("Your size is " + size)
    print("Printed text: " + text)

make_shirt("L", "Just smile! :)")

def div_by_five(a):
    if a%5 == 0:
        print("Is divisible by five")
    else:
        print("Not divisible by five")

div_by_five(9)

"""Default parametri"""

def describe_city(city, country = "Macedonia"):
    print(city + " is in " + country)

describe_city("Skopje")


"""Kvadraten koren na broj"""
def square(x):
    return x*x

square(2)

square(4)

"""Pass"""
def multiply():
    pass

def my_func(a):
    return a*5

print(my_func(6))



"""Absolutna vrednost na broj - funkcija"""
def abs_value(num):
    if num >= 0:
        return num
    elif num < 0:
        return -num

# print(abs_value(9))
print(abs_value(-9))


"""Da se isprintaat parni broevi od tuple so funkcija"""

def parni_broevi(aTuple):
    for t in aTuple:
        if t%2 != 0:
            print(t)
        else:
            print("Nema neparni broevi vo ovoj tuple")

parni_broevi((2,6,8,10))


def my_func1 (x):
    print("This value is part of the function " + x)

my_func1("Five")
y = "Six"
print("This parameter is not in the function " + y)

# da se napravi funkcija koja ke prima lista so ovosja, i ke gi isprinta so ciklus


def funkcija(list):
    for a in list:
        print(a)


funkcija(["Orange", "Lemon", "Apple"])


# da se najde faktoriel na daden broj

# factorel (5) = 5*(4)*(3)*(2)*1
# factoriel (3) = 3*2*1 = 6
# factoriel(0) = 1

"""Factoriel rekurzivna funkcija"""
def factoriel(num):
    if num == 1:
        return 1
    elif num < 1:
        print("NA")
    else:
        return num * factoriel(num-1)

# num*factoriel(num-1) = 5*4*3*2*1

print(factoriel(5))


"""За дадената листа да се најде вредноста 20 во листата и да се замени со 200.  list1 = [5, 10, 15, 20, 25, 50, 20]"""
def dvaeset(list):
    for i in list:
        if i == 20:
            print(200)

dvaeset([5, 10, 15, 20, 25, 50, 20])

"""Ova e funkcija koja go bara brojot 20 i go zamenuva so 200"""

def funkcija(lista):
    for neshto in lista:
        if neshto == 20:
            lista.remove(neshto)
            lista.append(200)
    return lista

def no_def_func():
    pass

list1 = [5, 10, 15, 20, 25, 50, 20]


def funkcija1(lista):
    for neshto in lista:
        if neshto == 20:
            a = list1.index(neshto)
            list1[a] = 200
            print(lista)
funkcija(list1)


print(funkcija([5, 10, 15, 20, 25, 50, 20]))











































