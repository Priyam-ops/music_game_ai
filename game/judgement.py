def judge_hit(note_time, input_time):
    """
    Judge player input timing against a note.

    Returns: "Perfect", "Good", or "Miss"
    """
    delta = abs(input_time - note_time)

    if delta <= 0.05:
        return "Perfect"
    elif delta <= 0.12:
        return "Good"
    else:
        return "Miss"
