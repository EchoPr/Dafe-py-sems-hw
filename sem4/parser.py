def parse(
    string: str, valid_pairs: list[tuple[str, str]]
) -> list[str]:
    ans = []

    for v in valid_pairs:
        string = string.replace(v[0], v[0] + ' ')
        string = string.replace(v[1], ' ' + v[1])
    a = string.split()


    for i in range(1, len(a) - 1):
        if not a[i].isalpha(): continue

        if a[i - 1][-3:] == a[i + 1][0] + a[i + 1][2:4] and a[i + 1][1] == '/':
            ans.append(a[i])


    return list(set(ans))




string = (
    "</p><p><a>float</b></p><p><b>frozenset</b>"
    "</p><p><c>list</c></p><p><b>list</b>"
)
valid_pairs = [("<a>", "</a>"), ("<b>", "</b>"), ("<c>", "</c>")]

assert parse(string, valid_pairs) == ["frozenset", "list"]