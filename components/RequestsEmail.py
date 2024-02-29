def RequestsEmail():
    while True:
        email = input("Please, enter you e-mail: ")
        
        validation1 = "@"
        validation2 = ".com"
        
        if validation1 in email and validation2 in email:
            print(f"The email entered was {email} .\n")
            return email
        else:
            print("Please, enter a valid e-mail.")