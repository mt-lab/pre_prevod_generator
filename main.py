#! /usr/bin/env python
import ru_parse_word_bank
import csv
from tkinter import filedialog


def ask_for_file():
    print("Select basic vocabulary:")
    return filedialog.askopenfile(mode='r')


def select_language():
    print("What's in the file?")
    print("ru - Russian")
    print("No other languages available yet")
    language_choice = input("Choose language: ")
    if language_choice == "ru":
        with open(file.name, newline='', encoding='windows-1251') as csvfile:
            word_reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in word_reader:
                ru_parse_word_bank.determine_part_of_speech(row)
    else:
        print("Are you sure? Try again")
        select_language()


file = ask_for_file()
select_language()
