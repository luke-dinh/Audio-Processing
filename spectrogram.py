import librosa
import librosa.display as display
import os
import IPython.display as ipd
import sys
import matplotlib.pyplot as plt

sys.path.append(".")

audio_path = "./mini_dataset_hum/0000.mp3"
# audio_hum = os.listdir("mini_dataset_hum")
# audio_arr = []
# ipd.Audio(audio_path)

x, sr = librosa.core.load(audio_path)
# plt.figure(figsize=(10,10))
# display.waveplot(x, sr=sr)
# plt.show()

# for file in audio_hum:
#     x, sr = librosa.core.load(file)
#     audio_arr.append(x)

# plt.figure(figsize=(10,10))
# librosa.display.waveplot(audio_arr[0])

# Spectrogram
X = librosa.core.stft(x)
Xdb = librosa.core.amplitude_to_db(abs(X))
plt.figure(figsize=(10,10))
display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()