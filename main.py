import sys
import os
from random import seed
from copy import deepcopy

# import all_of_me, blue_bossa, another_day_of_sun, minor_swing, fly_me_to_the_moon, mary, cantina
import cantina

from algo_util import generation
from note_util import writePiece

seed_num = 42
iter_count = 100
root_dir = './pieces/out/'

piece_imports = [
    # all_of_me.getPiece(),
    # blue_bossa.getPiece(),
    # another_day_of_sun.getPiece(),
    # minor_swing.getPiece(),
    # fly_me_to_the_moon.getPiece(),
    # mary.getPiece(),
    cantina,
]

pieces = [p.getPiece() for p in piece_imports]

piece_num = 0

piece, chord_progression, piece_title = pieces[piece_num]

print("Running on {} with seed of {} and generation number of {}".format(piece_title, seed_num, iter_count))

seed(seed_num)

population_size = 20

population = [deepcopy(piece) for i in range(population_size)]

if not os.path.exists(root_dir):
    os.makedirs(root_dir)

# writePiece(piece, chord_progression, 'init', 'init.mid')

for gen_num in range(iter_count):

    population = generation(population, chord_progression, piece)
    title = '{} ft. Genetic Algos, Gen {}'.format(piece_title, gen_num)

    for index in [0, len(population) - 1]:
        fname = root_dir + '{}-Seed{:0>2d}-Gen{:0>2d}-Rank{:0>2d}.mid'.format(piece_title.replace(" ", "-"), seed_num, gen_num, index)
        writePiece(population[index], chord_progression, title, fname)

