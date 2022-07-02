# print all number from 1 to 10

# for x in range(1, 101):
#     for y in range(1, 11):
#         if x * y % 2 == 0:
#             print(x * y)

#     print("moving on to next x value")

# print("done")

# names = ["bran", "ana", "joe", "nate"]

# names is an iratable. Can get indiviual items. every item in names Im going to refer to as name and do something with it inside this for loop. name is for loop is a word for me to make sense if what is in the names list(actual name). Change name to x and will print the same

# interpoltion
# for name in names:
#     print(f"a name from the list is {name}")

# Functions

# def function_name():
#     print("hey")


# function_name()

# def reverse_string(string):

#     output = ""

#     for char in string:
#         output = char + output

#     return output


# print(reverse_string("hello"))

from random import randint
# dice rolling function
# 3d6, 1d20, 2d4 - (number of dice) - d - (sides of the dice)
# 4,6,8,10,12,20
# 3d6 + 2 (modifier)


def roll_dice(number, sides, modifier):

    result = 0

    for x in range(0, number):
        result += randint(1, sides)

    result += modifier

    return result


print(roll_dice(1, 6, 0))
