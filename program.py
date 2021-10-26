#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This program generate random numbers

import random


def table(rows, columns):
    list_d1 = []
    total_number = 0
    for loop_counter_rows in range(0, rows):
        list_d2 = []
        for loop_counter_columns in range(0, columns):
            random_number = random.randint(0, 10)
            list_d2.append(random_number)
            print("{0} ".format(random_number), end="")
            total_number = total_number + random_number
        list_d1.append(list_d2)
        print("")
    average = total_number / (rows * columns)
    return average


def main():
    # this function generate random numbers
    print("Starting ...\n")
    integer1 = input("How many row would you like: ")
    integer2 = input("How many columns would you like: ")
    print("")
    try:
        rows = int(integer1)
        columns = int(integer2)
        if rows < 1 or columns < 1:
            print("Please use numbers > 0")
        else:
            average = table(rows, columns)
            print("\nThe average of all the numbers is: {0:,.2f}".format(average))

    except Exception:
        print("Invalid input")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
