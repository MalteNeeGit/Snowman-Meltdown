import ascii_art
import snowman
import random

#ANSI COLORS:
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
LIGHT_RED = "\033[1;31m"
END = "\033[0m"

def get_random_word():
    """Selects a random word from the list."""
    return snowman.WORDS[random.randint(0, len(snowman.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    #Display the snowman for the current number of mistakes.
    print("\n" + "❄️" * 15)
    print(ascii_art.STAGES[mistakes])
    #build a display version of the secret word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print()
    print("❄️" * 15 + "\n")

def input_validation(guessed_letters):
    while True:
        user_input = input(f"{CYAN}Guess a letter: {END}").lower().strip()

        if len(user_input) != 1:
            print(f"{LIGHT_RED}Please enter a single letter{END}")
        elif not user_input.isalpha():
            print(f"{LIGHT_RED}We need letters, try any from A - Z{END}")
        elif user_input in guessed_letters:
            print(f"{LIGHT_RED}You already had this letter{END}")
            continue
        else:
            return user_input


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = 3

    print(f"{CYAN}Welcome to Snowman Meltdown!{END}")

    while mistakes < max_mistakes:
        saved = True
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input_validation(guessed_letters)
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            print(f"{guess} {LIGHT_RED}is not in the word we are looking for{END}")
            mistakes += 1

        for char in secret_word:
            if char not in guessed_letters:
                saved = False

        if saved:
            break

    if mistakes < max_mistakes:
        print(ascii_art.STAGES[mistakes])
        print(f"☃️ {GREEN}Yeahh, you saved the Snowman{END} ☃️")
        print(f"{GREEN}The word was:{END} {secret_word}")

    else:
        print(ascii_art.STAGES[mistakes])
        print(f"{LIGHT_RED}Game Over! The Snowman melted :-({END}")
        print(f"{LIGHT_RED}The word was:{END} {secret_word}")

def ask_to_play_again():
    while True:
        choice = input(f"\n{CYAN}Would you like to play again?{END} {GREEN}(y/n): {END}").lower().strip()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print(f"{CYAN}Please enter 'y' for Yes or 'n' for No. {END}")


def main():
    while True:
        # Start first round:
        play_game()

        #if Game is finished, ask to play again
        if not ask_to_play_again():
            print(f"{GREEN}Thanks for playing Snowman Meltdown! Goodbye! ☃️👋{END}")
            break


if __name__ == "__main__":
    main()