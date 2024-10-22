def tsp_dp(adj_list):
    """Compute the exact solution to the TSP using dynamic programming and returns the optimal path.

    Args:
        dist_arr: Weighted undirected graph represented as an adjacency list. 

    Returns:
        List[int]: A list of city indices representing the optimal path.
    """
    # ...
    def get_weights(n, adj_list):
        weights = [[-1 for _ in range(n)] for _ in range(n)]
        for u, edges in enumerate(adj_list):
            for v, w in edges.items():
                weights[u][v] = w
                weights[v][u] = w
        return weights

    n = len(adj_list)
    for dict in adj_list:
        n = max(n, max(dict.keys()) + 1)

    print(n, adj_list)
    weights = get_weights(n, adj_list)

    f = [[-1 for _ in range(n)] for _ in range(1 << n)]
    f[1][0] = 0
    path = [[-1 for _ in range(n)] for _ in range(1 << n)]
    vis = [[False for _ in range(n)] for _ in range(1 << n)]
    vis[1][0] = True

    def dfs(sta, u):
        if vis[sta][u] or sta & 1 == 0:
            return f[sta][u]
        
        # print(f"In state {bin(sta)}, at node {u}")
        vis[sta][u] = True

        '''
        The state get value from a state that not visit u, use a path v->u
        '''
        mask = sta & ~(1 << u)
        # print(bin(mask))
        for v in range(n):
            if (mask & (1 << v)) and weights[u][v] != -1:
                val = dfs(mask, v)
                if val == -1:
                    continue
                val += weights[u][v]
                # print(f"from {bin(sta)}, {u} search {bin(mask)}, {v}, get {val}")
                if f[sta][u] == -1 or val < f[sta][u]:
                    
                    f[sta][u] = val
                    path[sta][u] = v

        return f[sta][u]
    
    last = None
    for i in range(1, n):
        if weights[0][i] == -1:
            continue
        val = dfs((1 << n) - 1, i)
        if val == -1:
            continue
        val += weights[i][0]
        if last == None or val < last:
            last = val
            path[(1 << n) - 1][0] = i
            f[(1 << n) - 1][0] = val

    for sta in range(1 << n):
        for i in range(n):
            if f[sta][i] == -1:
                continue
            print(f"{bin(sta)} {i} {f[sta][i]}")

    if last == None:
        return []

    ans = [0]
    sta = (1 << n) - 1
    u = path[sta][0]
    print(u)
    while u != 0:
        ans.append(u)
        v = path[sta][u]
        sta = sta & ~(1 << u)
        u = v

    
    ans.reverse()
    return ans



adj = [{3: 5, 4: 5}, {2: 5, 3: 4, 4: 9}, {1: 5, 4: 4}, {0: 5, 1: 4}, {0: 5, 1: 9, 2: 4}]




print(tsp_dp(adj))