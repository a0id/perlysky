import json

class Switch():
    def __init__(self, text):
        self.text = self.process(text)
        self.phrases = { }
        self.load()
    def process(self, text):
        text = text.lower()
        text = text.replace(",", "")
        text = text.replace("'", "")
        text = text.replace(".", "")
        return text
    def load(self):
        with open("static/phrases.json", "r") as f:
            self.phrases = json.loads(f.read())
    def switch(self):
        for phrase in self.phrases:
            self.text = self.text.replace(phrase.lower(), self.phrases[phrase])
        return self.text