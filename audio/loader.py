import librosa
import numpy as np

def load_audio(path, sr=22050):
    """
    Load an audio file and convert it to:
    - mono
    - fixed sample rate
    - normalized amplitude
    """
    y, sr = librosa.load(path, sr=sr, mono=True)
    y = librosa.util.normalize(y)
    return y, sr
