class ScoreManager:
    def __init__(self):
        self.score = 0
        self.combo = 0
        self.max_combo = 0

        self.counts = {
            "Perfect": 0,
            "Good": 0,
            "Miss": 0
        }

    def apply_judgement(self, judgement):
        if judgement == "Perfect":
            self.score += 300
            self.combo += 1
        elif judgement == "Good":
            self.score += 100
            self.combo += 1
        else:  # Miss
            self.combo = 0

        self.counts[judgement] += 1
        self.max_combo = max(self.max_combo, self.combo)

    def summary(self):
        return {
            "score": self.score,
            "combo": self.combo,
            "max_combo": self.max_combo,
            "counts": self.counts
        }
