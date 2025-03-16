from random import choice

def run_game():
    word: str = choice(["apple", "secret", "banana"])
    user_name: str = input("What is your Name? ")
    print(f"Welcome to Hangman, {user_name}!")

    guessed: str =''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word= ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print("_", end='')
                blanks += 1

        print()  #Adds a black new line

        if blanks ==0:
            print("You got it!")
            break

        guess: str = input("Enter a letter: ")
        if guess in guessed:
            print(f"You have already guessed: {guess}, Please try with different letters!")
            continue

        guessed += guess
        if guess not in word:
            tries -= 1
            print(f"Sorry, that ws wrong.. ({tries} remaining)")
            if tries == 0:
                print("No More tries remaining, You Lose!")
                break

if __name__ == "__main__":
    run_game()

