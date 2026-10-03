class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for (u, v) in prerequisites:
            if(u not in graph):
                graph[u] = set()
            graph[u].add(v)
        
        ans = []
        completed = set()
        path = set()

        def topo(c):
            if(c in completed):
                return True
            if(c in path):
                return False
            
            path.add(c)

            pre = graph.get(c, set())
            for p in pre:
                if(topo(p) == False):
                    return False
            ans.append(c)
            completed.add(c)
            path.remove(c)
            return True
        
        for i in range(numCourses):
            if(i not in completed):
                if(topo(i) == False):
                    return []
        
        return ans
