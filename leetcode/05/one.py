def longestPalindrome(s: str) -> str:
    theStart = -1
    theEnd = -1
    max_len = -1

    def isPal(l, r):
        for i in range((r - l + 1) // 2):
            if s[l + i] is not s[r - i]:
                return False
        return True

    for start in range(len(s) - 1):
        for end in range(start + 1, len(s)):
            if end - start > max_len:
                if isPal(start, end):
                    theStart = start
                    theEnd = end
                    max_len = end - start + 1
    return s[theStart : theEnd + 1]
