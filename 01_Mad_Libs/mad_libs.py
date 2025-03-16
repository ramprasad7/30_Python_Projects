def get_userinput(word_type: str) -> str:
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


def main() -> None:
    noun1: str = get_userinput("noun")
    verb1: str = get_userinput("verb")
    noun2: str = get_userinput("noun")
    verb2: str = get_userinput("verb")

    story: str = f"""
    A {noun1} {verb1} high above the mountains. The {noun2} is clear, with no clouds in sight. 
    It soars effortlessly, wings cutting through the air. 
    Suddenly, a gust of wind pushes the {noun1} off course. 
    It struggles to regain balance, but then it {verb2}, fluttering toward the ground. 
    For a moment, everything is still. The {noun1} lands softly on the grass, unharmed. 
    Looking up, it sees the vast {noun2}, waiting for its next flight. With a deep breath, 
    the {noun1} flaps its wings and rises once more. The {noun2} is endless, 
    and the adventure continues.
    """

    print(story)

if __name__ == "__main__":
    main()