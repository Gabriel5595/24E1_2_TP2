from components.RequestsId import RequestsId

def SelectsModification(peopleList):
    while True:
        try:
            id = RequestsId()
            
            print("""Please, enter the number correspondent to the field that should be modified:
1. Name
2. Date of Birth
3. CPF
4. E-mail\n""")
            field = int(input())
            if 0 < field < 5:
                return id, field-1
            else:
                print("Please, enter a valid option.")
        except ValueError:
            print("Please, enter a valid option.")