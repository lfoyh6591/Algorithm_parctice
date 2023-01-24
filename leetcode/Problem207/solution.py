class Solution:
    def dfs(self, graph, n, visited):
        if n in visited:
            return False
        if self.check[n]:
            return True

        visited.add(n)
        self.check[n] = True
        for x in graph[n]:
            if not self.dfs(graph, x, visited):
                return False
        visited.remove(n)

        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[]*numCourses for i in range(numCourses)]
        self.check = [False]*numCourses

        for prerequisite in prerequisites:
            a = prerequisite[0]
            b = prerequisite[1]

            graph[b].append(a)

        for i in range(numCourses):
            if self.check[i]:
                continue

            if not self.dfs(graph, i, set()):
                return False

        return True