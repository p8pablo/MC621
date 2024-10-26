def visitroom(matrix, visitados, x, y, lin, col):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitados[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < lin and 0 <= ny < col and not visitados[nx][ny] and matrix[nx][ny] == '.':
            visitroom(matrix, visitados, nx, ny, lin, col)


def countroom(matrix, lin, col):
    q = 0
    visitados = [[False for _ in range(col)] for _ in range(lin)]
    for i in range(lin):
        for j in range(col):
            if matrix[i][j] == '.' and not visitados[i][j]:
                visitroom(matrix, visitados, i, j, lin, col)
                q += 1
    return q


def main():
    n, m = map(int, input().split())
    matrix = []
    q = 0
    for i in range(n):
        matrix.append([])
        x = input()
        for j in x:
            matrix[i].append(j)
    
    print(countroom(matrix, n, m))
    return


main()
