from components.ValidatesCPF import ValidatesCPF
from components.FormatCPF import FormatCPF


def RequestsCPF():
    while True:
        try:
            cpf = input("Please, enter only the 11 CPF numbers: ")
            print("\n")
            
            if ValidatesCPF(cpf):
                return FormatCPF(cpf)
            else:
                print("The CPF entered is not valid. Please enter another.")
            
        except ValueError:
            print("Please, enter a CPF composed of 11 numbers.")