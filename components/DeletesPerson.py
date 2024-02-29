def DeletesPerson(id, peopleList):
    try:
        deletedPerson = peopleList.pop(id)
        print(f"Deleted person: {deletedPerson}")
        return peopleList
    except IndexError:
        print(f"Person with ID {id} could not be found. Please enter a valid ID.")