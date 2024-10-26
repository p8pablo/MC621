# utilizando código visto em aula

def longest_palindromic_subsequence(A):
    memo = {}
    def lps_length(l, r):
        if l > r:
            return 0
        if l == r:
            return 1
        if (l, r) in memo:
            return memo[(l, r)]
    
        if A[l] == A[r]:
            result = 2 + lps_length(l + 1, r - 1)
        else:
            result = max(lps_length(l, r - 1), lps_length(l + 1, r))
        memo[(l, r)] = result
        return result
    return lps_length(0, len(A) - 1)

def main():
    t = int(input())
    for _ in range(t):
        string = input()
        print(longest_palindromic_subsequence(string))
    return

main()