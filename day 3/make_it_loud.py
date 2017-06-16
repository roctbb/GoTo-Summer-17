import wave, struct

audiofile = wave.open("task1.wav")
params = audiofile.getparams()
n = audiofile.getnframes()

data = audiofile.readframes(n)
frames = struct.unpack("={0}h".format(n), data)

loud_frames = []
for frame in frames:
    loud_frames.append(frame * 10)

loud_data = struct.pack("={0}h".format(n), *loud_frames)

resultfile = wave.open('result.wav', 'wb')
resultfile.setparams(params)
resultfile.writeframes(loud_data)