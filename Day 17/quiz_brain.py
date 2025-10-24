class QuizBrain:
    def __init__(self, questionBank):
        self.questionNumber = 0
        self.score = 0
        self.questionBank = questionBank

    def nextQuestion(self):
        currentQuestion = self.questionBank[self.questionNumber]
        self.questionNumber += 1
        userAnswer = input(
            f"Q.{self.questionNumber}: {currentQuestion.text} (True/False)? "
        )
        self.checkAnswer(userAnswer, currentQuestion.answer)

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionBank)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correctAnswer}.")
        print(f"Your current score is: {self.score}/{self.questionNumber}\n")
