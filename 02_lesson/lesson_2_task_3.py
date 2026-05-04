import math


def square_area(side):
    return math.ceil(side * side)


side = int(input("Введите сторону квадрата: "))

result = square_area(side)

print(f"площадь квадрата {side}*{side} = {result}")
