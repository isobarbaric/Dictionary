
class Variant:

    def __init__(self, text, part_of_speech: str, definition: list):
        self.text = text 
        self.part_of_speech = part_of_speech
        self.defn = definition

    def __repr__(self):
        # return "(" + self.part_of_speech + ") : " + self.defn 
        return self.defn
