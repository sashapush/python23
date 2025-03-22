from typing import Union


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("Don't you dare divide by 0")
    return dividend / divisor


# try:
#     print(divide(15, 3))
#     print(divide(15, -3))
#     print(divide(0, 5))
# except Exception as e:
#     print(f"Error: {e}")

def multiply(*args: Union[int, float]):  # multiply (3,5,9) etc' *args = any number
    if len(args) == 0:
        raise ValueError("At least one value to multiply must be passed")

    total = 1
    for arg in args:
        total *= arg
    return total
