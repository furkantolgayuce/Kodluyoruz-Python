# Ödev - 2

notebook = list()

name, lastname, birthyear = input("Adınız: "), input("Soyadınız: "), int(input("Doğum Yılınız: "))

notebook.append([name,lastname,birthyear])

print("##########")

for i in notebook[0]:
    print(i)
