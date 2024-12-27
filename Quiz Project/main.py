from data import data
from question_model import Question
from quiz_brain import QuizBrain


q_deck = []

for q_item in data["results"]:
    q_text = q_item["question"]
    q_answer = q_item["correct_answer"]
    q_deck.append(Question(q_text, q_answer))

quiz = QuizBrain(q_deck)


if __name__ == "__main__":

    while not quiz.has_finished():
        quiz.next_question()
        print(f"Score {quiz.score}/{quiz.q_number}")