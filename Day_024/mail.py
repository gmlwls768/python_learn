with open("Day_024/Input/Names/invited_names.txt") as name_file:
    name = name_file.readlines()  # return list type

with open("Day_024/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()  # return string type
    for nam in name:
        strip_name = nam.strip()  # delete space
        new_letter = letter.replace(
            "[name]", strip_name)  # replace [name] to name
        with open(f"Day_024/Output/ReadyToSend/letter_for_{strip_name}.txt", "w") as complete:
            complete.write(new_letter)
