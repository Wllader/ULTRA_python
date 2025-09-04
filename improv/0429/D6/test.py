class Test:
    def __init__(self):
        self._text = "Výchozí text"

    @property
    def text(self):
        print("Teď čtu do vlastnosti text, pomocí skryté proměnné _text!")
        return self._text
    
    @text.setter
    def text(self, value):
        print("Teď dosazuji do vlastnosti text, pomocí skryté proměnné _text!")
        self._text = value

t = Test()

t.text = "Jiný než výchozí text"

print(
    t.text
)