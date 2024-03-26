from math import inf, isinf


def jump(jumps: list[int]) -> int:
    n = len(jumps)
    dp = [0] + [inf] * (n - 1)

    for i in range(n):
        if jumps[i] <= 0: continue
        
        for j in range(1, min(jumps[i], n - i - 1) + 1):
            dp[i + j] = min(dp[i + j], dp[i] + 1)

    return dp[-1] if not isinf(dp[-1]) else -1


jumps = [1, 1, 2, 10, 0, -100, 2]
assert jump(jumps) == 4
