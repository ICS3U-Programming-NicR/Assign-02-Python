#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: 30-03-2022

# Calculates the surface area and volume of different torus's


import math
import sys


def try_again_fnct():
    try_again = str(input("Would you like to try again? \n"))
    if try_again == "Y" or try_again == "y" or try_again == "yes" or try_again == "YES":
        main()
    elif try_again == "N" or try_again == "n" or try_again == "no" or try_again == "NO":
        sys.exit()


def main():
    maj_radius = int(
        input(
            "Enter the Major Radius (the distance from the center of the tube to the center of the torus) "
        )
    )
    min_radius = int(input("Enter the Minor Radius (the radius of the tube) "))
    if maj_radius > min_radius:
        print("This torus is a ring torus")
        surface_area = 4 * (math.pi**2) * min_radius * maj_radius
        volume = 2 * (math.pi**2) * (min_radius**2) * maj_radius
        print(
            "The volume is {} and the surface area is {}".format(volume, surface_area)
        )
        try_again_fnct()
    elif maj_radius == min_radius:
        print("This torus is a horn torus")
        surface_area = 4 * (math.pi**2) * min_radius * maj_radius
        volume = 2 * (math.pi**2) * (min_radius**2) * maj_radius
        print(
            "The volume is {} and the surface area is {}".format(volume, surface_area)
        )
        try_again_fnct()
    elif maj_radius:
        print("This torus is a spindle torus")
        surface_area = 4 * (math.pi**2) * (min_radius**2)
        volume = (2 / 3) * math.pi * (
            2 * (min_radius**2) + (maj_radius**2)
        ) * math.sqrt((min_radius**2) - (maj_radius**2)) + math.pi * (
            min_radius**2
        ) * maj_radius * (
            math.pi
            + 2
            * math.atan(maj_radius / math.sqrt((min_radius**2) - (maj_radius**2)))
        )
        print(
            "The volume is {:.2f} and the surface area is {:.2f}".format(
                volume, surface_area
            )
        )
        try_again_fnct()


if __name__ == "__main__":
    main()
