from components.SelectsModification import SelectsModification
from components.ModifiesPerson import ModifiesPerson

def RequestsModification(peopleList):
    id, field = SelectsModification(peopleList)
    newPeopleList = ModifiesPerson(peopleList, id, field)
    
    return newPeopleList