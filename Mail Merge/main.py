PLACEHOLDER = "[name]"

with open("Python Bootcamp/Intermediate/Mail Merge/names.txt") as f_names:
    names_list = f_names.readlines()

with open("Python Bootcamp/Intermediate/Mail Merge/template_letter.txt") as f_template:
    template_letter = f_template.read()

for name in names_list:
    with open(f"Python Bootcamp/Intermediate/Mail Merge/Ready to send/letter_for_{name.strip()}.txt", "w") as f_letter:
        letter_to_send = template_letter.replace(PLACEHOLDER, name.strip())
        f_letter.write(letter_to_send)