class basic:
    def __init__(self):
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
        print(variable, variable1, variable2, variable3, variable4, variable5, variable6, variable7, variable8,
              variable9)
        print(str(variable), str(variable1), str(variable2), str(variable3), str(variable4), str(variable5),
              str(variable6),
              str(variable7), str(variable8), str(variable9))
        print(str(type(variable)), str(type(variable1)), str(type(variable2)), str(type(variable3)),
              str(type(variable4)),
              str(type(variable5)), str(type(variable6)), str(type(variable7)), str(type(variable8)),
              str(type(variable9)))

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

        # # user input
        temperature = float(input("What's the temperature?"))
        temperature_scale = str(input("What's the unit of measurement?"))
        humidity = int(input("What's the humidity"))
        print("The temperature is " + str(temperature) + " degree " + temperature_scale + ". " + "Humidity is " +
              str(humidity) + "%.")


class Strings:
    # String slicing
    def string_slicing(self):
        pass

    # string method
    def string_method(self):
        pass

    # string indexing
    def string_indexing(self):
        pass

    # format specifier
    def format_specifier(self):
        pass


def math_module():
    # import math module
    pass


def random():
    # import random module
    pass


def conditional_statements_logical_operators():
    pass


def loops_and_controls():
    pass


class data_structures:
    # tuple
    def tuple(self):
        pass

    # set
    def set(self):
        pass

    # lists
    def list(self):
        pass

    # 2d lists
    def _2dlist(self):
        pass

    # dictionary
    def dictionary(self):
        pass


class arguments:
    def keyword_arguments(self):
        pass

    def args(self):
        pass

    def kwargs(self):
        pass


def exception_handling():
    pass


class file:
    # import os
    def read(self):
        pass

    def write(self):
        pass

    def copy(self):
        pass

    def move(self):
        pass

    def delete(self):
        pass


class object_oriented_programming:
    """ functions, return statement, nested function calls, class variables, inheritance,
        multilevel inheritance, multiple inheritance, method overriding, method chaining,
        super function, abstract classes, abstract methods, objects as arguments, duck typing"""

    def functions(self):
        pass

    def return_statements(self):
        pass

    def nested_function_calls(self):
        pass

    def class_variables(self):
        pass

    def inheritance(self):
        pass

    def multilevel_inheritance(self):
        pass


if __name__ == "__main__":
    basic()
