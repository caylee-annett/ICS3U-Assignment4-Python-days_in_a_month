#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program prints the number of days in a month, including leap years


def main():
    # This function tells the user how many days are in a month

    # Input
    print("This program tells you how many days are in the month "
          "that you enter.")
    month = input("Enter the name of a month: ")
    print("")

    # Process & Output
    if month == "january" or month == "January":
        print("There are 31 days in January.")
    elif month == "february" or month == "February":
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
    elif month == "march" or month == "March":
        print("There are 31 days in March.")
    elif month == "april" or month == "April":
        print("There are 30 days in April.")
    elif month == "may" or month == "May":
        print("There are 31 days in May.")
    elif month == "june" or month == "June":
        print("There are 30 days in June.")
    elif month == "july" or month == "July":
        print("There are 31 days in July.")
    elif month == "august" or month == "August":
        print("There are 31 days in August.")
    elif month == "september" or month == "September":
        print("There are 30 days in September.")
    elif month == "october" or month == "October":
        print("There are 31 days in October.")
    elif month == "november" or month == "November":
        print("There are 30 days in November.")
    elif month == "december" or month == "December":
        print("There are 31 days in December.")
    else:
        print("{} is not a valid input.".format(month))
    print("\nDone.")


if __name__ == "__main__":
    main()
