import math
from datetime import datetime
import calendar

def main():
    # Current date and time
    now = datetime.now()
    print("Current date and time:", now)
    print("Year:", now.year)
    print("Month:", now.month)
    print("Day:", now.day)
    print("Hour:", now.hour)
    print("Minute:", now.minute)
    print("Second:", now.second)

    # Create a specific date and time
    specific_date = datetime(2023, 7, 5, 12, 30, 45)
    print("\nSpecific date and time:", specific_date)

    # Format the current date and time
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("\nFormatted date and time:", formatted_date)

    # Calculate the difference between two dates
    date1 = datetime(2023, 7, 1)
    date2 = datetime(2024, 7, 1)
    difference = date2 - date1
    print("\nDifference in days between 2023-07-01 and 2024-07-01:", difference.days)

    # Perform some basic mathematical operations
    print("\nSquare root of 16:", math.sqrt(16))
    print("Factorial of 5:", math.factorial(5))
    print("Cosine of 0 radians:", math.cos(0))

    # Math constants
    print("\nValue of pi:", math.pi)
    print("Value of e:", math.e)

    # Logarithms
    print("\nNatural logarithm of 10:", math.log(10))
    print("Base-10 logarithm of 10:", math.log10(10))

    # Trigonometric functions
    angle = math.radians(45)  # Convert degrees to radians
    print("\nSine of 45 degrees:", math.sin(angle))
    print("Cosine of 45 degrees:", math.cos(angle))
    print("Tangent of 45 degrees:", math.tan(angle))

    # Calendar functionalities
    year = now.year
    month = now.month

    # Print the calendar for the current month
    print("\nCalendar for the current month:")
    print(calendar.month(year, month))

    # Check if the current year is a leap year
    is_leap = calendar.isleap(year)
    print(f"Is {year} a leap year?:", is_leap)

    # Print the number of leap years between two years
    start_year = 2000
    end_year = 2023
    leap_days = calendar.leapdays(start_year, end_year)
    print(f"Number of leap years between {start_year} and {end_year}:", leap_days)

if __name__ == "__main__":
    main()
