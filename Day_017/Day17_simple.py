# class User:

#     def __init__(self, user_id, username):  # constructor
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# user_1 = User("001", "hj")
# user_2 = User("002", "jack")
# print(user_1.followers)

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_bank.append(
        Question(question["question"], question["correct_answer"]))
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've complated to quiz")
print(f"Your final score was: {quiz.score}/ {quiz.question_number}")
