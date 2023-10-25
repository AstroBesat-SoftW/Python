from sympy import symbols, diff, solve, oo


x = symbols('x')

# f(x) fonksiyonu tanımladım
f_x = 2*x+4

# türevinin hesab
f_prime = diff(f_x, x)  # mesela bu koda göre türevi 2 olur :)

# Türevin sıfır noktalarını bulma
critical_points = solve(f_prime, x)

# İşaret değişikliklerini inceleyerek artan ve azalan aralıkları bulma
increasing_intervals = []
decreasing_intervals = []

if not critical_points:
    # Eğer türevin sıfır noktası yoksa, işlev her yerde artan veya her yerde azalan demektir.
    increasing_intervals.append("(-oo, oo) her yerde artıyor ")
    decreasing_intervals.append("(-oo, oo) her yerde azalıyor")
else:
    # Türevin sıfır noktaları varsa, bu noktaları kullanarak aralıkları belirleme
    critical_points = sorted(critical_points)
    
    if f_prime.subs(x, critical_points[0]) >= 0:
        increasing_intervals.append("(-oo, " + str(critical_points[0]) + ")")
    else:
        decreasing_intervals.append("(-oo, " + str(critical_points[0]) + ")")
    
    for i in range(len(critical_points) - 1):
        if f_prime.subs(x, critical_points[i]) >= 0 and f_prime.subs(x, critical_points[i + 1]) >= 0:
            increasing_intervals.append("(" + str(critical_points[i]) + ", " + str(critical_points[i + 1]) + ")")
        elif f_prime.subs(x, critical_points[i]) <= 0 and f_prime.subs(x, critical_points[i + 1]) <= 0:
            decreasing_intervals.append("(" + str(critical_points[i]) + ", " + str(critical_points[i + 1]) + ")")
    
    if f_prime.subs(x, critical_points[-1]) <= 0:
        decreasing_intervals.append("(" + str(critical_points[-1]) + ", oo)")
    else:
        increasing_intervals.append("(" + str(critical_points[-1]) + ", oo)")

# Sonuçları yazdırma
print("Artan aralıklar: " + ", ".join(increasing_intervals))
print("Azalan aralıklar: " + ", ".join(decreasing_intervals))
