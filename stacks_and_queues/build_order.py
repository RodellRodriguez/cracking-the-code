'''
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
'''
'''
a d
b d
c
d c
e
f b, a

We can do a topological sort to solve this problem

1. Determine num of total nodes
2. Identify all nodes with 0 incoming edges (these are all the possible starting points of a graph)
and add them to our final topological sorted array
3. For each node identified from the previous step, remove their outbound edges from the graph
    - This means delete the key of each node from the adjacency list
4. Repeat steps 2 and 3 until no more nodes can be identified in step 2
5. If resulting sorted list is the same size as the size determined in step 1 then
we have a valid build order else this sort has failed due to a cycle
'''

def build_order(projects, dependencies):
    adjacency_list = build_adjacency_list(projects, dependencies)
    build_order = []
    while True:
        values = list(adjacency_list.values())
        incoming_edge_nodes = []
        for nodes in values:
            incoming_edge_nodes += nodes # Flatten nested neighbors list

        zero_incoming_edge_nodes = []
        for node in adjacency_list.keys():
            if node not in incoming_edge_nodes:
                zero_incoming_edge_nodes.append(node)
        if zero_incoming_edge_nodes == []:
            break
        else:
            build_order += zero_incoming_edge_nodes
            for node in zero_incoming_edge_nodes:
                adjacency_list.pop(node)

    if len(build_order) == len(projects):
        return build_order
    raise RuntimeError("No build order exists for these projects.")

def build_adjacency_list(projects, dependencies):
    adjacency_list = {project: [] for project in projects}
    for node, neighbor in dependencies:
        adjacency_list[node].append(neighbor)
    return adjacency_list


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

print(build_order(projects, dependencies))
