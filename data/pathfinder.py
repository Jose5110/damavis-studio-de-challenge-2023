from collections import defaultdict, deque
from data.labyrinth import Labyrinth

labyrinth = Labyrinth('test_1')
array = labyrinth.array_generator()

def make_horizontal_graph(array):
    rows = len(array)
    cols = len(array[0])

    graph_horizontal = defaultdict(list)

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == '#':
                continue
            
            vertex = (i, (j,j+1,j+2))
            neighbors = []
            # Check neighboring vertices and add edges accordingly

            # Check above neighbor
            if i > 0 and array[i - 1][j] != '#':
                neighbors.append((i - 1, (j, j+1, j+2)))

            # Below neighbor
            if i < rows - 1 and array[i + 1][j] != '#':
                neighbors.append((i + 1, (j, j+1, j+2)))

            # Left neighbor
            if j > 0 and array[i][j - 1] != '#':
                neighbors.append((i, (j-1, j, j+1)))

            # Right neighbor
            if j+2 < cols - 1 and array[i][j + 3] != '#':
                neighbors.append((i, (j+1, j+2, j+3)))

            # Add edges for the current vertex
            for neighbor in neighbors:
                graph_horizontal[vertex].append(neighbor)

    return graph_horizontal

def make_vertical_graph(array):
    rows = len(array)
    cols = len(array[0])

    graph_vertical = defaultdict(list)

    for i in range(rows):
        for j in range(cols):
            if array[0][j] == '#' or array[0+1][j] == '#' or array[0+2][j] == '#':
                continue

            vertex = ((i,i+1,i+2), j)
            neighbors = []
            # This function is almost repeated for the sake of readability 

            # Check above neighbor
            if j > 0 and array[i][j - 1] != '#':
                neighbors.append(((i, i+1, i+2), j - 1))

            # Below neighbor
            if j < cols - 1 and array[i][j + 1] != '#':
                neighbors.append(((i, i+1, i+2), j + 1))

            # Left neighbor
            if i > 0 and array[i - 1][j] != '#':
                neighbors.append(((i-1, i, i-2), j))

            # Right neighbor
            if i+2 < rows - 1 and array[i + 3][j] != '#':
                neighbors.append(((i+1, i+2, i+3), j))

            # Add edges for current vertex
            for neighbor in neighbors:
                graph_vertical[vertex].append(neighbor)

    return graph_vertical

def breadth_first_search(graph, start, goal):
    queue = deque()
    # Start with the start vertex (initial position) and a path (the path starts with the initial position accounted for)
    queue.append((start, [start]))
    while queue:
        vertex, path = queue.popleft()
        
        # Found the goal, return the path
        if vertex == goal:
            return path  
        
        for neighbor in graph[vertex]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return -1 # No path found

h_graph = make_horizontal_graph(array)
v_graph = make_vertical_graph(array)

start = (0, (0, 1, 2))
goal = (len(array)-1,len(array[0])-1)

breadth_first_search(h_graph,start,goal)