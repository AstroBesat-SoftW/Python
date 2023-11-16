# 7th week math lesson

from sympy import symbols, diff



# x sembolunu tanımlıyoruz
x = symbols('x')

# ben bunu harici girdide alabilirim kullanıcıdan fakat istemiyorum şuan
# o yüzden önceden girilmiş girdi yapıcam (kayıtlı)
f = (x**3 -5) * (- x**2 + 3)

# Türevinini alma kısmı
turevli = diff(f, x)

# Sonucu yazdır
print("f(x) =", f ,"Girilen Denklem")
print("f'(x) =", turevli , "Türevli hali")

# burada bitirebilirdim fakat ben şunu istiyorum
# diyelim soruda f'(-1) istiyor -1 i yerine koymalıyız.

fxyerinesunuyaz = turevli.subs(x, 1)


print("f'(1) =", fxyerinesunuyaz)
