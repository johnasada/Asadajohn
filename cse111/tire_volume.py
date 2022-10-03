# import the math module so i can use math.pi.
from ast import If
from cmath import pi
import math
from datetime import datetime
import os
from tkinter import Y
from tkinter.messagebox import YES
from turtle import width
pi= math.pi
# Previous Program
# Print a description of this program for the user to use.
print("This program computes and outputs")
print("the volume of space inside that tire.")
print()
# Get the width, ratio and diameter from the user.
Width=int(input("Enter the width of the tire in mm: "))
Ratio=int(input("Enter the aspect ratio of the tire: "))
Diameter=int(input("Enter the diameter of the wheel in inches: "))
Buy=(input("Do you want to buy the tire: "))
Phone_Number=("+2348111665753")
print()
# Compute the volume of space inside the tire.
volume=(pi * (pow(Width,2) * Ratio * (Width * Ratio + 2540 * Diameter)))/(10000000000)

# Print the volume of space inside the tire for the user to see, rounded to 2 digit place.
print("The approximate volume is: {:.2f}".format(volume) + " liters")
# End of previous program.
print()
current_date_and_time= datetime.now(tz=None)
print(current_date_and_time)
with open("volumes.txt", mode='at') as tire_volume:
    #print("{:.2f}".format(volume), file=tire_volume)
    print(f"{current_date_and_time}, {Width}, {Ratio}, {Diameter}, {'{:.2f}'.format(volume)}", file=tire_volume) 
with open("volumes.txt", mode='at') as tire_volume:
    print(f"{Phone_Number}", file=tire_volume)