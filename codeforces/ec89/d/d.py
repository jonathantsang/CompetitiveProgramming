rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(n, arr):
    maxInt = max(arr)+5
    pr, pf = [],  [0 for _ in range(maxInt)]
    is_prime = [True for _ in range(maxInt)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, maxInt):
        if is_prime[i]:
            pr.append(i)
            pf[i] = i
        for p in pr:
            if i*p >=maxInt:
                break
            pf[i*p] = p
            is_prime[i*p] = False
            if (i%p==0):
                break
    a = [str(-1) for _ in range(n)]
    b = [str(-1) for _ in range(n)]
    for  i in range(n):
        r = arr[i]
        if is_prime[r]:
            continue
        g, h = r, 1
        p = pf[r]
        while g%p == 0:
            g//=p
            h*= p
        if g!=1:
            a[i] = str(g)
            b[i]= str(h)

    print(' '.join(a))
    print(' '.join(b))

n = rri()
arr=rrm()
solve(n, arr)
