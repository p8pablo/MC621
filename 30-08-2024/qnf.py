def main():
    n, m =[int(x) for x in input().split()]
    matrix = []
    Q = 0
    F = 0
    for i in range(n):
        matrix.append([])
        x = input()
        for j in x:
            matrix[i].append(j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                if isQ(i,j):
                    Q += 1
                else:
                    isF(i,j)
                    F += 1
    print(Q, F)
    return
def isQ(i,j):
    
    return False
def isF(i,j):
    
    return False
main()