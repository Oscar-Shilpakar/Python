# Write a Python program to calculate the area and circumference of a circle with a given radius from terminal.

pi=22/7
radius=float(input("Enter radius of circle: "))
area=(pi)*radius*radius
circumference=2*(pi)*radius
print(f"Area of the circle is {area}")
print(f"Circumference of the circle is {circumference}")