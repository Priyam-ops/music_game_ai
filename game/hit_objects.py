def notes_to_hit_objects(notes, num_lanes=4):
    """
    Convert detected notes into rhythm-game hit objects.

    notes: list of (time, frequency, note_name)
    """
    hit_objects = []

    for time, freq, note in notes:
        # Map pitch to lane
        lane = hash(note) % num_lanes

        hit_object = {
            "time": float(round(time, 3)),  # seconds
            "lane": lane,
            "note": note
        }

        hit_objects.append(hit_object)

    return hit_objects
