import random



def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []

    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main() -> None:
    while True:
        try:
            user_input: str = input("Enter dice would you like roll? ")

            if user_input.lower() == 'exit':
                print("Thanks for Playing!")
                break

            result = roll_dice(int(user_input))
            print(*result, sep=", ")
            total: int = 0
            for num in result:
                total += num
            print(f"Total Dice Value = {total}")

        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()