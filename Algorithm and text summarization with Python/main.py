import subprocess

# İlk kodu çalıştır
subprocess.run(["python", "turn.py"])

# İlk kod tamamlandıktan sonra diğer kodları çalıştır
subprocess.run(["python", "turn2.py"])
subprocess.run(["python", "turn3.py"])
subprocess.run(["python", "turnend.py"])
