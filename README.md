# Jamnetic Algorhythms

Build your own improvisation!

TODO file details here

## Setup

Install the `music21` and the `midiutil` python packages from `requirements.txt` and you're good to go!

## Making Songs

You'll have to make a python file for your song and manually fill out the chord progression. To find `.mxl` melodies, check out [Musescore](https://musescore.com/sheetmusic?text=rambling+wreck)!

When making a chord progression, you want the root of your chord to be in the same octave range as your melody, since the genetic algorithm just samples from the chord progression. When outputting the song, the chord progression gets knocked down two octaves.

## Improving Upon The Algorithm

### Adding Mutators
Go to `mutators.py`, create a function (make sure it returns `True` if successful), and add it to the `mutators` array at the top of the file. Also, give it a probability in the `mutator_probabilities` array in `getRandomMutator`

## Other Notes

All of this boilerplate is recycled from the [original repo I made a while back](https://github.com/mjkaufer/jamnetic-algorhythms). I tried to clean it up a little before copying it here though!

Some OK outputs I've noticed are

* Cantina band
    * Seed 42, Generation 29, Rank 0