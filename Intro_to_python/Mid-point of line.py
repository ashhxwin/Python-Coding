# Harry is trying to find the midpoint of a line segment given the coordinates of its two endpoints. Write a Python program to help Harry calculate the midpoint of the line. 
# The formula for the midpoint is Midpoint formula is [ (x1 + x2)/2 , (y1 + y2)/2 ]

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

midpoint_x = (x1 + x2) / 2
midpoint_y = (y1 + y2) / 2

print(f"{midpoint_x} {midpoint_y}")