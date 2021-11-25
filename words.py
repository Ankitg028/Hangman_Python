import pandas as pd

df = pd.read_csv('Hangman_Python\syllable_word.csv')

words_list = df['word'].tolist()

# print(words_list)