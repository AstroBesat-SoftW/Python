import logging

logging.basicConfig(filename="detailed_system_log.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    logging.info(event)

log_event("Sistem Çağrısı: read() - Başarılı")
log_event("Sistem Çağrısı: write() - Başarılı")
