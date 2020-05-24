
def dijkstra(G, n, start_node, end_node):
    INFINITY = 999999
    cost = []
    distance = []
    pred = []
    visited = []
    """
        Init cost matrix with 0 value
    """
    for i in range(n):
        cost.append([])
        for j in range(n):
            cost[i].append(0)

    """
        Init base value of cost matrix base on G matrix
    """
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                cost[i][j] = INFINITY
            else:
                cost[i][j] = G[i][j]

    """
        Init distance, pred, visited
    """
    for i in range(n):
        distance.append(cost[start_node][i])
        pred.append(start_node)
        visited.append(0)
    distance[start_node] = 0
    visited[start_node] = 1
    count = 1

    """
        Main of dijkstra algorithm
    """
    next_node = None
    while count < n-1:
        min_distance = INFINITY
        for i in range(n):
            if distance[i] < min_distance and visited[i] == 0:
                min_distance = distance[i]
                next_node = i
        if next_node is not None:
            visited[next_node] = 1
        else:
            return None
        for i in range(n):
            if visited[i] == 0:
                if min_distance + cost[next_node][i] < distance[i]:
                    distance[i] = min_distance + cost[next_node][i]
                    pred[i] = next_node
        count += 1

    """
        Handling result
    """
    result = None
    if distance[end_node] == INFINITY:
        return result

    result = {
       'distance': distance[end_node],
        'path': []
    }
    j = end_node
    while j != start_node:
        result['path'].append(j)
        j = pred[j]
    result['path'].append(start_node)
    result['path'].reverse()

    return result

