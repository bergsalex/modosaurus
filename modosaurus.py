#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='A tool to match groups of notes to possible scales')

parser.add_argument('Notes', metavar='N', nargs='+')

args = parser.parse_args()

t = {'C':  0,
     'C#': 1,
     'Db': 1,
     'D':  2,
     'D#': 3,
     'Eb': 3,
     'E':  4,
     'F':  5,
     'F#': 6,
     'Gb': 6,
     'G':  7,
     'G#': 8,
     'Ab': 8,
     'A':  9,
     'A#': 10,
     'Bb': 10,
     'B':  11}

t2 = ['C',
      'Db',
      'D',
      'Eb',
      'E',
      'F',
      'Gb',
      'G',
      'Ab',
      'A',
      'Bb',
      'B']

scales = {"Major / Ionian": [0, 2, 4, 5, 7, 9, 11],
          "Melodic Minor": [0, 2, 3, 5, 7, 9, 11],
          "Harmonic Minor": [0, 2, 3, 5, 6, 9, 11],
          "Natural Minor / Aeolian":  [0, 2, 3, 5, 7, 8, 10],
          "Harmonic Minor / Mohammedan":  [0, 2, 3, 5, 7, 8, 11],
          "Major Pentatonic":  [0, 2, 4, 7, 9],
          "Minor Pentatonic":  [0, 3, 5, 7, 10],
          "Blues":  [0, 3, 5, 6, 7, 10],
          "Minor Blues":  [0, 2, 3, 5, 6, 7, 8, 10],
          "Major Blues":  [0, 2, 3, 4, 5, 6, 7, 9, 10],
          "Augmented / Whole Tone":  [0, 2, 4, 6, 8, 10],
          "Diminished":  [0, 2, 3, 5, 6, 8, 9, 11],
          "Half Whole Diminished":  [0, 1, 3, 4, 6, 7, 9, 10],
          "Phrygian-Dominan / major Phrygian / Spanish-flamenco":  [0, 1, 4, 5, 7, 8, 10],
          "Dorian":  [0, 2, 3, 5, 7, 9, 10],
          "Phrygian":  [0, 1, 3, 5, 7, 8, 10],
          "Lydian":  [0, 2, 4, 6, 7, 9, 11],
          "Mixolydian":  [0, 2, 4, 5, 7, 9, 10],
          "Locrian":  [0, 1, 3, 5, 6, 8, 10],
          "Dorian b2":  [0, 1, 3, 5, 7, 9, 10],
          "Lydian augmented":  [0, 2, 4, 6, 8, 9, 11],
          "Lydian b7 / overture":  [0, 2, 4, 6, 7, 9, 10],
          "Mixolydian b13 / Hindu":  [0, 2, 4, 5, 7, 8, 10],
          "Locrian #2":  [0, 2, 3, 5, 6, 8, 10],
          "Super Locrian / Altered":  [0, 1, 3, 4, 6, 8, 10],
          "Enigmatic":  [0, 1, 4, 6, 8, 10, 11],
          "Double harmonic / gypsy / Byzantine": [0, 1, 4, 5, 7, 8, 11],
          "Hungarian minor":  [0, 2, 3, 6, 7, 8, 11],
          "Persian":  [0, 1, 4, 5, 6, 8, 11],
          "Arabian / major Locrian":  [0, 2, 4, 5, 6, 8, 10],
          "Japanese":  [0, 1, 5, 7, 8],
          "Egyptian":  [0, 2, 5, 7, 10],
          "Hirajoshi":  [0, 2, 3, 7, 8],
          }

relative = [[((i+n) % 12, i, (12-n) % 12)
             for i in (t[n]
             for n in args.Notes
             if n in t.keys())]
            for n in xrange(0, 11)]


a = [[(name, t2[n[2]], n[0] in scale, t2[n[1]]) for n in rel]
     for name, scale in scales.iteritems()
     for rel in relative]

matches = [i[0] for i in a if all(x[2] for x in i)]
for match in matches:
    print "%s %s" % (match[1], match[0])
