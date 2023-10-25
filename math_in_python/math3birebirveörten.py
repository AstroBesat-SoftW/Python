def f(x):
    return x**2

def g(x):
    return 3*x+2   # fonksiyon tanımlanıyor

def kontrol_et(f):
    birebir = True
    orten = True

    # Birebir kontrol kısmi
    for x1 in range(-100, 101):
        for x2 in range(-100, 101):
            if x1 != x2 and f(x1) == f(x2):
                birebir = False
                break

    # Örten kontrol kismi
    for y in range(-100, 101):
        x_values = []
        for x in range(-100, 101):
            if f(x) == y:
                x_values.append(x)
        if len(x_values) > 1:
            orten = False
            break

    if birebir and orten:
        print("Verilen fonksiyon hem birebir hem de örten bir fonksiyondur.")
    elif birebir:
        print("Verilen fonksiyon birebir bir fonksiyondur.")
    elif orten:
        print("Verilen fonksiyon örten bir fonksiyondur.")
    else:
        print("Verilen fonksiyon ne birebir ne de örten bir fonksiyondur.")

kontrol_et(g) # burada istersek f yi çağırabiliriz yani f(x) ama ben g(x) yaptım
