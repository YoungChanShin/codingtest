class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = dict()
        for w in strs:
            key = "".join(sorted(list(w)))
            if key in counts.keys():
                counts[key].append(w)
            else:
                counts[key] = [w]

        return list(counts.values())