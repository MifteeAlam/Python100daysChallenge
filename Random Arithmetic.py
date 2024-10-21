A=15
B=12
C=14
sum_result =A**(B+C)

print("The result is :",sum_result)


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # It's a leap year
            else:
                return False  # Not a leap year
        else:
            return True  # It's a leap year
    else:
        return False  # Not a leap year

# Example usage
year = 1997
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")