layer = int(input("Kat Sayısı: "))

c = '*'

for i in range(layer):
    print((c*i).rjust(layer-1)+c+(c*i).ljust(layer-1))
