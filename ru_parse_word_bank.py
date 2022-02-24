import noun_toolkit


def generate_nouns(input_row):
    print("It is a noun")
    noun_toolkit.generate_plural(input_row)


def generate_verbs(input_row):
    print(input_row['ru'] + " is a verb")


def generate_adjectives(input_row):
    print(input_row['ru'] + " is an adjective")


def determine_part_of_speech(input_row):
    if input_row['partOfSpeech'] == 'n.':
        generate_nouns(input_row)
    if input_row['partOfSpeech'] == 'v.':
        generate_verbs(input_row)
    if input_row['partOfSpeech'] == 'adj.':
        generate_adjectives(input_row)


def start(input_row):
    determine_part_of_speech(input_row)
