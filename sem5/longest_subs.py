def lengthOfLongestSubstring(s: str) -> int:
    t = ''
    mp = dict(zip(s, [-1] * len(s)))
    mx = 0
    n = len(s)
    start = 0

    for i in range(len(s)):
        if mp[s[i]] != -1:
            mx = max(mx, len(t) - start)
            pos = mp[s[i]]

            start = max(pos + 1, start)
                
        t += s[i]
        mp[s[i]] = i

    mx = max(mx, len(t) - start)
    return mx
    

if __name__ == "__main__":
    assert lengthOfLongestSubstring('abcabcbb') == 3
    assert lengthOfLongestSubstring('bbbbb') == 1
    assert lengthOfLongestSubstring('pwwkew') == 3     # 'pwke' является подпоследовательностью, 
    assert lengthOfLongestSubstring('tmmzuxt') == 5  
    assert lengthOfLongestSubstring('bbtablud') == 6                                             # но не подсловом
