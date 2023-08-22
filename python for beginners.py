import math
import time
import random

# # output and data type
print('single quotation')
print("double quotation")
print("str" + "ing")

variable = "value unoriginal "
variable1 = False
variable2 = 69
variable3 = 69.69
variable4, variable5, variable6 = "value4", "value5", 59.59
variable7 = variable8 = variable9 = 99

print(type(variable), type(variable1), type(variable2), type(variable3), type(variable4), type(variable5),
      type(variable6), type(variable7), type(variable8), type(variable9))
print(variable, variable1, variable2, variable3, variable4, variable5, variable6, variable7, variable8, variable9)
print(str(variable), str(variable1), str(variable2), str(variable3), str(variable4), str(variable5), str(variable6),
      str(variable7), str(variable8), str(variable9))
print(str(type(variable)), str(type(variable1)), str(type(variable2)), str(type(variable3)), str(type(variable4)),
      str(type(variable5)), str(type(variable6)), str(type(variable7)), str(type(variable8)), str(type(variable9)))

print(len(variable))
print(variable.capitalize())
print(variable.replace(" ", "s"))
# print(variable.) //library

# # typecasting
x = 1
y = 2.34
y = int(y + 1)
z = "hole"
print("my" + z + "is" + str(y) + "cm")

# # math(import math)

a = -100
b = 200.555

print(abs(a))
print(round(b))
print(math.sqrt(b))
# print(math.) //library

# # user input
temperature = float(input("What's the temperature?"))
temperature_scale = str(input("What's the unit of measurement?"))
humidity = int(input("What's the humidity"))
print("The temperature is " + str(temperature) + " degree " + temperature_scale + ". " + "Humidity is " +
      str(humidity) + "%.")

# # string slicing
utility = "art notebook"
category = utility[0:3]
alternate_category = utility[:3]
utility_type = utility[4:12]
alternate_utility_type = utility[4:]
randoms = utility[1:12:2]
reversed_utility = utility[::-1]
sliced = slice(4, -4)
print(utility, category, alternate_category, utility_type, alternate_utility_type, randoms, reversed_utility,
      utility[sliced])

# # if statements
if temperature_scale == "celsius":
    if temperature >= 50:
        print("temperature is too high!")
    else:
        print("you are alright.")

elif temperature_scale == "fahrenheit":
    if temperature >= 120:
        print("temperature is too high!")
    else:
        print('you are alright.')
# logical operators (and,or,not)

# while loop
name = ""
# name = None
while name == "" or len(name) < 5:
    name = str(input("What's your name?"))

# import time
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
print("race starts!")

# nested loops
for i in range(5, 0, -1):
    for k in range(5 - i):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")

    print()

# break continue pass
for i in range(5):
    print(i, end=" ")
    if i == 3:
        break
print()
for j in range(10):
    print(j, end=" ")
    if j == 3:
        continue
    print()

print()

# lists
gaming = ["valorant", "pubg", "chess", "cod"]
print(gaming)
gaming.append("coc")
print(gaming)
# list_variable_name. //library

# 2d lists
brain = ["think", "life", "mushy"]
heart = ["beat", "pmp blood", "fragile"]
leg = ["walk", "run", "mobility", "skinny"]
human = [brain, heart, leg]
print(human)

# tuples

user = ("mahdi", 23, "university")
print(user.count("mahdi"))
print(user.index("university"))
for i in user:
    print(i)

if "university" in user:
    print("studies in uni.")

# sets
games = {"valorant", "pubg", "chess", "cod", "cod", "cod"}
games.remove("pubg")
games.add("cr")
# games. //library
for i in games:
    print(i)

# dictionaries
fruits = {"mango": "tasty",
          "orange": "sour",
          "chocolate": "dark"}

fruits.update({"apple": "juicy"})
print(fruits)
# print(fruits.pop("china"))
fruits.clear()
print(fruits)

# indexing/index operator

vct2023 = "valorant champion tournament"
common_noun = vct2023[18:].capitalize()
proper_noun = vct2023[:8].capitalize()
abstract_noun = vct2023[9:17].capitalize()

print(abstract_noun + "s ", common_noun + ",", proper_noun)


# functions

def getfresh():
    print("wake up and get out of bed.")
    time.sleep(1)
    print("go to bathroom.")
    time.sleep(1)
    print("wash your face then brush your teeth.")
    time.sleep(1)
    print("get out!")


getfresh()


# functions with parameters and return type

def summation(first_number, second_number):
    total = first_number + second_number
    print(total)
    return total


summation(1, 2)
print(summation(5, 5), "yahoo!")


# keyword arguments

def my_name(first, middle, last):
    print(first, middle, last)


my_name(middle="Mahdi", last="Hossain", first="Md.")


# nested functions call

# variable scope
# local global bl enclosed

# # args
def multiplication(*args):
    total = 1
    args = list(args)
    args[0] = 1
    for k in args:
        total *= k
    return total


print(multiplication(1, 2, 3))


def median(data):
    ans = 0
    for i in data:
        ans += i
    total = ans / len(data)
    return total


no_of_numbers = int(input("How many numbers do you want to find the median of?"))
numbers = []
print("Enter the", no_of_numbers, "numbers you wish to find the median of.")
for i in range(0, no_of_numbers):
    x = float(input(""))
    numbers.append(x)

print(median(numbers))


# **kwargs

def my_full_name(**kwargs):
    print("Hello", kwargs["first"], kwargs["middle"], kwargs["end"], kwargs["nickname"])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


my_full_name(first="Md.", middle="Mahdi", end="Hossain", nickname="Zawaad")
print()

# str.format

number = 1000000000
print("the formatted number is {:.3f}".format(number))  # decimal
print("the formatted number is {:,}".format(number))  # 0s separated by comma
print("the formatted number is {:b}".format(number))  # binary
print("the formatted number is {:o}".format(number))
print("the formatted number is {:X}".format(number))
# str.format library

# random library

dice = random.randint(1, 6)
one = random.random()
print(dice)
print(one)
rpc = ["rock", "paper", "scissor"]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "k", "q"]
print(random.choice(rpc))
random.shuffle(cards)

print(rpc)
print(cards)

# exception handling
