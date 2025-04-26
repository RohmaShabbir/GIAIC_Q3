import json
from case import Case
from clue import Clue
from suspect import Suspect

def load_case(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        case_data = data["cases"][0]  # Load the first case

        clues = [Clue(c["question"], c["answer"], c["points"]) for c in case_data["clues"]]
        suspects = [Suspect(s["name"], s["statement"], s["is_lying"]) for s in case_data["suspects"]]

        return Case(case_data["title"], clues, suspects, case_data["criminal"])