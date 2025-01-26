from flask import session

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        try:
            user_answer = float(user_answer.strip())
        except:
            ValueError

        if user_answer == self.answer:
            return True
        else: 
            session['tries_left'] -= 1
            return False
    
    @property
    def tries_left(self):
        return session.get('tries_left')