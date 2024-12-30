def get_moras(word: str):
    """
    Get moras list from
    """
    glas = ["a", "i", "u", "e", "o"]
    moras = []
    indx = 0
    mora = ""
    while indx < len(word):
        if mora == "n" and word[indx] not in glas:
            moras.append(mora)
            mora = word[indx]
        else:
            mora += word[indx]
        if mora[-1] in glas:
            moras.append(mora)
            mora = ""
        indx += 1
    if mora != "":
        moras.append(mora)
    return moras
