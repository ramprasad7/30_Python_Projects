from dataclasses import dataclass
from textblob import TextBlob


@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text:str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('😊', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😠', polarity)

    else:
        return Mood('😐', polarity)


def run_bot():
    print("Enter some text to get a sentiment analysis back: ")
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "exit":
            break
        mood: Mood = get_mood(user_input, sensitivity=0.4)
        print(f"Bot: {mood.emoji}, {mood.sentiment}")

def main() -> None:
    run_bot()

if __name__ == '__main__':
    main()