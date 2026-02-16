# faktoriyel fonksiyon hali

a = int(input())

def fak(x):
    m = 1
    for i in range(x+1):
        m *= i
    return x

print(fak(a))

# faktoriyel sonuc ekana döndürür