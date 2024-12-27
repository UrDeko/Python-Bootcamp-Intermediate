import csv
import pandas

NATO_PHONETIC_ALPHABET = "Python Bootcamp/Intermediate/NATO Alphabet Project/nato_phonetic_alphabet.csv"

with open(NATO_PHONETIC_ALPHABET, "r") as f:
    data = dict(csv.reader(f))

alphabet = pandas.read_csv(NATO_PHONETIC_ALPHABET)

name = input("What is your name?\n")
data = {row.letter: row.code for index, row in alphabet.iterrows()}
result = [data[letter.upper()] for letter in name]
print(result)