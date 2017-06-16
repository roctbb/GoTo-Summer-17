import wave, pyaudio

import struct

#измерение громкости
def level(stream, time, framerate, sample_width, chunk_size):
    data = b''
    # записали полсекунды звука
    for i in range(int(time * framerate / chunk_size)):
        chunk_data = stream.read(chunk_size)
        data = data + chunk_data
    n = len(data) // sample_width
    frames = struct.unpack('={0}h'.format(n), data)
    average = sum(list(map(abs, frames))) // n
    return average

sample_width = 2
framerate = 44100
channels = 1
chunk_size = 1024
record_time = 10

#создаем pyaudio и узнаем формат данных по глубине
audio = pyaudio.PyAudio()
f = audio.get_format_from_width(sample_width)

input_stream = audio.open(
    format=f,
    channels=channels,
    rate=framerate,
    input=True,
    frames_per_buffer=chunk_size)

while True:
    l = level(input_stream, 0.5, framerate, sample_width, chunk_size)
    print(l)

