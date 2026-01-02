import pretty_midi
import librosa

def notes_to_midi(notes, output_path="output.mid", instrument_name="Acoustic Grand Piano"):
    """
    Convert detected notes into a MIDI file.

    notes: list of (time, frequency, note_name)
    """
    midi = pretty_midi.PrettyMIDI()

    instrument_program = pretty_midi.instrument_name_to_program(instrument_name)
    instrument = pretty_midi.Instrument(program=instrument_program)

    for i, (time, freq, note_name) in enumerate(notes):
        pitch = pretty_midi.note_name_to_number(note_name)

        start = time
        end = start + 0.4  # fixed duration for now
        velocity = 100

        midi_note = pretty_midi.Note(
            velocity=velocity,
            pitch=pitch,
            start=start,
            end=end
        )

        instrument.notes.append(midi_note)

    midi.instruments.append(instrument)
    midi.write(output_path)

    return output_path
