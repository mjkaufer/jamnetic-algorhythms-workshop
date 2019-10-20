# Jamnetic Algorhythms

Build your own improvisation! [Presentation link](https://docs.google.com/presentation/d/1RAhDPbYeFIr2DY1zRlA3OiqJQaPXbZHKo3N5k62ZCLk/edit?usp=sharing)

## Setup

Install the `music21` and the `midiutil` python packages from `requirements.txt` and you're good to go!

## Making Songs

You'll have to make a python file for your song and manually fill out the chord progression. To find `.mxl` melodies, check out [Musescore](https://musescore.com/sheetmusic?text=rambling+wreck)!

When making a chord progression, you want the root of your chord to be in the same octave range as your melody, since the genetic algorithm just samples from the chord progression. When outputting the song, the chord progression gets knocked down two octaves.

## Improving Upon The Algorithm

### Adding Mutators
Go to `mutators.py`, create a function (make sure it returns `True` if successful), and add it to the `mutators` array at the top of the file. Also, give it a probability in the `mutator_probabilities` array in `getRandomMutator`. Then you should be good to go! Feel free to remove mutators from the list or edit the probabilities as you see fit.

### Adding Fitness Functions
In `algo_utils.py`, find the `fitness` function, and add your conditions in there! Ez pz

### Changing 'Reproduction'
Check out `combinePieces` and `generation` in `algo_util.py`, they should be pretty straightforward

### Adding Songs
Make a python file similar to `cantina.py`. You'll need to import a `.mxl` file and write out the chord progression. Import that song into `main.py` and update `piece_imports` and `piece_num` appropriately

## Schema / 'Docs'
Each note in a melody is a `GANote`, which has pitch (as a midi number) and duration (with `1` representing a quarter note). Measures are an array of `GANote`s. Pieces are an array of measures.

Chord progressions handle notes slightly differently – we assume the chord is constant for the measure so we only include the MIDI pitches. Because of this, chord progression measures are simply an array of numbers, with the progressions themselves being an array of measures similar to how melody is organized.

When creating a chord progression, have the root note of each chord be in the same octave as the melody, since the genetic algorithm logic picks chord tones via the chord without transposition.

## Other Notes

All of this boilerplate is recycled from the [original repo I made a while back](https://github.com/mjkaufer/jamnetic-algorhythms). I tried to clean it up a little before copying it here though!

Some OK outputs I've noticed are

* Cantina band
    * Seed 42, Generation 29, Rank 0