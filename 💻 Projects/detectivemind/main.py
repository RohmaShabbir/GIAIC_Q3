from player import Player
from case import Case
from story_loader import load_case

print("\U0001F575️ Welcome to DetectiveMind - Mystery Puzzle Game")
name = input("Enter Your name, Detective: ")
player = Player(name)
 
# Load a case from JSON
case = load_case("data/cases.json")

# Start the case
case.play(player)

print(f"\nCase Completed, {player.name}!")
print(f"Score: {player.score} / 100")
if player.solved:
    print("\U0001F3C6 You solve the case! Well done!")
else:
    print("❌ Wrong accusation. Better luck next time!")