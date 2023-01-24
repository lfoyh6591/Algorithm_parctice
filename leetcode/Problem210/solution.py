class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for i in range(numCourses)]
        check = [0]*numCourses
        dic = {}
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            check[prerequisite[0]] += 1
        
        for i in range(numCourses):
            l = dic.get(check[i], [])
            l.append(i)
            dic[check[i]] = l

        ret = []

        while len(ret) != numCourses:
            if not dic.get(0, []):
                return []

            roots = dic[0]
            for root in roots:
                dic[0].remove(root)
                ret.append(root)
                nexts = graph[root]
                for n in nexts:
                    dic[check[n]].remove(n)
                    check[n] -= 1
                    l = dic.get(check[n], [])
                    l.append(n)
                    dic[check[n]] = l

                graph[root] = []
            

        return ret