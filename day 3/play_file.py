import wave, pyaudio

#открываем файл и читаем из него данные
audiofile = wave.open("recorded.wav")
n = audiofile.getnframes()
data = audiofile.readframes(n)

#создаем pyaudio и узнаем формат данных по глубине
audio = pyaudio.PyAudio()
f = audio.get_format_from_width(audiofile.getsampwidth())

#открываем поток и запихиваем туда аудио
output_stream = audio.open(
    format=f,
    channels=audiofile.getnchannels(),
    rate=audiofile.getframerate(),
    output=True)
output_stream.write(data)
output_stream.close()

