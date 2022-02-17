
def generate_plural(input_row):

    word = list(input_row['ru'])
    try:
        if word[-1] == 'о':
            print("Generating plural version for a noun ending with 'a'..")
            word[-1] = 'a'
            print(str(word))
    except IndexError:
        print("[-] THERE SEEMS TO BE NO WORD!!!")
