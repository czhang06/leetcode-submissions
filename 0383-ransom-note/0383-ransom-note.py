class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for c in ransomNote:
            count1[ord(c) - ord('a')] += 1
        for c in magazine:
            count2[ord(c) - ord('a')] += 1
        
        for i in range(len(count1)):
            if count1[i] > count2[i]:
                return False
        return True