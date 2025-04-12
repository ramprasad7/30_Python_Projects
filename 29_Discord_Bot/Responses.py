from difflib import get_close_matches
import json


def get_best_match(user_question: str, questions: dict) -> str:
    questions: list[str] = [q for q in questions]
    matches: list[str] = get_close_matches(user_question,questions,n=1, cutoff=0.6)

    if matches:
        return matches[0]


def get_response(message: str, knowledge: dict) -> str | None:
    best_match: str = get_best_match(message,knowledge)

    if answer := knowledge.get(best_match):
        return answer

    else:
        return 'I don\'t understand, could you please repeat that.'


def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    knowledge: dict = load_knowledge('knowledge.json')
    print(get_response('He ll o', knowledge))