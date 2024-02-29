from components.RequestsName import RequestsName
from components.RequestsDateOfBirth import RequestsDateOfBirth
from components.RequestsCPF import RequestsCPF
from components.RequestsEmail import RequestsEmail

def RegistersPerson():

    fullName = RequestsName()
    dateOfBirth = RequestsDateOfBirth()
    cpf = RequestsCPF()
    email = RequestsEmail()
    
    newPerson = [fullName, dateOfBirth, cpf, email]
    
    print(f"New person created: {newPerson}")
    
    return newPerson