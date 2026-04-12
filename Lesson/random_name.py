import random

isimler = ["isim_1", "isim_2", "isim_3", "isim_4", "isim_5", "isim_6", "isim_7"]

random.shuffle(isimler)

print("--- Görev Dağılım Listesi ---")
print(f"Madde 2: {isimler[0]}")
print(f"Madde 3: {isimler[1]}")
print(f"Madde 4: {isimler[2]}")
print(f"Madde 5: {isimler[3]}")
print(f"Madde 6: {isimler[4]} ve {isimler[5]}")
print(f"Madde 7: {isimler[6]}")
