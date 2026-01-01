import librosa
import numpy as np

def detect_onsets(y, sr, hop_length=512):
    """
    Detect note onsets in an audio signal.

    Returns onset times in seconds.
    """
    onset_env = librosa.onset.onset_strength(
        y=y,
        sr=sr,
        hop_length=hop_length
    )

    onset_frames = librosa.onset.onset_detect(
        onset_envelope=onset_env,
        sr=sr,
        hop_length=hop_length
    )

    onset_times = librosa.frames_to_time(
        onset_frames,
        sr=sr,
        hop_length=hop_length
    )

    return onset_times, onset_env
