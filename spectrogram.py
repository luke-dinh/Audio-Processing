import librosa
import os
import IPython.display as ipd
import sys

sys.path.append(".")

audio_hum = os.listdir("mini_dataset_hum")
for file in audio_hum:
    x, sr = librosa.core.load(file)
