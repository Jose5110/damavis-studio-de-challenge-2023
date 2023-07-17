from collections import defaultdict, deque

def make_horizontal_graph(array):
    rows = len(array)
    cols = len(array[0])

    graph_horizontal = defaultdict(list)

    for i in range(rows):
        for j in range(cols):
            if (array[i][j] == '#') or (array[i][j] if j > cols-3 else False):
                continue
            
            # Check if any coordinate of the vertex is over a blocked cell
            if any(array[x][y] == '#' for x in range(i, i+1) for y in range(j, j+3) if 0 <= x < rows and 0 <= y < cols):
                continue
            
            vertex = (i, (j,j+1,j+2))
            neighbors = []

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
            if (array[i][j] == '#') or (array[i][j] if i > rows-3 else False):
                continue
            
            # Check if any coordinate of the vertex is over a blocked cell
            if any(array[x][y] == '#' for y in range(j, j+1) for x in range(i, i+3) if 0 <= x < rows and 0 <= y < cols):
                continue

            vertex = ((i,i+1,i+2), j)
            neighbors = []
            # This function is repeated for the sake of readability 

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

def free_area_check(coord, array, rows, cols):
    x, y = coord

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) == (x, y):
                continue
            if not (0 <= i < rows and 0 <= j < cols):
                return False
            if array[i][j] == '#':
                return False

    return True

def add_edges_between_graphs(graph1, graph2, array, vertex_formats):
    rows = len(array)
    cols = len(array[0])

    for vertex1, edges1 in graph1.items():
        if isinstance(vertex1, vertex_formats[0]):
            x1 = vertex1[0]
            y1 = vertex1[1][1]
            for vertex2, edges2 in graph2.items():
                if isinstance(vertex2, vertex_formats[1]):
                    x2 = vertex2[0][1]
                    y2 = vertex2[1]
                    if (x1, y1) == (x2, y2) and free_area_check((x1, y1), array, rows, cols):
                        edges1.append(vertex2)
                    else:
                        continue
        # elif isinstance(vertex1, vertex_formats[1]):
        #     x1 = vertex1[0][1]
        #     y1 = vertex1[1]
        #     for vertex2, edges2 in graph2.items():
        #         if isinstance(vertex2, vertex_formats[0]):
        #             x2 = vertex2[0]
        #             y2 = vertex2[1][1]
        #             if (x1, y1) == (x2, y2) and free_area_check((x1, y1), array, rows, cols):
        #                 edges1.append(vertex2)
        #             else:
        #                 continue

    return graph1

def breadth_first_search(graph, start, goals, vertex_formats, goal_formats):
    queue = deque()
    queue.append((start, [start]))

    while queue:
        vertex, path = queue.popleft()

        if any(isinstance(vertex, format) for format in goal_formats):
            if vertex in goals:
                return path

        for neighbor in graph[vertex]:
            if neighbor not in path and any(all(isinstance(x, t) for x, t in zip(neighbor, f)) for f in vertex_formats):
                queue.append((neighbor, path + [neighbor]))

    return -1