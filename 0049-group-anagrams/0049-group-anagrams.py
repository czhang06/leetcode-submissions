class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = {}
        
        for s in strs:
            my_dict = {}
            for letter in s:
                if letter in my_dict:
                    my_dict[letter] += 1
                else:
                    my_dict[letter] = 1

            sorted_dict = tuple(sorted(my_dict.items()))
            if sorted_dict in result:
                result[sorted_dict].append(s)
            else:
                result[sorted_dict] = [s]
        
        r = []
        for val in result:
            r.append(result[val])
        return r