#! /usr/bin/env python3

import argparse

NOTE_TO_SEMITONE = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5,
    'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10,
    'B': 11
}


SEMITONE_TO_NOTE = [
    'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'
]


scales = {
    "Major / Ionian": [0, 2, 4, 5, 7, 9, 11],
    "Melodic Minor": [0, 2, 3, 5, 7, 9, 11],
    "Harmonic Minor": [0, 2, 3, 5, 6, 9, 11],
    "Natural Minor / Aeolian": [0, 2, 3, 5, 7, 8, 10],
    "Harmonic Minor / Mohammedan": [0, 2, 3, 5, 7, 8, 11],
    "Major Pentatonic": [0, 2, 4, 7, 9],
    "Minor Pentatonic": [0, 3, 5, 7, 10],
    "Blues": [0, 3, 5, 6, 7, 10],
    "Minor Blues": [0, 2, 3, 5, 6, 7, 8, 10],
    "Major Blues": [0, 2, 3, 4, 5, 6, 7, 9, 10],
    "Augmented / Whole Tone": [0, 2, 4, 6, 8, 10],
    "Diminished": [0, 2, 3, 5, 6, 8, 9, 11],
    "Half Whole Diminished": [0, 1, 3, 4, 6, 7, 9, 10],
    "Phrygian-Dominan / major Phrygian / Spanish-flamenco": [
        0, 1, 4, 5, 7, 8, 10
    ],
    "Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Lydian": [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "Locrian": [0, 1, 3, 5, 6, 8, 10],
    "Dorian b2": [0, 1, 3, 5, 7, 9, 10],
    "Lydian augmented": [0, 2, 4, 6, 8, 9, 11],
    "Lydian b7 / overture": [0, 2, 4, 6, 7, 9, 10],
    "Mixolydian b13 / Hindu": [0, 2, 4, 5, 7, 8, 10],
    "Locrian #2": [0, 2, 3, 5, 6, 8, 10],
    "Super Locrian / Altered": [0, 1, 3, 4, 6, 8, 10],
    "Enigmatic": [0, 1, 4, 6, 8, 10, 11],
    "Double harmonic / gypsy / Byzantine": [0, 1, 4, 5, 7, 8, 11],
    "Hungarian minor": [0, 2, 3, 6, 7, 8, 11],
    "Persian": [0, 1, 4, 5, 6, 8, 11],
    "Arabian / major Locrian": [0, 2, 4, 5, 6, 8, 10],
    "Japanese": [0, 1, 5, 7, 8],
    "Egyptian": [0, 2, 5, 7, 10],
    "Hirajoshi": [0, 2, 3, 7, 8],
}

def main():
    parser = argparse.ArgumentParser(description='A tool to match groups of notes to possible scales')

    parser.add_argument('Notes', metavar='N', nargs='+', help='A note (e.g. Ab, E#, G)')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.1.1')

    args = parser.parse_args()

    # Convert input note names to their semitone values
    input_semitones = [NOTE_TO_SEMITONE[note_name]
                       for note_name in args.Notes
                       if note_name in NOTE_TO_SEMITONE]


    # For each possible transposition (0 to 11 semitones),
    # create a list of tuples for the input notes.
    # Each tuple: (transposed_semitone, original_semitone,
    #              root_of_this_transposition)
    # 'root_of_this_transposition' is the note that would be the root if this
    # transposition formed a scale starting on C.
    relative_transpositions = []
    for n_semitones_transposition in range(12):  # 0 to 11 semitones
        transposed_input_notes = []
        for original_semitone in input_semitones:
            transposed_semitone = (original_semitone +
                                   n_semitones_transposition) % 12
            # The 'key' or 'root' for this specific transposition group.
            # If the original note C (0) is transposed by
            # n_semitones_transposition, the original root of the scale would be
            # (12 - n_semitones_transposition) % 12.
            # This represents what the tonic would be if the transposed notes were
            # mapped back to a scale starting on C.
            effective_root_semitone = (12 - n_semitones_transposition) % 12
            transposed_input_notes.append(
                (transposed_semitone, original_semitone, effective_root_semitone)
            )
        relative_transpositions.append(transposed_input_notes)


    # Determine potential scale matches
    # 'potential_scale_matches' will be a list of lists.
    # Each inner list corresponds to a scale and contains tuples:
    # (scale_name, potential_tonic_note_name, is_note_in_scale,
    #  original_input_note_name_for_this_tonic, scale_intervals)
    potential_scale_matches = []
    for scale_name, scale_intervals in scales.items():
        for transposed_note_group in relative_transpositions:
            current_scale_details = []
            # All notes in transposed_note_group share the same
            # effective_root_semitone (n[2]) and thus the same potential tonic
            # if this group matches the current scale.
            if not transposed_note_group:  # Skip if input notes were empty or all invalid
                continue

            # The potential tonic for this scale match is determined by the
            # transposition. n[2] (effective_root_semitone) from any note in
            # transposed_note_group gives us this.
            potential_tonic_semitone = transposed_note_group[0][2]
            potential_tonic_note_name = SEMITONE_TO_NOTE[potential_tonic_semitone]

            for transposed_semitone, original_semitone, _ in transposed_note_group:
                is_note_in_scale = transposed_semitone in scale_intervals
                # We need to find which of the original input notes corresponds to
                # this potential tonic. This seems overly complex here; the
                # original_semitone maps directly to an input note, but the
                # important part is the *potential_tonic_note_name* for the scale.
                # The SEMITONE_TO_NOTE[original_semitone] gives the original
                # note name that, after transposition, is being checked against
                # the scale.
                original_input_note_name_for_this_transposed_note = (
                    SEMITONE_TO_NOTE[original_semitone]
                )

                current_scale_details.append((
                    scale_name,
                    potential_tonic_note_name,  # The root of the matched scale
                    is_note_in_scale,
                    # The specific input note being checked:
                    original_input_note_name_for_this_transposed_note,
                    scale_intervals
                ))
            potential_scale_matches.append(current_scale_details)


    # Filter for actual matches where all input notes fit the scale
    # Each item in 'actual_matches' will be the first element of the inner list
    # from potential_scale_matches, which contains the scale_name and the tonic.
    actual_matches = []
    for scale_details_list in potential_scale_matches:
        # detail[2] is 'is_note_in_scale'
        if scale_details_list and all(detail[2] for detail in scale_details_list):
            # All notes in this group match the scale, so add the representative
            # detail (scale name, tonic, intervals). The first element (detail[0])
            # contains all necessary info for printing the match.
            actual_matches.append(scale_details_list[0])


    for match_info in actual_matches:
        # match_info is (scale_name, potential_tonic_note_name,
        #                is_note_in_scale (True), original_input_note_name,
        #                scale_intervals)
        # We need scale_name (match_info[0]) and
        # potential_tonic_note_name (match_info[1])
        # And scale_intervals (match_info[4]) to print the full scale notes.
        tonic_note_name = match_info[1]
        scale_name = match_info[0]
        scale_intervals = match_info[4]

        # Construct the notes of the matched scale starting from the tonic
        notes_in_matched_scale = [
            SEMITONE_TO_NOTE[(interval + NOTE_TO_SEMITONE[tonic_note_name]) % 12]
            for interval in scale_intervals
        ]
        print(f"{tonic_note_name} {scale_name}: {' '.join(notes_in_matched_scale)}")

if __name__ == '__main__':
    main()
