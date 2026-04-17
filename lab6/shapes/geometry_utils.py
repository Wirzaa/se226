import math

def circle_area(radius):
    if radius <= 0:
        while(radius <= 0):
           radius = int(input("Invalid radius, try again:"))
    return (math.pi * (radius**2))

def circle_perimeter(radius):
    if radius <= 0:
        while(radius <= 0):
           radius = int(input("Invalid radius, try again:"))
    return (2 * math.pi * radius)
    
def rectangle_area(width, height):
    while(width <= 0):
        width = int(input("Invalid width input, try again: "))
    while(height <= 0):
        height = int(input("Invalid height input, try again: "))
    return width*height

def rectangle_perimeter(width, height):
    while(width <= 0):
        width = int(input("Invalid width input, try again: "))
    while(height <= 0):
        height = int(input("Invalid height input, try again: "))
    return 2*(width + height)

def triangle_area(base, height):
    while(base <= 0):
        base = int(input("Invalid base input, try again: "))
    while(height <= 0):
        height = int(input("Invalid height input, try again: "))

    return (base*height/2)
