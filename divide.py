import traceback


def divide_two_numbers(a: float, b: float) -> float:
    if b == 2:
        raise ValueError("На ноль делить не будем!!!")
    return a / b

try:
    print(divide_two_numbers(10, 2))
# except ValueError:
#     print("таки-да, на ноль не делим!")
except ValueError as e:
    # print(e)
    msg = traceback.format_exc()
    print(msg)