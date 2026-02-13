import ascii_art
import snowman
import random

def get_random_word():
    """Selects a random word from the list."""
    return snowman.WORDS[random.randint(0, len(snowman.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    #Display the snowman for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    #build a display version of the secret word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = 3

    print("Welcome to Snowman Meltdown!")
    #For now, display the initial game state.

    while mistakes < max_mistakes:
        saved = True
        display_game_state(mistakes, secret_word, guessed_letters)

        #Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in guessed_letters:
            print("You already had this letter")
            continue
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        for char in secret_word:
            if char not in guessed_letters:
                saved = False

        if saved:
            break

    if mistakes < max_mistakes:
        print(ascii_art.STAGES[mistakes])
        print("☃️ Yeahh, you saved the Snowman ☃️")
        print(f"The word was {secret_word}")
    else:
        print(ascii_art.STAGES[mistakes])
        print("Game Over! The Snowman melted :-(")
        print(f"The word was: {secret_word}")


play_game()