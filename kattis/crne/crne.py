n = int(input())

p, q = n//2, n//2
if p+q < n:
    p += 1
print((p+1)*(q+1))
