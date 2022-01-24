def solution(name):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    name_manipul = list(map(lambda x: min([alphabet.index(x), 26 - alphabet.index(x)]),
                            list(name)))
    if len(name) == 1:
        return name_manipul[0]

    length = len(name) - 1
    idx = 1

    for i in range(1, len(name)):
        if "A" * i in name[1:]:
            idx = name.find("A" * i, 1)
        else:
            length = i - 1
            break

    if idx - 1 <= len(name) - idx - length:
        rev = 2 * (idx - 1) + (len(name) - idx - length)
    else:
        rev = (idx - 1) + 2 * (len(name) - idx - length)

    return sum(name_manipul) + min(rev, len(name) - 1)


