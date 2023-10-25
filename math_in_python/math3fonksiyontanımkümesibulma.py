from sympy import symbols, Interval, sqrt, solve

# Sembolu tanıyıtorum
x = symbols('x')

# Math3 f(x) ve g(x)'i tanımlıyorum
fx = sqrt(x)
gx = sqrt(x - 1)   #sqrt köklü ifadeler için kullnulur
#                   mesela sqrt(4) dersek 2 olarak çıkar.
#                   burada yapılan şu: hocanın sorduğunu tanımlıyorum
#                   mesela soruda f(x)=kök için de ve g(x)= kök içinde x-1 demiş.

# f(x) ve g(x) fonksiyonlarının tanım kümesini hesaplayın
tanim_fx = Interval(0, float('inf'))
tanim_gx = Interval(1, float('inf'))

# ortak tanım kümesinin hesaplanmasi
ortaktanim = tanim_fx.intersection(tanim_gx)

# Sonucu yazdırın
print("f(x) ve g(x) fonksiyonlarının ortak tanım kümesi:", ortaktanim)
