sayi = int(input("Faktöriyel'i hesaplanacak sayıyı giriniz: "))
carp = 1

if sayi == 0:
    print("Sıfır'ın faktöriyel'i 1'dir.".format(sayi))
else:
    for i in range(1,sayi+1):
        carp*=i
    print("{} sayısının faktöriyel'i {}'dir".format(sayi,carp))
