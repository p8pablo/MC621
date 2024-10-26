def main():
    nums = []
    while True:
        num = input()
        if not num:
            break
        else:
            nums.append(int(num))
    for n in range(len(nums)):
        print("Case ", n + 1, ":", sep="")
        runPrime(nums[n])
        if n != len(nums) - 1:
            print("\r")


def runPrime(n):
    arr = []
    used = [False] * (n + 1)
    for i in range(n):
        arr.append(i + 1)
    used[1] = True
    primeRing([1], n, used)

    return


def primeRing(path, n, used):
    if len(path) == n:
        if isPrime(path[-1] + path[0]):

            print(" ".join(map(str, path)))
        return
    for i in range(2, n + 1):
        if not used[i] and isPrime(path[-1] + i):
            used[i] = True
            primeRing(path + [i], n, used)
            used[i] = False

    return


def isPrime(num):
    arr = []
    for i in range(1, num + 1):
        if not num % i:
            arr.append(i)
    if len(arr) == 2:
        return True
    else:
        return False


main()
