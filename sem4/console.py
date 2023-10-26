def lev(a: str, b: str) -> int:
    n, m = len(a), len(b)

    if n > m:
        a, b = b, a
        n, m = m, n

    cur = [x for x in range(n + 1)]
    for i in range(1, m + 1):
        prev, cur = cur, [i] + [0] * n

        for j in range(1, n + 1):
            f = 0
            if a[j - 1] != b[i - 1]: f = 1

            cur[j] = min(
                prev[j] + 1,
                cur[j - 1] + 1,
                prev[j - 1] + f
            )
    
    return cur[n]



def check_comand(user_comand: str, comands: list[str]) -> bool:
    if user_comand in comands:
        return True

    cnt = 0
    for c in comands:
        if lev(c, user_comand) <= 1:
            cnt += 1
    if cnt != 1:
        return False 
        
    return True


assert check_comand('gt', ['cd', 'ls', 'git']) 
assert not check_comand('gt', ['cd', 'ls', 'git', 'get'])
assert not check_comand("getting", ['cd', 'ls', 'git', 'get'])
assert check_comand("get", ['cd', 'ls', 'git', 'get'])
assert check_comand("wget", ['cd', 'ls', 'get', 'wget'])
assert not check_comand("rm", ['cd', 'ls', 'git', 'wget'])