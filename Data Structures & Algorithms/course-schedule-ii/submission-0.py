class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(numCourses)}

        for (u, v) in prerequisites:
            graph[u].add(v)
        
        visited = set()
        path = set()
        ans = []

        def topo_sort(c):
            if(c in visited):
                return True
            if(c in path):
                return False
            path.add(c)

            prerq = graph[c]
            for p in prerq:
                if(not topo_sort(p)):
                    return False
            
            path.remove(c)
            visited.add(c)
            ans.append(c)
            return True
        
        for i in range(numCourses):
            if(i not in visited):
                if(not topo_sort(i)):
                    return []
        return ans
