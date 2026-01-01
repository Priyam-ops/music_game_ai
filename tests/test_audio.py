from audio.loader import load_audio
from audio.onset import detect_onsets
from audio.pitch import detect_pitch

AUDIO_PATH = r"C:\hp\test.wav"

y, sr = load_audio(AUDIO_PATH)

onset_times, _ = detect_onsets(y, sr)
pitches = detect_pitch(y, sr, onset_times)

print("Detected notes:")
for t, freq, note in pitches:
    print(f"Time: {t:.2f}s | Frequency: {freq:.2f} Hz | Note: {note}")
