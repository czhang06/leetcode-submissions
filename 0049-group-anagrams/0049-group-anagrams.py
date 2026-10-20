
class Solution(object):
    def groupAnagrams(self, strs):
        result = {}

        for s in strs:
            counts = [0] * 26

            for letter in s:
                counts[ord(letter) - ord('a')] += 1

            key = tuple(counts)

            if key not in result:
                result[key] = []

            result[key].append(s)

        return list(result.values())
