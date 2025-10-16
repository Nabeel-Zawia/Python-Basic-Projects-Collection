from question_model import quetion
from data import question_data
from quiz_brain import QuizBrain

quetions = question_data

quetion_bank=[]

for text in quetions:
    quetion_text = text["text"]
    quetion_answer = text["answer"]
    new_q = quetion(q_text=quetion_text,q_answer=quetion_answer)
    quetion_bank.append(new_q)

quiz = QuizBrain(quetion_bank)

while quiz.still_has_quetions():

    quiz.next_quetion()