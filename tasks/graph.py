from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def DFSUtil(self,v, visited,retur):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        retur.append(v)

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in v.outbound:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited,retur)

    def dfs(self) -> list[Node]:
        retur = []
        retur.append(self._root)
        visited = set()
        visited.add(self._root)
        for neighbour in self._root.outbound:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited,retur)
        return(retur)


    def bfs(self) -> list[Node]:
        visited = []  # List for visited nodes.
        queue = []
        visited.append(self._root)
        queue.append(self._root)

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)
            print(m, end=" ")
            for neighbour in m.outbound:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited



