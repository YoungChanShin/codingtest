class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        answer = []

        phone_book = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def recur(word, cur):
            if cur == len(digits):
                answer.append(word)
                return
            for l in phone_book[digits[cur]]:
                recur(word + l, cur + 1)

        recur("", 0)
        return answer
