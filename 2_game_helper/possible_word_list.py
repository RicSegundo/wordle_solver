import pandas as pd
import os
from typing import Dict, List
from Levenshtein import distance as levenshtein_distance
from itertools import permutations

file_list: str = r'5_letter_word_list.csv'
file_directory: str = r'wordle_solver/0_initial_steps'
file_list_path: str = os.path.join(file_directory, file_list)

word_list_df: pd.DataFrame = pd.read_csv(file_list_path)
word_list: List = word_list_df[word_list_df.columns[0]].to_list()

valid_caracthers = ['i', 't']
positive_positions = []
negative_positions = [(2,3),(1,)]
negative_caracthers = ['d', 'a', 'e', 'u', 's', 'r', 'p']

final_list = []

for word in word_list:
    if all(x in word for x in valid_caracthers) and not any(x in word for x in negative_caracthers):
        for ind, positive in enumerate(valid_caracthers):
            if word.index(positive) not in negative_positions[ind]:
                final_list.append(word)

print(final_list)

