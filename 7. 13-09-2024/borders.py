def main():
    string = input()
    prefix = []
    sufix = []
    borders = []
    i = 0
    j = len(string) - 1
    for _ in range(len(string)):
        prefix.append(string[i])
        sufix.append(string[j])
        i += 1
        j -= 1
        r_sufix = sufix[::-1]
        if prefix == r_sufix and len(prefix) < len(string):
            borders.append(len(prefix))
    for i in borders:
        print(i, end=" ")
    return


main()
