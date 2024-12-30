import json

from .mora import get_moras


def get_hiragana():
    with open("source/hiragana.json", encoding="utf-8") as f:
        return json.load(f)


class Romakan:

    def __init__(self):
        self.hiragana = get_hiragana()

    def convert_hiragana(self, word: str) -> str:
        moras = get_moras(word)
        result = ""
        for mora in moras:
            if len(mora) > 2:
                if mora[0] == mora[1]:  # double symbol
                    result += "っ"
                    mora = mora[1:]
            result += self.hiragana[mora]
        return result
