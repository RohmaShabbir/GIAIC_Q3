class Clue:
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer.lower()
        self.points = points

    def ask(self):
        print(f"Clue: {self.question}")
        user_input = input("> ").lower()
        if user_input == self.answer:
            print("✔ Correct!")
            return self.points
        else:
            print(f"❌ Incorrect! Correct answer: {self.answer}")
            return 0 