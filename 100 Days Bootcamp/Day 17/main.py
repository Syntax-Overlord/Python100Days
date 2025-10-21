from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))
# print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.stillHasQuestions():
    quiz.nextQuestion()
print("\nYou've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}\n\n")
