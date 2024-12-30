from src.romakan.mora import get_moras


def test_get_moras():
    assert get_moras("shou") == ["sho", "u"]


def test_moras2():
    assert get_moras("hataraku") == ["ha", "ta", "ra", "ku"]


def test_moras3():
    assert get_moras("dantan") == ["da", "n", "ta", "n"]


def test_moras4():
    assert get_moras("shou") == ["sho", "u"]


def test_moras5():
    assert get_moras("hataraku") == ["ha", "ta", "ra", "ku"]


def test_mora6():
    assert get_moras("isshouni") == ["i", "ssho", "u", "ni"]


def test_mora7():
    assert get_moras("jaa") == ["ja", "a"]


def test_mora8():
    assert get_moras("kaishyain") == ["ka", "i", "shya", "i", "n"]


def test_mora9():
    assert get_moras("koujou") == ["ko", "u", "jo", "u"]


def test_mora10():
    assert get_moras("byubipyu") == ["byu", "bi", "pyu"]


def test_mora11():
    assert get_moras("chotto") == ["cho", "tto"]


def test_mora12():
    assert get_moras("menma") == ["me", "n", "ma"]
