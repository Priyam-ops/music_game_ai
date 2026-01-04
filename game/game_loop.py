import time

class GameLoop:
    def __init__(self, hit_objects, judge_fn, score_manager):
        self.hit_objects = hit_objects
        self.judge = judge_fn
        self.score_manager = score_manager
        self.current_index = 0

    def run(self):
        print("Game started...")
        start_time = time.time()

        while self.current_index < len(self.hit_objects):
            current_time = time.time() - start_time
            obj = self.hit_objects[self.current_index]

            # Simulate player hitting exactly on time
            simulated_input_time = obj["time"]

            if current_time >= obj["time"]:
                judgement = self.judge(obj["time"], simulated_input_time)
                self.score_manager.apply_judgement(judgement)

                print(
                    f"Time {current_time:.2f}s | "
                    f"Lane {obj['lane']} | "
                    f"Note {obj['note']} | "
                    f"{judgement}"
                )

                self.current_index += 1

            time.sleep(0.005)  # Small delay to avoid busy loop

        print("Game finished.")
