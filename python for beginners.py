import math
import time
import random
import os
import shutil
from abc import ABC, abstractmethod

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
    name = str(input("What's your name?")).capitalize()

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
print(gaming.pop(0))
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
try:
    numerator = int(input("Enter a dividend: "))
    denominator = int(input("Enter a divisor: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("you can not divide by 0")
except ValueError as e:
    print(e)
    print("you have to divide by a number.")
except Exception as e:
    print(e)
    print("something went wrong.")
else:
    print(result)

# detect a file

path = "E:\\Git\\Python-for-beginners\\demo_file_detection.txt"
if os.path.exists(path):
    print("file exists")
else:
    print("file doesn't exist.")

# read a file
try:
    with open("demo_file_detection.txt") as file:
        print(file.read())
        print(file.closed)
    print(file.closed)
except FileNotFoundError as e:
    print(e)
    print("file not found")

# write a file

new_text = "good morning, darling!\n did you sleep well?\n want some coffee?"
try:
    with open("demo_file_detection.txt", "w") as file:
        file.write(new_text)
except FileNotFoundError as e:
    print(e)
    print("file doesn't exist.")

# copy a file
shutil.copyfile("demo_file_detection.txt", "copy.txt")
# shutil.copy()
# shutil.copy2()

# move a file

# delete a file
demo_path = "copy.txt"
os.remove(demo_path)  # delete a file
# os.rmdir(demo_path) # delete a file or empty folder
# shutil.rmtree(demo_path) # delete files or folders

# modules
help("modules")

# rock paper scissor game

user_won = 0
computer_won = 0
games_played = 0


def rps():
    global user_won, computer_won, games_played
    kid_game = ["rock", "paper", "scissor"]
    computer = random.choice(kid_game)
    print("Your computer wants to play a rock paper scissor game with you.\nMake your move!!!!")

    user = None
    while user not in kid_game:
        user = str(input("Your choice: ")).lower()
    print("Computer chose:", computer)

    if user == computer:
        print("it's a draw.")
    elif kid_game.index(user) == (kid_game.index(computer) + 1) % 3:
        print("You win!")
        user_won += 1
    else:
        print("You lost. Haha!")
        computer_won += 1

    games_played += 1


rps()
choice = ["yes", "no"]


def play_again():
    print("Hey", name, "do you want to play the game again?(yes/no)")
    my_choice = ""
    while my_choice not in choice:
        my_choice = str(input("Your choice: ")).lower()
    if my_choice == "yes":
        rps()
        play_again()
    else:
        print("You won:", user_won, "times\nComputer won:", computer_won,
              "times\nGames played:", games_played,
              "times\nHopefully you had fun playing the game. Tata!")


play_again()

# more concise rock paper scissor game by perplexity.ai
'''OPTIONS = ["rock", "paper", "scissor"]

def get_user_choice():
    user_choice = None
    while user_choice not in OPTIONS:
        user_choice = str(input("Your choice: ")).lower()
    return user_choice

def get_computer_choice():
    return random.choice(OPTIONS)

def play_round(user_won, computer_won):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw.")
    elif OPTIONS.index(user_choice) == (OPTIONS.index(computer_choice) + 1) % 3:
        print("You win!")
        user_won += 1
    else:
        print("You lost. Haha!")
        computer_won += 1

    return user_won, computer_won

def play_game():
    user_won = 0
    computer_won = 0
    print("Your computer wants to play a rock paper scissor game with you.\nMake your move!!!!")

    for i in range(10):
        user_won, computer_won = play_round(user_won, computer_won)

    print("You won:", user_won, "times\n",
          "Computer won:", computer_won, "times",
          "\nHopefully you had fun playing the game. Tata!")

def play_again():
    choice = None
    while choice not in ["yes", "no"]:
        choice = str(input("Hey, do you want to play the game again? (yes/no)")).lower()

    if choice == "yes":
        play_game()
        play_again()
    else:
        print("Thanks for playing!")

play_game()
play_again()'''

# quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


# object-oriented programming oop

class Computer:
    computer_age = 2  # class variable

    def __init__(self, monitor, graphics, processor, ram, pc_user):
        self.monitor = monitor  # instance variable
        self.graphics = graphics
        self.processor = processor
        self.ram = ram
        self.pc_user = pc_user

    def play_game(self):
        print("you are playing game on", self.pc_user, "'s computer")

    def editing(self):
        print("you are editing on", self.pc_user, "'s computer")

    def configuration(self):
        print("the pc's configuration is:", self.monitor, self.graphics, self.processor, self.ram)

    # from computer(file name) import Computer


computer = Computer("phillips", 'AMD Vega 11 pro', "Ryzen 5 3400G", "8 gb", "Mahdi")
computer.play_game()
computer.editing()
computer.configuration()
print("computer age:", computer.computer_age, "years")
computer.computer_age = 5
print("computer age:", Computer.computer_age, "years")
Computer.computer_age = 6
print("computer age:", Computer.computer_age, "years")


# inheritance
class Government:
    country = "Bangladesh"
    name = "Republic of Bangladesh"
    system = "flawed democracy"

    def __init__(self):
        print("governments are for the people, by the people, of the people. But the people are retarded.")

    def law(self):
        print("everyone must follow!")

    def people(self):
        print("government works for the people")


class PrimeMinister(Government):
    name = "Sheikh Hasina"

    def __init__(self):
        super().__init__()
        print(
            "the prime minister is appointed by the President based upon the result \nof the electorates choice in parliamentary general election held by the Election Commission.")


class President(Government):
    name = "Mohammed Shahabuddin"

    def __init__(self):
        super().__init__()
        print(
            " President is elected by an indirect election by \nthe members of parliament as per Article 48 of the Constitution.")


class MembersOfParliament(Government):
    def __init__(self):
        super().__init__()
        print("300 Members are elected by direct polls in their respective constituencies Whoever wins the most votes.")

    def location(self):
        print("parliament")


print(Government.name)
print(PrimeMinister.name)

bd2 = Government()
bd = MembersOfParliament()
bd.location()
bd.law()


# multilevel inheritance

class Human:
    pass


class Body(Human):
    pass


class Hand(Body):
    pass


class Fingers(Hand):
    pass


# multiple inheritance

class BlackPieces:
    pass


class WhitePieces:
    pass


class Chess(BlackPieces, WhitePieces):
    pass


# method overriding

# method chaining

class Morning:

    def wake(self):
        print("wake up")
        return self

    def fresh_up(self):
        print("fresh up")
        return self

    def eat(self):
        print("have breakfast")
        return self

    def greet(self):
        print("kiss wife")
        return self

    def work(self):
        print("go to work")
        return self


def methodchaining():
    morning = Morning()
    (morning.wake(). \
     fresh_up(). \
     eat(). \
     greet().work())


# super function check government class

# abstract classes
# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

# vehicle.stop()
car.stop()
motorcycle.stop()


# objects as arguments

class Car:
    color = None


class Motorcycle:
    color = None


def change_color(vehicle, color):
    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


# duck typing

# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)

# walrus operator

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)


# functions to variables

def hello():
    print("Hello")


hi = hello
hi()


# say = print
# say("Whoa! I can't believe this works! :O")


# higher order functions

#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ---- 1. accepts a function as an argument ----
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)

