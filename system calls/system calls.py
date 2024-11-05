import psutil
import time

def log_system_calls():
    # Log dosyasını açıyoruz
    with open("system_log.txt", "a") as log_file:
        while True:
            for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                try:
                    # Her işlem için PID, adı, CPU ve bellek kullanımını log dosyasına yazıyoruz
                    log_file.write(
                        f"PID: {process.info['pid']}, "
                        f"Name: {process.info['name']}, "
                        f"CPU: {process.info['cpu_percent']}%, "
                        f"Memory: {process.info['memory_info'].rss}\n"
                    )
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # İşlem mevcut değilse, erişim yoksa veya zombi işlemse devam ediyoruz
                    continue
            log_file.write("\n")
            # 5 saniye bekleme
            time.sleep(5)

# Fonksiyonu çağırıyoruz
log_system_calls()
