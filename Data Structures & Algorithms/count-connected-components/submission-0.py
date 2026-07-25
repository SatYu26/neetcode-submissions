from collections import defaultdict

class  Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(set)
        for i in range(n):
            adjList[i] = set()
        for a, b in edges:
            adjList[a].add(b)
            adjList[b].add(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adjList[node]:
                dfs(n)
            return
        c = 0
        for k in list(adjList.keys()):
            if k not in visited:
                dfs(k)
                c += 1
        return c