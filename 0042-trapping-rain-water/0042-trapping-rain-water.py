class Solution:
    def trap(self, height: list[int]) -> int:
        ltr = [height[0]]
        for i in range(1, len(height)):
            ltr.append(max(ltr[-1], height[i]))
        
        result = 0
        msf = height[-1]
        for i in range(len(height) - 2, 0, -1):
            msf = max(msf, height[i])
            result += min(ltr[i], msf) - height[i]
            
        
        return result