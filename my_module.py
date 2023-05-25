import math

def calculate_square_footage(house):
    length = house.get("length", 0)
    width = house.get("width", 0)
    return length * width

def calculate_circumference(radius):
    return 2 * math.pi * radius