import json

class Add():
    def __init__(self, perly, english):
        new_phrase = { perly: english }
        with open("static/phrases.json") as f:
            self.data = json.load(f)
        self.data.update(new_phrase)

        print(self.data)
        with open("static/phrases.json", "w") as f:
            # f.write(str(self.data))
            json.dump(self.data, f, indent=4)
