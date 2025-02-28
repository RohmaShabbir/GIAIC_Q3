import random

print("\n🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 50 and 100. You have 5 chances.\n")

# Random number generate karna
number_to_guess = random.randint(50, 100)
chances = 5

for attempt in range(1, chances + 1):
    user_guess = input(f"Attempt {attempt}/{chances} - Enter your guess: ")

    # Input validation
    if not user_guess.isdigit():
        print("❌ Invalid input! Please enter a number.\n")
        continue

    user_guess = int(user_guess)

    if user_guess == number_to_guess:
        print(f"✅ Congratulations! You guessed the number {number_to_guess} in {attempt} attempts! 🎉")
        break
    elif user_guess < number_to_guess:
        print("🔼 Too low! Try a higher number.\n")
    else:
        print("🔽 Too high! Try a lower number.\n")

# After the game is over or Loss
if user_guess != number_to_guess:
    print(f"\n😞 Game Over! The correct number was {number_to_guess}. Better luck next time!")

