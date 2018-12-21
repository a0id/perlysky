import json

class Switch():
    def __init__(self, text):
        self.text = text.lower()
        self.phrases = { }
        self.load()
    def load(self):
        with open("static/phrases.json", "r") as f:
            self.phrases = json.loads(f.read())
        self.phrases = self.phrases["phrases"]
    def switch(self):
        for phrase in self.phrases:
            self.text = self.text.replace(phrase.lower(), phrase[phrase])
        return self.text