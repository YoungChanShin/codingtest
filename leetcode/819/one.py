from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_count = Counter()
        en = ""
        for l in paragraph:
            if l.isalpha():
                en += l.lower()
            elif en != "":
                if en not in banned:
                    words_count[en] += 1
                en = ""
        if en is not "" and en not in banned:
            words_count[en] += 1
        return words_count.most_common(1)[0][0]
