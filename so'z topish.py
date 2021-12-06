import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word=get_word()
    word_letters = set(word)
    user_letters = ' '
    print(f"Mен {len(word)} хонали сўз ўйладим. Топингчи?")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Шу вактгача киритган харфларингиз: {user_letters}")
        letter = input("Харф киритинг: ".upper())
        if letter in user_letters:
            print("Бу харфларни олдин киритгансиз бошка харф киритинг")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} харфи тўгри.")
        else:
            print("Бундай харф йўк.")
        user_letters += letter
    print(f"Табриклайман {word} сўзини {len(user_letters)} та уриниш билан топдингиз")
play()
