

import matplotlib.pyplot as plt
import numpy as np

# 0'lardan oluşan 20x20 matris çizelim.
siyahbeyaz=np.zeros((20,20))

plt.figure()
plt.subplot(1,3,1)
plt.imshow(siyahbeyaz, 'gray', interpolation='none')

plt.subplot(1,3,2)

# siyahbeyaz'a eşitle
siyahbeyaz_cerceveli=siyahbeyaz

# Satırları siyah bırakıp içerisini beyaz yapmak için
# satır ve sütunlarda 2'den başlayıp 18 e kadar 1'e eşitliyoruz.
siyahbeyaz_cerceveli[2:18,2:18] = 1
plt.imshow(siyahbeyaz_cerceveli, 'gray', interpolation='none')


plt.subplot(1,3,3)
siyahbeyaz_cerceveli_kosegen=siyahbeyaz_cerceveli

# Köşegen çizdiriyoruz.
siyahbeyaz_cerceveli_kosegen[2:18,2:18]= np.where(np.eye(16) == 1,0,1)
plt.imshow(siyahbeyaz_cerceveli_kosegen, 'gray', interpolation='none')
