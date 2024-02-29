from components.RegistersPerson import RegistersPerson
from components.SearchesPerson import SearchesPerson
from components.RequestsId import RequestsId
from components.PrintsList import PrintsList
from components.RequestsModification import RequestsModification
from components.DeletesPerson import DeletesPerson

def Menu():
    
    peopleList = [["João Silva", "15-05-1987", "123.456.789-09", "joao.silva@email.com"],
  ["Maria Oliveira", "22-09-1990", "987.654.321-00", "maria.oliveira@email.com"],
  ["Carlos Pereira", "10-12-1985", "345.678.901-23", "carlos.pereira@email.com"],]
    
    while True:
        print("""\nEnter the number for one of the options below:
1. Create a record
2. Query a record by ID
3. List the records
4. Modify a record
5. Delete a record
6. Exit""")
        
        selectedOption = input("Option: ")
        
        if selectedOption == "1":
            print(f"Option {selectedOption} selected")
            
            peopleList.append(RegistersPerson())
            
        elif selectedOption == "2":
            print(f"Option {selectedOption} selected")
            
            SearchesPerson(RequestsId(), peopleList)
            
        elif selectedOption == "3":
            print(f"Option {selectedOption} selected")
            
            PrintsList(peopleList)
            
        elif selectedOption == "4":
            print(f"Option {selectedOption} selected")
            
            peopleList = RequestsModification(peopleList)
            
        elif selectedOption == "5":
            print(f"Option {selectedOption} selected")
            
            id = RequestsId()
            peopleList = DeletesPerson(id, peopleList)
            
        elif selectedOption == "6":
            print(f"Option {selectedOption} selected")
            print("Exiting...")
            break
        else:
            print("No matching option found. Please enter a valid number.")