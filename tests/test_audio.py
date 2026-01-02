from audio.loader import load_audio
from audio.onset import detect_onsets
from audio.pitch import detect_pitch
from audio.midi import notes_to_midi

AUDIO_PATH = r"C:\hp\test.wav"

y, sr = load_audio(AUDIO_PATH)
onset_times, _ = detect_onsets(y, sr)
notes = detect_pitch(y, sr, onset_times)

midi_path = notes_to_midi(notes, output_path="output.mid")

print(f"MIDI file created: {midi_path}")

