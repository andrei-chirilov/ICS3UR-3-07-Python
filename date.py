#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program determines if you can date my grandaughter


def main():
    # this functions use the compound boolean expression

    # input
    age = int(input("Enter your age: "))
    print("")

    # process & output
    if age >= 25 and age <= 40:
        print("You may date my granddaughter.")
    else:
        print("You cannot date my granddaughter.")


if __name__ == "__main__":
    main()
