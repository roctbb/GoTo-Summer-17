import pyaudio, wave, struct
from speechkit import text_to_record

text = "Купила баба порося, а он ей как раз."

path = text_to_record(text)
file = wave.open(path)
data = file.readframes(file.getnframes())

audio = pyaudio.PyAudio()
output_stream = audio.open(format=audio.get_format_from_width(file.getsampwidth()),
                channels=file.getnchannels(),
                rate=file.getframerate(),
                output=True,
                frames_per_buffer=1024)
output_stream.write(data)
