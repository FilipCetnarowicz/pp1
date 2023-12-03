person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print("dictionary:", person)

print("dictionary - name:", person["name"])

print("dictionary - hobby:", person["hobby"])

print("dictionary - surname:", person["surname"])
person["surname"]="Nowak"
print("dictionary - surname:", person["surname"])

print("dictionary - married:", person["married"])
person["married"] = not person["married"]
print("dictionary - married:", person["married"])

person["gender"]="male"
print("dictionary - gender:", person["gender"])

person["hobby"]+=["bicycle"]

person["phone"]["work"]="123"
print("dictionary - phone:", person["phone"])

print(person)