def main():
    graph = {}
    v, e = [int(x) for x in input().split()]
    for i in range(v + 1):
        graph[i] = []
    for i in range(e):
        v_in, v_out, z = [int(x) for x in input().split()]
        graph[v_in].append(v_out)
        graph[v_out].append(v_in)
    n = dfs(graph, v + 1)
    print(n)
    return


def dfsvisit(G, v, cor):
    cor[v] = "c"
    for adj in G[v]:
        if not cor[adj]:
            dfsvisit(G, adj, cor)
    cor[v] = "p"


def dfs(G, v):
    cor = [None] * v
    count = 0
    for i in range(1, v):
        if not cor[i]:
            dfsvisit(G, i, cor)
            count += 1
    return count


main()
