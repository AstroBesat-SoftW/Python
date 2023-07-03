#burada yapman gereken görseldeki çıktıyı alman paint aç
#boş sayfanın ortasına fareyi koy kalanını kendi yavaşça oluşturuyor çizerek.

import pyautogui, time

time.sleep(5)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance -5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance -5
    pyautogui.dragRel(0, -distance, duration=0.2)
    
    
