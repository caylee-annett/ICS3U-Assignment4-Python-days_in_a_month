#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program prints the number of days in a month, including leap years


def main():
    # This function tells the user how many days are in a month

    # Input
    print("This program tells you how many days are in the month "
          "that you enter.")
    month = input("Enter the name of a month (capitalize first letter): ")
    print("")

    # Process & Output
    if month == "January" or month == "March" or month == "May" \
            or month == "July" or month == "August" or month == "October" \
            or month == "December":
        print("There are 31 days in {}.".format(month))
    elif month == "April" or month == "June" or month == "September" \
            or month == "November":
        print("There are 30 days in {}.".format(month))
    elif month == "February":
        year_string = input("Enter the year to see if it is a leap year: ")
        try:
            year_integer = int(year_string)
            if year_integer % 4 == 0:
                if year_integer % 100 == 0 and year_integer % 400 != 0:
                    print("There are 28 days in February.")
                else:
                    print("There are 29 days in February.")
            else:
                print("There are 28 days in February.")
        except Exception:
            print("{} is not a valid input.".format(year_string))
    else:
        print("{} is not a valid input.".format(month))
    print("\nDone.")


if __name__ == "__main__":
    main()
