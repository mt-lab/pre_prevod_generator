import csv
from tkinter import filedialog
import noun_toolkit
import logging


def generate_nouns(input_row):
    print("It is a noun")
    noun_toolkit.generate_plural(input_row)


def generate_verbs(input_row):
    print("It is a verb")


def generate_adjectives(input_row):
    print("It is an adjective")


def determine_part_of_speech(input_row):
    if input_row['partOfSpeech'] == 'n.':
        generate_nouns(input_row)
    if input_row['partOfSpeech'] == 'v.':
        generate_verbs(input_row)
    if input_row['partOfSpeech'] == 'adj.':
        generate_adjectives(input_row)


input_csv = filedialog.askopenfile(mode='r')
with open(input_csv.name, newline='', encoding='windows-1251') as csvfile:
    word_reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in word_reader:
        determine_part_of_speech(row)

