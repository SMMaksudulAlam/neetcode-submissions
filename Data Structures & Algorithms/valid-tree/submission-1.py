class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = {}
        for e in edges:
            i = e[0]
            j = e[1]
            if(dic.get(i)==None):
                dic[i] = []
            dic[i].append(j)
            if(dic.get(j)==None):
                dic[j] = []
            dic[j].append(i)
        
        visited = {}
        track_edges = {}
        res = []
        def dfs(n):
            visited[n] = 1
            if(dic.get(n)!=None):
                lst = dic[n]
                for e in lst:
                    if(visited.get(e)==None):
                        track_edges[(n, e)]=1
                        r = dfs(e)
                        if(not r):
                            return False
                    elif(track_edges.get((e, n))!=None):
                        pass
                    else:
                        return False
            res.append(n)
            return True

        r = dfs(0)
        if(r and len(res)==n):
            return True
        return False

            

        