from audio.loader import load_audio
from audio.preprocessing import mel_spectrogram
from audio.onset import detect_onsets
import matplotlib.pyplot as plt
import librosa.display

y, sr = load_audio("test.wav")

# Detect onsets
onset_times, onset_env = detect_onsets(y, sr)

# Plot onset strength
plt.figure(figsize=(10, 4))
plt.plot(onset_env)
plt.title("Onset Strength Over Time")
plt.xlabel("Frame Index")
plt.ylabel("Strength")
plt.show()

print("Detected onset times (seconds):")
print(onset_times)
