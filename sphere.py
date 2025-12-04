# inspiration code for Python Unit Testing Project

import math

def surfaceArea():
    pass

def volume(rad):
    volume = (4/3) * math.pi * rad**3
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\n The volume of a sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
