DetectiveMind - Mystery Puzzle Game
Welcome to DetectiveMind! A CLI-based interactive mystery game where you play as a detective, solving clues and interrogating suspects to catch the criminal. The game is built using Object-Oriented Programming (OOP) principles in Python.

How to Play
Start by entering your name to play as a detective.

You will be given a case with clues, suspects, and a story.

Solve the clues and interact with the suspects.

Make your final guess to identify the criminal.

Your score is based on the number of clues solved and the correctness of your final guess.

detectivemind/
│
├── main.py              # Main game loop
├── player.py            # Player class (holds player name, score)
├── clue.py              # Clue class (handles clues and answers)
├── suspect.py           # Suspect class (handles interrogation)
├── case.py              # Case class (holds the case logic and flow)
├── story_loader.py      # Loads cases from JSON file
└── data/
    └── cases.json      # Stores case data (clues, suspects, story)

Game Features
Interactive Clues: Players solve riddles and logic puzzles to gain points.

Suspect Interrogation: Players interrogate suspects, with truth/lie detection.

Criminal Identification: Players make a guess about who the criminal is based on clues.

Scoring System: Players accumulate points by solving clues and correctly identifying the criminal.
