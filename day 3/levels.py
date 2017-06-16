import wave, pyaudio

import struct


# запись звука time секунд
def record(stream, time, framerate, chunk_size):
    data = b''
    for i in range(int(time * framerate / chunk_size)):
        chunk_data = stream.read(chunk_size)
        data = data + chunk_data
    return data


# измерение громкости
def level(data):
    n = len(data) // 2
    frames = struct.unpack('={0}h'.format(n), data)
    average = sum(list(map(abs, frames))) // n
    return average


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

output_stream = audio.open(
    format=f,
    channels=channels,
    rate=framerate,
    output=True,
    frames_per_buffer=chunk_size)

while True:
    data = b''
    data = record(input_stream, 0.5, framerate, chunk_size)
    if level(data) > 1500:
        print("start recording")
        data += record(input_stream, 10, framerate, chunk_size)
        input_stream.stop_stream()

        output_stream.write(data)
        input_stream.start_stream()
        print("stop recording")


