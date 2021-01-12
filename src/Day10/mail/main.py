with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
names = map(lambda x: x.strip("\n"), names)

with open("Input/Letters/starting_letter.docx") as file:
    letter_base = file.read()

for name in names:
    new_letter = letter_base.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.docx", mode="w") as file:
        file.write(new_letter)
