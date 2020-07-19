from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vertices=numCourses
        graph=defaultdict(list)
        flag=1

        for k,v in prerequisites:
            graph[v].append(k)
        def topologicalSort(v,visited_vertices,main_stack):
            visited_vertices[v] = True
            for i in graph[v]:
                if visited_vertices[i] == False:
                    topologicalSort(i,visited_vertices,main_stack)
            main_stack.insert(0,v)

        def CyclicTest(v, visited_vertices, main_stack):
            visited_vertices[v] = True
            main_stack[v] = True
            for i in graph[v]:
                if visited_vertices[i] == False:
                    if CyclicTest(i, visited_vertices, main_stack) == True:
                        return True
                elif main_stack[i] == True:
                    return True
            main_stack[v] = False
            return False

        visited_vertices = [False] * vertices
        main_stack = [False] * vertices
        for node in range(vertices):
            if visited_vertices[node] == False:
                if CyclicTest(node, visited_vertices, main_stack) == True:
                    flag=0
        if flag!=0:
            visited_vertices = [False] * vertices
            main_stack = []
            for i in range(vertices):
                if visited_vertices[i] == False:
                    topologicalSort(i, visited_vertices, main_stack)
            return main_stack
        else:
            return []



if __name__=="__main__":
    output=Solution().findOrder(4,[[0, 1], [3, 1], [1, 3], [3, 2]])
    print(output)
