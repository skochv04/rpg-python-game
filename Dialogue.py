import json


# można wyciągać text z jsona, który znajduje się w folderze NPC z odpowiednim ID, logika parsowania podobna jak z
# Spritesheet
class Dialogue:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as f:
            self.data = json.load(f)
        f.close()

    def parse_text(self, dialogue):
        text = self.data['dialogues'][dialogue]['text']
        responses = self.data['dialogues'][dialogue]['responses']

        return text, responses
