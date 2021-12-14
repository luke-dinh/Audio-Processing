import librosa
import os
import IPython.display as ipd

audio_hum = os.listdir("mini_dataset_hum")
for file in audio_hum:
    x, sr = librosa.load(file)
