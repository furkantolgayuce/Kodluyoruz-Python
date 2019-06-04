name = input("Name: ")

lastname = input("Lastname: ")

while True:
    birthyear = input("Birthyear (number required 4-digit): ")
    if birthyear.isdigit() and len(birthyear.strip()) == 4:
        birthyear = int(birthyear)
        break
while True:
    tcnu = input("TC Number (number required 11-digit): ")
    if (tcnu.isdigit() and len(tcnu.strip()) == 11):
        tcnu = int(tcnu)
        break
    if tcnu == "":
        break
        

dictionary = {"name" : name,
              "lastname" : lastname,
              "birthyear" : birthyear,
              "tcnu" : tcnu}

for i in dictionary:
    print(i, ": ", dictionary[i])
