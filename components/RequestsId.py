def RequestsId():
    while True:
        try:
            id = int(input("Please, enter the person's ID: "))
            return id
        except ValueError:
            print("Invalid number. Please, enter a valid ID.")