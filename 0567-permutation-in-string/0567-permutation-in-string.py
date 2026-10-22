class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for s in s1:
            count1[ord(s) - ord('a')] += 1
        
        l = 0
        
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1 == count2:
            return True
        r = len(s1) - 1
        while r < len(s2) - 1:
            r += 1
            count2[ord(s2[r]) - ord('a')] += 1
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if count1 == count2:
                return True
        return False