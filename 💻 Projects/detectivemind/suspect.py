class Suspect:
    def __init__(self, name, statement, is_lying):
        self.name = name
        self.statement = statement
        self.is_lying = is_lying

    def interrogate(self):
        print(f"\nInterrogating {self.name}...")
        print(f"\"{self.statement}\"")
        print("Truth Detector:", "⚠️ Possibly Lying" if self.is_lying else "✅ Seems Truthful")