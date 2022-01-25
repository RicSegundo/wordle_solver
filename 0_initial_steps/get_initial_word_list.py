from mimetypes import init
import pandas as pd
import os
from typing import List

"""Data retrieved from 'https://www.wordgamedictionary.com/english-word-list/download/english.txt'"""

initial_file: str = r'english.txt'
initial_file_path: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), initial_file)

file_export: str = r'5_letter_word_list.csv'
file_path_export: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_export)

# Only take 5 letters words
caracthers_value: int = 5

with open(initial_file_path) as x:
    five_letter_word_list: List  = [line.strip().lower() for line in x if len(line) == (caracthers_value + 1)]

# Clean up list:
five_letter_word_list: List = [word for word in five_letter_word_list if word.isalpha() and len(word) == 5]

# Export list into a .csv
file_export: pd.DataFrame = pd.DataFrame(five_letter_word_list, columns =['five_letter_words'])
file_export.to_csv(file_path_export, sep=';', index=False)

