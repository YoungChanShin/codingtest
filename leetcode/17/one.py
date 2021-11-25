class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        answer = []

        phone_book = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def recur(word, cur):
            if cur == len(digits):
                answer.append(word)
                return
            for l in phone_book[digits[cur]]:
                recur(word + l, cur + 1)

        recur("", 0)
        return answer
