from components.ValidatesLeapYear import ValidatesLeapYear

def ValidatesDate(day, month, year):
    if month < 1 or month > 12:
        return False

    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ValidatesLeapYear(year):
        daysInMonth[2] = 29

    return 1 <= day <= daysInMonth[month]