# ----------- 2. returns a function ------------
# def divisor(x):
# def dividend(y):
# return y / x
# return dividend


# divide = divisor(2)
# print(divide(10))

# lamda
# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda g: g * 2
print(double(1))

multiply = lambda g, h: g * h
print(multiply(1, 2))

add = lambda g, h, j: g + h + j
print(add(1, 2, 3))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Bro", "Code"))
# sort

# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

grade = lambda grades: grades[1]
# students.sort(key=age)                     # sorts current list
sorted_students = sorted(students, key=grade)  # sorts and creates a new list

for i in sorted_students:
    print(i)

# map

# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

# filter


# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)


# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)

# reduce()

# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y,: x + y, letters)
print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y,factorial)
# print(result)

# list comprehension

# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []  # create an empty list
for i in range(1, 11):  # create a for loop
    squares.append(i * i)  # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1, 11)]
print(squares)

# --------------------------------------------------------------
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
# passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)

# dictionary comprehension

# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# -------------------------------------------------------------------------
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------------------------
# def check_temp(value):
# if value >= 70:
# return "HOT"
# elif 69 >= value >= 40:
# return "WARM"
# else:
# return "COLD"


# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

# zip function

# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021", "1/2/2021", "1/3/2021"]

# --------------------------------------
users = list(zip(usernames, passwords))

for i in users:
    print(i)

# --------------------------------------
users = dict(zip(usernames, passwords))

for key, value in users.items():
    print(key + " : " + value)

# --------------------------------------
users = zip(usernames, passwords, login_dates)

for i in users:
    print(i)


# if __name__=main

# ***********************************
# if _name_ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is _name_
#  Python will assign the _name_ variable a value of '__main__' if it's
#  the initial module being run

def main():
    print("Hello!")


if __name__ == '__main__':
    main()

# ***********************************

# time module

# ***************************************************************************
print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())  # return current seconds since epoch
print(time.ctime(time.time()))  # will get current time

# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# thread

# ******************************************************
# Python threading tutorial
# ******************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# demon thread

# Python daemon threads
# ************************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())

answer = input("Do you wish to exit?")

# ************************************************************

# multiprocessing

# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")


#if _name_ == '__main__':
 #   main()

# *********************************
