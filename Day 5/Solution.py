from random import choice, shuffle

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n").strip())
nr_symbols = int(input(f"How many symbols would you like?\n").strip())
nr_numbers = int(input(f"How many numbers would you like?\n").strip())
choices = []
password = ""
for i in range(nr_letters):
    choices.append(choice(letters))
for j in range(nr_symbols):
    choices.append(choice(symbols))
for k in range(nr_numbers):
    choices.append(choice(numbers))
print(choices)
shuffle(choices)
print(choices)
for i in range(len(choices)):
    password += choices[i]
print(f"Your password is {password}")
