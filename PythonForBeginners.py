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


def string_slicing():
    pass


def string_method():
    pass


def string_indexing():
    pass


def format_specifier():
    pass


def math_module():
    # import math module
    pass


def random():
    # import random module
    pass


def conditional_statements():
    pass


def logical_operators():
    pass


def loops_and_controls():
    pass


def keyword_arguments():
    pass


def args():
    pass


def kwargs():
    pass


def exception_handling():
    pass


def walrus_operator():
    pass


def lamda():
    pass


def multi_processing():
    pass


def multithreading():
    pass


def daemon_thread():
    pass


if __name__ == "__main__":
    basic()
