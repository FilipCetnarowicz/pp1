def f(name):
    acronym=""
    newName=name.split()
    print(f"name as a list of words: {newName}")
    for firstWords in newName:
        acronym+=firstWords[0]
    return acronym



name=str(input("type in what you want to make acronym of: "))
print(f(name))


