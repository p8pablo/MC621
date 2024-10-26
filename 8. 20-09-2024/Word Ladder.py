def main():
    s = []
    t = []
    s_s = input()
    t_s = input()
    for i in range(len(s_s)):
        s.append(s_s[i])
        t.append(t_s[i])
    x = []
    for i in range(len(s)):
        if t[i] != s[i]:
            if t[i] < s[i]:
                s[i] = t[i]
                x.append(''.join(s))

    for j in range(len(s)-1, -1, -1):
        if t[j] != s[j]:
            s[j] = t[j]
            x.append(''.join(s))
    
    print(len(x))
    for i in x:
        print(i)
    return
main()