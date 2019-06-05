import os

#mevcut_dizin = os.getcwd()
mevcut_dizin = os.chdir("/home/tolga/Belgeler")


# 1
liste = os.listdir(mevcut_dizin)
print(liste)
# Boşluklara kaçış ekleyelim.
sonuc = map(lambda x: x.replace(" ", "\ "),liste)
liste = list(sonuc)


#2 
os.mkdir("pdf")
for i in liste:
    if i[-3:] == "pdf":
        os.system("mv {} ./pdf".format(i))

# 3
present, future = input("Değişecek uzantı: "), input("Olmasını istediğiniz: ")
for i in liste:
    if i[-len(present):] == present:
        os.system("mv {} {}".format(i,i[:-len(present)]+future))

# 4
path = '/home/tolga/İndirilenler'
files = os.listdir(path)
i = 1

for file in files:
    filename, file_extension = os.path.splitext(file)
    os.rename(os.path.join(path, file), os.path.join(path, filename + str(i) + file_extension))
    i = i+1
