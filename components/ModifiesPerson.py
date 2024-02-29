from components.RequestsName import RequestsName
from components.RequestsDateOfBirth import RequestsDateOfBirth
from components.RequestsCPF import RequestsCPF
from components.RequestsEmail import RequestsEmail

def ModifiesPerson(peopleList, id, field):
    person = ["Name", "Day of Birth", "CPF", "E-mail"]
    
    
    print(f"The field '{person[field]}' of person ID {id} was selected for modification.")
    print(f"The actual value of this field is '{peopleList[id][field]}'")
    
    if field == 0:
        newName = RequestsName()
        peopleList[id][field] = newName
        print(f"The new person registration is: {peopleList[id]}\n")
        return peopleList
    elif field == 1:
        newDateofBirth = RequestsDateOfBirth()
        peopleList[id][field] = newDateofBirth
        print(f"The new person registration is: {peopleList[id]}\n")
        return peopleList
    elif field == 2:
        newCpf = RequestsCPF()
        peopleList[id][field] = newCpf
        print(f"The new person registration is: {peopleList[id]}\n")
        return peopleList
    else:
        newEmail = RequestsEmail()
        peopleList[id][field] = newEmail
        print(f"The new person registration is: {peopleList[id]}\n")
        return peopleList