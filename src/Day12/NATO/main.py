import pandas

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in csv_data.iterrows()}

is_on = True
while is_on:
    user_input = input("Enter a word: ").upper()
    if user_input == "EXIT":
        is_on = False
        continue
    output = [phonetic_dictionary[letter] for letter in user_input]
    print(output)
