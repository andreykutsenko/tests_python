import sys


if len(sys.argv) < 2:
    print("Передайте длину стороны квадрата!")
    exit()

square_side = sys.argv[1]
if not square_side.isnumeric():
    print("Передайте число в качестве стороны квадрата!")
    exit()

perimeter = int(square_side) * 4
print(perimeter)