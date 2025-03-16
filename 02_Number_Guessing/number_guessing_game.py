from random import randint

MAX_TRIES: int = 3

def main() -> None:
    lower_num, higher_num = 1, 10
    random_numer: int = randint(lower_num, higher_num)

    print(f"Guess the number in range from {lower_num} to {higher_num}.")

    tries: int = 1

    while tries <= MAX_TRIES:
        try:
            user_guess: int = int(input("Guess: "))

        except ValueError as e:
            print("Please Enter a valid number.")
            continue
        if user_guess > random_numer:
            print("Number is lower")
        elif user_guess < random_numer:
            print("Number is higher")
        else:
            print("You Guessed Correct!")
            break
        print(f"{MAX_TRIES - tries} Tries remaining.")
        tries += 1

if __name__ == "__main__":
    main()