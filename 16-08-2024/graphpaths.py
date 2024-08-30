def main():
    graph = {}
    v, e, k = [int(x) for x in input().split()]
    for i in range(v + 1):
        graph[i] = []
    for i in range(e):
        v_in, v_out = [int(x) for x in input().split()]
        graph[v_in].append(v_out)
    n = paths(graph, v, k)
    mod = pow(10, 9) + 7
    print(n % mod)
    return


def paths(graph, v, k):
    stack = [(1, 0)]  
    count = 0

    while stack:
        current_node, lenPath = stack.pop()

        if lenPath == k and current_node == v:
            count += 1
            continue

        if lenPath < k:
            for adj in graph[current_node]:
                stack.append((adj, lenPath + 1))

    return count


main()
