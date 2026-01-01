# Music Game AI 🎵

A Python-based project that aims to:
- Convert audio files into musical structure
- Generate spectrograms and detect rhythmic events
- Serve as the foundation for an osu!-style rhythm game
- Eventually support music sheet (MIDI / notation) generation

---

## Current Features (Completed)

- Audio loading and normalization
- Waveform visualization
- Mel spectrogram generation
- Onset (note start) detection

These features form the core audio analysis pipeline.

---

## Project Structure
```
music_game_ai/
│
├── audio/
│ ├── loader.py # Audio loading and normalization
│ ├── preprocessing.py # Spectrogram generation
│ └── onset.py # Onset detection
│
├── tests/
│ └── test_audio.py # Test and visualization scripts
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python
- librosa
- numpy
- matplotlib

---

## How to Run (So Far)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. run 
    ```bash
   python -m tests.test_audio