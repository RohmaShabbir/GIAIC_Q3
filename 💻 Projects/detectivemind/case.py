from clue import Clue
from suspect import Suspect

class Case:
    def __init__(self, title, clues, suspects, criminal):
        self.title = title
        self.clues = clues
        self.suspects = suspects
        self.criminal = criminal

    def play(self, player):
        print(f"\nYour case: \"{self.title}\"\n")

        for clue in self.clues:
            points = clue.ask()
            player.add_score(points)

        for suspect in self.suspects:
            suspect.interrogate()

        print("\nWho is the criminal?")
        for i, suspect in enumerate(self.suspects):
            print(f"[{i+1}] {suspect.name}")

        guess = int(input("\nYour guess (enter number): "))
        if self.suspects[guess - 1].name == self.criminal:
            print("\n🎯 Your guess right!")
            player.solved = True
            player.add_score(30)
        else: 
            print(f"\nWrong guess! The criminal was {self.criminal}")