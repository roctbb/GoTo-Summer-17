#!/usr/bin/python
import serial
import wave, pyaudio
import struct
import time
from speechkit import record_to_text

#The following line is for serial over GPIO
port = '/dev/tty.usbmodem14511' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino


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
framerate = 16000
channels = 1
chunk_size = 1024

# создаем pyaudio и узнаем формат данных по глубине
audio = pyaudio.PyAudio()
f = audio.get_format_from_width(sample_width)

input_stream = audio.open(
    format=f,
    channels=channels,
    rate=framerate,
    input=True,
    frames_per_buffer=chunk_size)

while True:
    data = b''
    data = record(input_stream, 0.5, framerate, chunk_size)
    if level(data) > 1500:
        print("start recording")
        data += record(input_stream, 2, framerate, chunk_size)
        print("stop recording")
        input_stream.stop_stream()
        try:
            command = record_to_text(data)
            print(command)
            if command.find("вкл")!=-1:
                ard.write(bytes('1'.encode('ascii')));
                time.sleep(1)
            if command.find("выкл")!=-1:
                ard.write(bytes('0'.encode('ascii')));
                time.sleep(1)
        except:
            pass
        input_stream.start_stream()



