import pyaudio
from speechkit import record_to_text

audio = pyaudio.PyAudio()
input_stream = audio.open(format=audio.get_format_from_width(2),
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=1024)
data = b''
for i in range(16000 * 4//1024):
    data += input_stream.read(1024)

text = record_to_text(data)
print(text)

