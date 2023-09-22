# kan testi


A = int(input("A Çöktümü[1] - Çökmedimi[0] :"))
B = int(input("\nB Çöktümü[1] - Çökmedimi[0] :"))
O = int(input("\n0 Çöktümü[1] - Çökmedimi[0] :"))
RH = int(input("\nRH Çöktümü[1] - Çökmedimi[0] :"))


if (A == 1 and B == 0  and RH == 0):
    print("A RH(-)")
    
elif (A == 1 and B == 0  and RH == 1):
    print("A RH(+)")
    
elif (A == 0 and B == 1  and RH == 0):
    print("B RH(-)")
    
elif (A == 0 and B == 1  and RH == 1):
    print("B RH(+)")
    
elif (A == 1 and B == 1  and RH == 0):
    print("AB RH(-)")

elif (A == 1 and B == 1  and RH == 1):
    print("AB RH(+)")

elif (A == 0 and B == 0  and O == 1 and RH == 0):
    print("0 RH(-)")
    
elif (A == 0 and B == 0  and O == 1 and RH == 1):
    print("0 RH(+)")
