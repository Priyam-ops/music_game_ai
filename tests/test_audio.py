from audio.loader import load_audio
from audio.onset import detect_onsets
from audio.pitch import detect_pitch
from game.hit_objects import notes_to_hit_objects
from game.judgement import judge_hit
from game.scoring import ScoreManager

AUDIO_PATH = r"C:\hp\test.wav"

y, sr = load_audio(AUDIO_PATH)
onset_times, _ = detect_onsets(y, sr)
notes = detect_pitch(y, sr, onset_times)
hit_objects = notes_to_hit_objects(notes)

score_manager = ScoreManager()

# Simulate player input
for obj in hit_objects:
    note_time = obj["time"]
    simulated_input = note_time + 0.03  # 30 ms late
    judgement = judge_hit(note_time, simulated_input)

    score_manager.apply_judgement(judgement)

    print(
        f"Note {obj['note']} | "
        f"Judgement: {judgement} | "
        f"Score: {score_manager.score} | "
        f"Combo: {score_manager.combo}"
    )

print("\nFinal Results:")
print(score_manager.summary())
