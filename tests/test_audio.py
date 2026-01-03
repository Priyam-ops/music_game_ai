from audio.loader import load_audio
from audio.onset import detect_onsets
from audio.pitch import detect_pitch
from game.hit_objects import notes_to_hit_objects

AUDIO_PATH = r"C:\hp\test.wav"

y, sr = load_audio(AUDIO_PATH)
onset_times, _ = detect_onsets(y, sr)
notes = detect_pitch(y, sr, onset_times)

hit_objects = notes_to_hit_objects(notes)

print("Generated hit objects:")
for obj in hit_objects:
    print(obj)
