#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program prints integers from 1000 to 2000
# Outputting five integers per line, separated by a space


def main():
    # Input: set start and end numbers
    start = 1000
    end = 2000

    # Process + Output: loop through numbers and print them
    for number in range(start, end + 1):
        print(f"{number} ", end="")  # Print number and stay on same line
        if (number - 999) % 5 == 0:
            print("")  # Print newline after every 5 numbers


if __name__ == "__main__":
    main()
