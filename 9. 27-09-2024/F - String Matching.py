def main():
    string = input()
    pattern = input()
    count = 0
    if len(string) < len(pattern):
        print(0)
        return
    max_index = len(string) - len(pattern)
    for i in range(0, max_index + 1):
        if string[i:i+len(pattern)] == pattern:
            count += 1
            i += len(pattern)
    print(count)

main()
