import random

def update_guess(current_guess,word):
    guess = ""
    for i in range(len(word)):
        if word[i] != " ":
            if len(current_guess)>0 and current_guess[i] != "_":
                guess+=word[i]
            else:
                guess+="_"
        else:
            guess += " "
    return guess

def guess_letter(letter,word_to_check,guess):
    letter_match = False
    for i in range(len(word_to_check)):
        if word_to_check[i] == letter:
            letter_match = True
            guess_list = list(guess)
            guess_list[i] = letter
            guess = "".join(guess_list)
    return guess, letter_match

def validate_guess(guess):
    for i in range(len(guess)):
        if guess[i] == "_":
            return False
    return True

max_lives = 6
current_lives = max_lives

HANGMAN_PICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORD_BANK = ["whale","tornado","apple","store","gate","ice cream","big castle","red dragon"]
word = WORD_BANK[random.randint(0,len(WORD_BANK)-1)]

current_guess = ""
current_guess = update_guess(current_guess,word)

is_game_over = False

while not is_game_over:
    print("****************************************",current_lives,"/",max_lives," LIVES LEFT****************************************")
    print("Word to guess: ", current_guess)
    guessed_letter = input("Guess a letter : ")
    current_guess, is_valid = guess_letter(guessed_letter,word,current_guess)
    is_game_over = validate_guess(current_guess)
    if is_game_over:
        print(f"Congratulations! You found the word {current_guess}")

    if not is_valid:
        print(f"You guess {guessed_letter}, that's not in the word. You lose a life.")
        current_lives -= 1
        is_game_over = current_lives<=0
        print(f"Game over. The word was {word}")
    else:
        print(f"You guess {guessed_letter}, that's right!")
    print(HANGMAN_PICS[current_lives])




