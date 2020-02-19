from util import Queue
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    
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

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        print('graph add 0', graph.add_vertex(pair[0]))
        print('graph add 1', graph.add_vertex(pair[1]))
        # added in reverse order (because of the test case)
        graph.add_edge(pair[1], pair[0])
   
    q = Queue()

    q.enqueue([starting_node])

    #visited = set()
    ancestor_length = 1
    # returning -1 if there is no further path(root ancestor)
    root_ancestor = -1

    while q.size() > 0:
        # dequeue the next path
        node_path = q.dequeue()

        # getting the last instance of the path 
        value = node_path[-1]

        if value < root_ancestor or len(node_path) > ancestor_length:
            print('node_path', node_path)
            root_ancestor = value
            ancestor_length = len(node_path)
            print(' root_ancestor: ', root_ancestor)
            print('value root_ancestor: ', value)
        # edge is the same as neighbor
        for edge in graph.vertices[value]:
            path = node_path[:]
            path.append(edge)
            q.enqueue(path)
            print('path', path)

    print(root_ancestor)
    return root_ancestor 
    

       