#çekliş yapalım

import random

def cevap(numara):
    if numara == 1:
        return 'besat kazandı'
    elif numara == 2:
        return 'ahmet kazandı'
    elif numara == 3:
        return 'ali kazandı'
    elif numara == 4:
        return 'cansu kazandı'
    elif numara == 5:
        return 'sedef kazandı'
    elif numara == 6:
        return 'dilay kazandı'
    elif numara == 7:
        return 'şeref kazandı'


r = random.randint(1,7) #1 ila 7 arası random üret

cevapbuolsun = cevap(r)
print('-'*50)
print(cevapbuolsun)
    
