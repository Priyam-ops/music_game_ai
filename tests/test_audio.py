from audio.loader import load_audio
from audio.onset import detect_onsets
from audio.pitch import detect_pitch
from game.hit_objects import notes_to_hit_objects
from game.judgement import judge_hit

AUDIO_PATH = r"C:\hp\test.wav"

y, sr = load_audio(AUDIO_PATH)
onset_times, _ = detect_onsets(y, sr)
notes = detect_pitch(y, sr, onset_times)
hit_objects = notes_to_hit_objects(notes)

# Simulate player hitting slightly late
for obj in hit_objects:
    note_time = obj["time"]
    simulated_input = note_time + 0.1  # 30 ms late
    result = judge_hit(note_time, simulated_input)

    print(
        f"Lane {obj['lane']} | "
        f"Note {obj['note']} | "
        f"Judgement: {result}"
    )
