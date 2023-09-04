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


if __name__ == "__main__":
    basic()
