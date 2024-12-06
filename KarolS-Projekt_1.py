"""
KarolS-Projekt_1: První projekt do Engeto Online Python Akademie - Textový
analyzátor

author: Karol Seneši
email: senesi.charles@seznam.cz
discord: KarolS. (immaculate_gull_26453)
akademie: python-24-4-2024
"""
# Použijeme re modul ze standardní knihovny v Pythonu pro nahrání textů ze
# souboru tasks_template.py. Je možné i texty přímo zkopírovat do kódu jako 
# seznam (list).
import re
from task_template import TEXTS

# Registrovaní uživatelé a hesla
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Zadání přihlašovacích údajů
username = input("Username: ")
password = input("Password: ")

# Ověření uživatele, přivítání uživatele, zamítnutí uživatele u nesprávné
# kombinace username a password a ukončení programu
print("-" * 40)
if users.get(username) == password:
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
else:
    print("Unregistered user, terminating the program..")
    exit()

# Pokyn uživateli k zadání vybraného textu od 1 do 3, ukončení programu
# při zadání inputu mimo 1, 2 a 3
print("-" * 40)
try:
    choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
    if choice < 1 or choice > len(TEXTS):
        raise ValueError
except ValueError:
    print("Invalid input, terminating the program..")
    exit()

# Vybraný text
text = TEXTS[choice - 1]

# Analýza textu
words = re.findall(r'\b\w+\b', text)
titlecase_words = [word for word in words if word.istitle()]
uppercase_words = [word for word in words if word.isupper() and word.isalpha()]
lowercase_words = [word for word in words if word.islower()]
numeric_strings = [int(word) for word in words if word.isdigit()]
word_lengths = [len(word) for word in words]

# Výsledky analýzy
print("-" * 40)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {len(titlecase_words)} titlecase words.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric_strings)}")
print("-" * 40)

# Vytvoření sloupcového grafu
print(f"{'LEN':<3}| {'OCCURENCES':<20}|NR.")
print("-" * 40)
for length in sorted(set(word_lengths)):
    count = word_lengths.count(length)
    print(f"{length:<3}| {'*' * count:<20}|{count}")
print("-" * 40)
