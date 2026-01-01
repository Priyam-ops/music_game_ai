import numpy as np
import soundfile as sf

sr = 22050
t = np.linspace(0, 2, int(sr * 2), endpoint=False)
y = 0.5 * np.sin(2 * np.pi * 440 * t)  # 440 Hz tone

sf.write("test.wav", y, sr)
