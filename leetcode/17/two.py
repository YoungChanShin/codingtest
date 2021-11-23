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
            for l in phone_book[digits[cur]]:
                if cur == len(digits) - 1:
                    answer.append(word + l)
                    continue
                recur(word + l, cur + 1)

        recur("", 0)
        return answer
