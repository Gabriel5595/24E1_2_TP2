def RequestsName():
    while True:
        name = input("Please enter your name: ")
        surname = input("Please enter your surname: ")
        if name.isalpha() and surname.isalpha():
            fullName = name.title() + " " + surname.title()
            print(f"The name entered was {fullName}")
            return fullName
        else:
            print("Please, enter a valid name.")