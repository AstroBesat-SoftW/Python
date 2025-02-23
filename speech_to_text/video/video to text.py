import moviepy.editor as mp
import speech_recognition as sr

# MP4 dosyasını yükle
video_file = "video.mp4"

# MP4 dosyasından sesi çıkart
clip = mp.VideoFileClip(video_file)
clip.audio.write_audiofile("temp.wav")

# Ses dosyasını tanıma işlemini yap
audio_file = "temp.wav"
recognizer = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
    try:
        # Ses dosyasını metne çevir
        text = recognizer.recognize_google(audio, language="tr-TR")
        print(text)
    except sr.UnknownValueError:
        print("Ses tanınmadı.")
