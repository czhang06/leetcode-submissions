class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = defaultdict(list)
        need = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            need[a] += 1

        q = deque(c for c in range(numCourses) if need[c] == 0)
        result = []

        while q:
            c = q.popleft()
            result.append(c)
            for course in graph[c]:
                need[course] -= 1
                if need[course] == 0:
                    q.append(course)
                    
        
        return result if len(result) == numCourses else []
