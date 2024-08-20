def main():
    graph = {}
    v, e, k = [int(x) for x in input().split()]
    for i in range(v + 1):
        graph[i] = []
    for i in range(e):
        v_in, v_out = [int(x) for x in input().split()]
        graph[v_in].append(v_out)
        graph[v_out].append(v_in)
    if k == 1:
        print(v - 2)
        return
    n, cities = dfs(graph, v + 1)
    if len(cities) == 1:
        print(0)
        return
    for c in range(len(cities)):
        cities[c] = min(cities[c], k)
    print(max(0, n - (sum(cities) // 2) - 1))

    return


def dfsvisit(G, v, cor):
    cor[v] = "c"
    for adj in G[v]:
        if not cor[adj]:
            dfsvisit(G, adj, cor)
    cor[v] = "p"
    return


def dfs(G, v):
    cities = []
    cor = [None] * v
    count = 0
    comp_ant = 0

    for i in range(1, v):
        if not cor[i]:
            dfsvisit(G, i, cor)
            count += 1
            comp_atual = 0
            for c in cor:
                if c:
                    comp_atual += 1
            cities.append(comp_atual - comp_ant)
            comp_ant = comp_atual
    return count, cities


main()
