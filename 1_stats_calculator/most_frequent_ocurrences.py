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

all_freq = {}
position_freq = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {}
}
  
for word in word_list:
    position = 0
    
    for caracther in word:
        # general caracther count
        if caracther in all_freq:
            all_freq[caracther] += 1
        else:
            all_freq[caracther] = 1
        
        # position caracther count
        if caracther in position_freq[position]:
            position_freq[position][caracther] += 1
        else:
            position_freq[position][caracther] = 1
        
        position += 1

top_5 = slice(5)
most_frequent_letters: List = sorted(all_freq, key=all_freq.get, reverse=True)[top_5]

#most_frequent_per_position: Dict = {position: max(position_freq[position], key=position_freq[position].get) for position in position_freq.keys()}

def check_if_already_exist(dictionary: Dict, position:int) -> None:
    most_frequent = max(dictionary[position], key=dictionary[position].get)
    if most_frequent in most_frequent_list:
        del dictionary[position][most_frequent]
        check_if_already_exist(dictionary, position)
    else:
        most_frequent_list.append(most_frequent)
        most_frequent_per_position[position] = most_frequent


most_frequent_per_position: Dict = {}
most_frequent_list: List = []
for position in position_freq.keys():
    fallback = position_freq.copy()
    check_if_already_exist(fallback, position)

most_common: str = ''.join(most_frequent_letters)
most_common_per_position: str = ''.join(most_frequent_per_position.values())

most_common_existant: str = min(word_list, key = lambda w: levenshtein_distance(most_common, w))
most_common_per_position_existant: str = min(word_list, key = lambda w: levenshtein_distance(most_common_per_position, w))

most_common_list: List = [''.join(permutation) for permutation in permutations(most_common)]
most_common_list_existant: List = [min(word_list, key = lambda w: levenshtein_distance(word, w)) for word in most_common_list]

print(most_common_existant)
print(most_common_per_position_existant)
print(most_common_list_existant)
