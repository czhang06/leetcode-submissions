class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        need = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            need[a] += 1

        q = deque(c for c in range(numCourses) if need[c] == 0)
        taken = 0

        while q:
            c = q.popleft()
            taken += 1
            for course in graph[c]:
                need[course] -= 1
                if need[course] == 0:
                    q.append(course)
                    
        
        return taken == numCourses

            