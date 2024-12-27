import random


class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.q_number = 0
        self.q_bank = q_list
        random.shuffle(self.q_bank)


    def has_finished(self):

        return self.q_number == len(self.q_bank)


    def _check_answer(self, q_answer, u_answer):

        if q_answer.lower() == u_answer.lower():
            self.score += 1
            print("That's correct!")
        else:
            print(f"That's wrong! The answer is {q_answer}")


    def next_question(self):

        question = self.q_bank[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {question.q_text} (True/False): ")
        self._check_answer(question.q_answer, user_answer)