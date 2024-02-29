from components.ValidatesDate import ValidatesDate
from components.FormatDate import FormatDate

def RequestsDateOfBirth():
    while True:
        try:
            day = int(input("Enter your day of birth: "))
            month = int(input("Enter your month of birth: "))
            year = int(input("Enter your year of birth: "))
        
            if ValidatesDate(day, month, year):
                return FormatDate(day, month, year)
            else:
                print("Invalid date. Please, enter a valid date.")

        except ValueError:
            print("Please, type integer to represent day, month and year.")