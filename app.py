from timeit import timeit

code1 = """
def calculate_xfactor(age):

    if age <= 0:
        raise ValueError("age cannot be 0 of less")
    return 10 / age


try:
    calculate_xfactor(-2)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):

    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
  pass
"""
print("first code=", timeit(code1, number=100000))
print("second code=", timeit(code2, number=100000))
