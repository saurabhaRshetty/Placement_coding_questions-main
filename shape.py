#1circle
#2square
#3triangle
#4rectangle
#Enter ur choice:1
#enter radius: 10
#area of circle: 34
#enter your choice

import math

def menu():
    print("\n#1 Circle")
    print("#2 Square")
    print("#3 Triangle")
    print("#4 Rectangle")
    print("#5 Exit")

def area_circle():
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print(f"Area of circle: {area:.2f}")

def area_square():
    s = float(input("Enter side: "))
    area = s * s
    print(f"Area of square: {area:.2f}")

def area_triangle():
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print(f"Area of triangle: {area:.2f}")

def area_rectangle():
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print(f"Area of rectangle: {area:.2f}")

# Main program
while True:
    menu()
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        area_circle()
    elif ch == 2:
        area_square()
    elif ch == 3:
        area_triangle()
    elif ch == 4:
        area_rectangle()
    elif ch == 5:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
