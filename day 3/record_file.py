import wave, pyaudio

sample_width = 2
framerate = 44100
channels = 1
chunk_size = 1024
record_time = 10

# создаем pyaudio и узнаем формат данных по глубине
audio = pyaudio.PyAudio()
f = audio.get_format_from_width(sample_width)

input_stream = audio.open(
    format=f,
    channels=channels,
    rate=framerate,
    input=True,
    frames_per_buffer=chunk_size)

data = b''

for i in range(record_time * framerate // chunk_size):
    new_data = input_stream.read(chunk_size)
    data = data + new_data

input_stream.close()

audiofile = wave.open('recorded.wav', 'wb')

audiofile.setsampwidth(sample_width)
audiofile.setnchannels(channels)
audiofile.setframerate(framerate)

audiofile.writeframes(data)
