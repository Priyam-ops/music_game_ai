import librosa
import numpy as np

def detect_pitch(y, sr, onset_times, fmin=librosa.note_to_hz("C2"), fmax=librosa.note_to_hz("C7")):
    """
    Detect pitch at each onset time.
    Returns a list of (time, frequency, note_name).
    """
    pitches = []

    for t in onset_times:
        # Take a short window around the onset
        start_sample = int(t * sr)
        end_sample = start_sample + int(0.1 * sr)  # 100 ms window

        frame = y[start_sample:end_sample]
        if len(frame) == 0:
            continue

        # Use YIN algorithm for pitch detection
        f0 = librosa.yin(
            frame,
            fmin=fmin,
            fmax=fmax,
            sr=sr
        )

        # Take median to stabilize
        freq = np.median(f0)

        if np.isnan(freq):
            continue

        note = librosa.hz_to_note(freq)
        pitches.append((t, freq, note))

    return pitches
