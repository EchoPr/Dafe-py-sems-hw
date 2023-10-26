def parse(
    string: str, valid_pairs: list[tuple[str, str]]
) -> list[str]:
    ans = []

    for v in valid_pairs:
        string = string.replace(v[0], v[0] + ' ')
        string = string.replace(v[1], ' ' + v[1])
    a = string.split()

    vars = set()
    for i in range(1, len(a) - 1):
        if not a[i].isalpha(): continue

        if a[i - 1][a[i - 1].rfind('<') + 1:-1] == a[i + 1][a[i + 1].find('<') + 2:a[i + 1].find('>')] \
           and a[i + 1][1] == '/' or \
           a[i - 1][a[i - 1].rfind('<') + 2:-1] == a[i + 1][a[i + 1].find('<') + 1:a[i + 1].find('>')] \
           and a[i - 1][a[i - 1].rfind('<') + 1] == '/':
            if a[i] not in vars: ans.append(a[i])

    return ans


string = (
    "</a>this<a></b>is<b><a>good</a><c>example</c>"
)
valid_pairs =  [('<a>', '</a>'), ('</a>', '<a>'), ('</b>', '<b>'), ('<c>', '</c>')]
assert parse(string, valid_pairs) == ['this', 'is', 'good', 'example']