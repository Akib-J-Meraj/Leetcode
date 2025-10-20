from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list and indegree map
        adj: dict[int, list[int]] = defaultdict(list)
        inDegree: dict[int, int] = {i: 0 for i in range(numCourses)}

        # Build the graph
        for edge in prerequisites:
            u = edge[1]  # prerequisite
            v = edge[0]  # course that depends on u
            adj[u].append(v)
            inDegree[v] += 1

        # Initialize queue with courses having no prerequisites
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        order = []

        # Perform Kahn's algorithm
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        # If we were able to take all courses, return the order
        if len(order) == numCourses:
            return order
        else:
            return []  # cycle detected → not all courses can be finished
