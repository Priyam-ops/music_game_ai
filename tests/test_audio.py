from audio.loader import load_audio
from audio.onset import detect_onsets
from audio.pitch import detect_pitch
from game.hit_objects import notes_to_hit_objects
from game.judgement import judge_hit
from game.scoring import ScoreManager
from game.game_loop import GameLoop

AUDIO_PATH = r"C:\hp\test.wav"

y, sr = load_audio(AUDIO_PATH)
onset_times, _ = detect_onsets(y, sr)
notes = detect_pitch(y, sr, onset_times)
hit_objects = notes_to_hit_objects(notes)

score_manager = ScoreManager()
game = GameLoop(hit_objects, judge_hit, score_manager)
game.run()

print("\nFinal Score Summary:")
print(score_manager.summary())
