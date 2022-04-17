#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, check if the package is acceptable


def main():
    # This function checks package's weight and volume

    # input
    weight_string = input("Enter your package's weight(kg): ")
    length_string = input("Enter your package's length(cm): ")
    width_string = input("Enter your package's width(cm): ")
    height_string = input("Enter your package's height(cm): ")

    # process & output
    print("")
    try:
        weight_integer = int(weight_string)
        length_integer = int(length_string)
        width_integer = int(width_string)
        height_integer = int(height_string)
        volume = length_integer * width_integer * height_integer
        if weight_integer <= 0 or volume <= 0:
            print("Please put in a positive integer!")
        elif weight_integer <= 27 or volume <= 10000:
            print("Your package will be accepted.")
        else:
            print("Your package is too heavy and too large!")
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
