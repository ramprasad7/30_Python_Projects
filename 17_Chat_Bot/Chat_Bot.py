from difflib import get_close_matches

from sympy.codegen import While


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def chat_bot(knowledge: dict):
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "exit":
            break
        best_match: str | None = get_best_match(user_input,knowledge)

        if answer := knowledge.get(best_match):
            print(f"Bot: {answer}")

        else:
            print(f"Bot: I don't understand, can you rephrase it.")

def main():
    brain: dict = {"hello" : "Hey there!",
                   "how are you" : "I am good, thanks! how about you?",
                   "what time it is" : "I don\'t have clue!",
                   "bye" : "see you!"}
    print("Welcome to Chat Bot!")
    chat_bot(brain)


if __name__ == '__main__':
    main()