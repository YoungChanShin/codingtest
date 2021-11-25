def longestPalindrome(s):
    def slide(left: int, right: int):
        while -1 < left and right < len(s) and s[left] == s[right]:
            left -= 1
            right -= 1
        return s[left : right + 1]

    if len(s) < 2 or s == s[::-1]:
        return s
    max_str = s[0]
    for i in range(len(s) - 1):
        max_str = max(max_str, slide(i, i + 1), slide(i, i + 2), key=len)

    return max_str


s = "babad"

print(longestPalindrome(s))