import librosa
import numpy as np

def mel_spectrogram(y, sr, n_mels=128):
    """
    Convert audio waveform into a Mel spectrogram.
    """
    S = librosa.feature.melspectrogram(
        y=y,
        sr=sr,
        n_fft=2048,
        hop_length=512,
        n_mels=n_mels
    )

    # Convert to log scale (dB)
    S_db = librosa.power_to_db(S, ref=np.max)
    return S_db
