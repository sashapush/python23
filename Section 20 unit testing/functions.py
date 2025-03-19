from typing import Union

def divide(dividend: Union[int,float], divisor: Union[int,float]):
    if divisor==0:
        raise ValueError("Don't you dare divide by 0")
    return dividend / divisor

# try:
#     print(divide(15, 3))
#     print(divide(15, -3))
#     print(divide(0, 5))
# except Exception as e:
#     print(f"Error: {e}")