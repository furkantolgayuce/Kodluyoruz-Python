
## Aşağıdaki iç içe döngüyü tek satırda yazma.
liste = []
for i in range(2,10):
    for j in range (1,10):
            liste.append(i*j)
print(liste)


# İç içe döngüleri kullanırken yukarıdan başlayarak yan yana yazılır. en içerideki en başa yazılır!
liste2 = [(i*j) for i in range(2,10) for j in range(1,10)]
print(liste2)

if liste == liste2:
    print("Listeler Aynı")
