from src.romakan.converter import Romakan

romakan = Romakan()


def test_converter1():
    assert romakan.convert_hiragana("syasin") == "しゃしん"


def test_converter2():
    assert romakan.convert_hiragana("issyouni") == "いっしょうに"


def test_converter3():
    assert romakan.convert_hiragana("isshyouni") == "いっしょうに"


def test_converter4():
    assert romakan.convert_hiragana("tyotto") == "ちょっと"
