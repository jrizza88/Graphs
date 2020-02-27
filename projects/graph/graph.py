"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        #pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #self.vertices[v1].add(v2)
        # this helps to check
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exists")
        #pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
    ## This whole thing takes the FIFO idea! First in First Out
        #pass  # TODO
        # algorithm 
        # they will not hold true? necessarily
        # algorithm will hold true!

        ## Create an empty queue and enqueue the starting vertex ID
        q = Queue()

        q.enqueue(starting_vertex)
        ## Create an empty Set to store visited nodes/verticies
        visited = set()
        # visited = {1}
        # visited = {1, 2}
        ## While the queue is not empty...
        while q.size() > 0: 
            # Dequeue the first vertex
            current_node = q.dequeue()
            # If that vertex has not been visited...
            if current_node not in visited:
                # Mark it as visited.
                print(current_node)
                visited.add(current_node)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[current_node]:
                    q.enqueue(neighbor)

                # ALT way to get neighbors and then put them in lines:
                ## and get its neighbors
                #edges = self.get_neighbors(current_node)
                ## put them in line to be visited
                #for edge in edges:
                 #   queue.enqueue(edge)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        ## Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        ## make a set for the visited vertices
        visited = set()
        ## While the stack is not empty... we have more ppl to visit
        while s.size() > 0: 
            # Pop the first vertex
            v = s.pop()
            # Check if the vertex has been visited...
            if v not in visited:
                # Mark it as visited.
                print(v)
                visited.add(v)
                # Then add all of its neighbors (push) to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        #pass  # TODO

        ## why can't we do bft recursively?

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(vertex)

        edges = self.get_neighbors(vertex)


        if len(edges) == 0:
            return

        else:
            for edge in edges:
                if edge not in visited:
                    self.dft_recursive(edge, visited)
                else:
                    return


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # make a queue
        queue = Queue()
        # make a set for visited
        visited = set()
        # enqueue A PATH TO the starting_vertex
        queue.enqueue([starting_vertex])
        # while the queue isn't empty:
        while queue.size() > 0:
        ## dequeue the next path

            path = queue.dequeue()
            ## current_node is the last thing in the path
            ## -1 helps to get the last instance from path
            current_node = path[-1]
            ## check if it's the target, aka the destination_vertex
            ## if so, return the path!!
            ## -1 helps to get the last instance
            if current_node == destination_vertex:
                print('when current node = destination', path)
                return path

        ## if not, mark this as visited
            if current_node not in visited:
                visited.add(current_node)
        ## get the neighbors
                edges = self.get_neighbors(current_node)
        ## copy the path, add the neighbor to the copy
               # copy_path = self.get_neighbors(current_node)
               # copy_path.add(path)
        ## for each one, add a PATH TO IT to our queue
                for edge in edges:
                    
                    copy_path = path.copy()
                    ## alt way copy_path = len(path)
                    copy_path.append(edge)
                    queue.enqueue(copy_path)
        return 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        visited = set()
        
        stack.push([starting_vertex])

        while stack.size() > 0:

            path = stack.pop()

            current_node = path[-1]

            if current_node == destination_vertex:
                return path
            
            if current_node is not visited:
                visited.add(current_node)

                edges = self.get_neighbors(current_node)

                for edge in edges:
                    current_path = path[:]
                    current_path.append(edge)
                    stack.push(current_path)
        return 

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = []

        visited.add(starting_vertex)
        
        path = path + [starting_vertex]  
        #path += [starting_vertex]


        if starting_vertex == destination_vertex:
            return path

        edges = self.get_neighbors(starting_vertex) 
        if len(edges) == 0:
            return

        for edge in edges:
            if edge not in visited:
                new_edge = self.dfs_recursive(edge, destination_vertex, visited, path)
                print('dfs recurisve: ', new_edge )
                if new_edge:
                    return new_edge
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(graph.bft(1))
    graph.bft(1)
  

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('graph.dft(1): ', graph.dft(1))
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print('recursion', graph.dfs_recursive(1, 6))
    