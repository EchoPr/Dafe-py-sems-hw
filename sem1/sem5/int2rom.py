def intToRoman(num: int) -> str:
    trans = {
        1: (1, 0, 0),
        2: (2, 0, 0),
        3: (3, 0, 0),
        4: (1, 1, 0),
        5: (0, 1, 0),
        6: (1, 1, 0),
        7: (2, 1, 0),
        8: (3, 1, 0),
        9: (1, 0, 1)
    }

    holy_magic = (
        ('I', 'V', 'X'), ('X', 'L', 'C'),
        ('C', 'D', 'M'), ('M', '', '')
    )

    res = ''
    unit = 1000
    i = 3
    while i >= 0:
        int_part = num // unit
        if int_part != 0:
            if int_part <= 5:
                res += holy_magic[i][0] * trans[int_part][0] + holy_magic[i][1] *trans[int_part][1]
            elif 6 <= int_part <= 8:
                res += holy_magic[i][1] * trans[int_part][1] + holy_magic[i][0] *trans[int_part][0]
            else:
                res += holy_magic[i][0] + holy_magic[i][2]

        num %= unit
        i -= 1
        unit /= 10

    return res


if __name__ == "__main__":
    assert intToRoman(3) == "III"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(1994) == "MCMXCIV"
    assert intToRoman(3999) == "MMMCMXCIX"