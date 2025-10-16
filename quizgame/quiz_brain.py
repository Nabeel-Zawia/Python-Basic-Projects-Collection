class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0
    def still_has_quetions(self):
        number_left = len(self.question_list)
        return self.question_number < number_left 

         
    def next_quetion(self):
        current_quetion = self.question_list[self.question_number]
        self.question_number +=1
        user_answer=input(f"Q.{self.question_number}{current_quetion.text} (True/False): ")
        self.check_answer(user_answer,current_quetion.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You got it right!")
            
        else:
            print("Thats wrong.")
        print(f"the correct answer was: {correct_answer}")
        print(f"Your score is : {self.score} / {self.question_number}")
        print("\n")
        if self.still_has_quetions() == False:
            print(f"your final score is : {self.score} / {self.question_number}")