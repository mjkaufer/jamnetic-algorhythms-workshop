from note_util import isMeasureSilent, GANote, getNonRestNotes
from random import random, choice, shuffle, sample, choices

# all functions here have same args, and will return an array of notes, mutates `currentPiece` argument
# return false if operation fails for some reason, so we know to run a different mutator on the current function

def getMutators():
    return [pickRandomChordTone, subdivide]

def getRandomMutator(duration = 0):
    # we can parameterize the likeliness we pick a given mutator based on the length of the note!
    # here, we want the odds that we subdivide an already small note to be small
    quanta = (duration / 4.0) ** 1.5

    # these probabilities line up w/ the mutators object above
    # also they're relative weights so don't worry about normalizing
    mutator_probabilities = [1, quanta]

    # because normal choice doesn't support weights :P
    return choices(getMutators(), weights=mutator_probabilities)[0]

def pickRandomChordTone(currentPiece, chordProgression, measureIndex, noteIndex):
    original_midi_note = currentPiece[measureIndex][noteIndex].midi_note

    new_midi_note = choice(chordProgression[measureIndex])

    delta = original_midi_note - new_midi_note
    while abs(delta) > 6:
        # try to bring them closer together
        if delta < 0:
            new_midi_note -= 12
        else:
            new_midi_note += 12

        delta = original_midi_note - new_midi_note

    currentPiece[measureIndex][noteIndex].midi_note = new_midi_note
    return True

def subdivide(currentPiece, chordProgression, measureIndex, noteIndex):
    p = random()

    note = currentPiece[measureIndex][noteIndex]

    note_array = []

    if p < 0.5:
        # even subdivision
        note_array = [note.clone(new_duration=note.duration / 2.0), note.clone(new_duration=note.duration / 2.0)]
    elif p < 0.75:
        # triplet
        note_array = [note.clone(new_duration=note.duration / 3.0), note.clone(new_duration=note.duration / 3.0), note.clone(new_duration=note.duration / 3.0)]
    else:
        # dotted
        long_note = note.clone(new_duration=note.duration * 0.75)
        short_note = note.clone(new_duration=note.duration * 0.25)

        if random() < 0.5:
            note_array = [long_note, short_note]
        else:
            note_array = [short_note, long_note]


    measure = currentPiece[measureIndex]

    currentPiece[measureIndex] = measure[:noteIndex] + note_array + measure[noteIndex+1:]

    return True