"""
Utility functions for date-related calculations.

This module provides:
1. A function to check whether a given year is a leap year.
2. A function to determine the number of days in a given month of a given year.
"""

# Index 0 is a placeholder so that month numbers (1–12) map directly to indices
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """
    Check whether a given year is a leap year.

    Rules for leap year:
    - The year must be divisible by 4, AND
    - If the year is divisible by 100, it must also be divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """
    Return the number of days in a specific month of a given year.

    This function:
    - Validates the month value.
    - Handles February separately for leap years.
    - Uses a predefined list for other months.

    Parameters:
    year (int): The year (used to check leap year).
    month (int): Month number (1 to 12).

    Returns:
    int or str:
        - Number of days in the month if input is valid.
        - 'Invalid Month' if the month is outside 1–12.
    """

    # Validate month range
    if not 1 <= month <= 12:
        return 'Invalid Month'

    # Special case: February in a leap year
    if month == 2 and is_leap(year):
        return 29

    # Return days from predefined list
    return month_days[month]


# Example usage
print(days_in_month(2017, 2))
