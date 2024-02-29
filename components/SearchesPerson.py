def SearchesPerson(id, peopleList):
    if  0 <= id <= len(peopleList):
        print(f"Person ID {id}: {peopleList[id]}\n")
    else:
        print(f"No person could be found with ID {id}\n")