import random
import sys

class RPS:

    def __init__(self):
        print("Welcome to RPS 69!")

        self.moves: dict = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input("Rock, Paper or Scissors? >> ").lower()

        if user_move == "exit":
            print("Thanks for Playing!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid Move..")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move,ai_move)
        self.check_move(user_move,ai_move)


    def display_moves(self, user_move: str, ai_move: str):
        print("------------")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")

    def check_move(self,user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's A Tie")
        elif user_move == "rock" and ai_move == "scissors":
            print("You Won!")
        elif user_move == "scissors" and ai_move == "paper":
            print("You Won!")
        elif user_move == "paper" and ai_move == "rock":
            print("You Won!")
        else:
            print("AI wins!")


if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()