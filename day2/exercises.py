# Calculate age from year of birth, assuming current year is 2020
def calc_age(yob):
    print(f"Your age is {2020 - yob}.")

calc_age(1993)

# Calculate age from year of birth provided as input
def ask_yob():
    yob = input("Please enter your year of birth: ")
    print(f"Your age is {2020 - int(yob)}.")

ask_yob()

''' 
def ask_yob():
    print(
        f"Your age is 
        {2020 - int(input("Please enter your year of birth: "))}."
    )

ask_yob()
'''

# Calculate age using date of birth (year, month, day)
# relative to current date
def ask_dob():
    # Add modules
    import time
    import datetime
    from datetime import date
    import math
    
    # Ask for date of birth (year, month and day separately)
    print("Please enter your date of birth:")
    y = int(input("Year (YYYY): "))
    m = int(input("Month  (MM): "))
    d = int(input("Day    (DD): "))
    # Elapsed date corresponding to date of birth
    dob = date(y, m, d)
    
    # Get current date
    curdate = datetime.datetime.now()
    # Elapsed date
    today = date(int(curdate.year), int(curdate.month), int(curdate.day))

    # Compute age, i.e. difference in days between 
    # today and dob, divided by 365.25
    age = math.floor((today-dob).days/365.25)

    print(f"Your age is {age}.")

ask_dob()