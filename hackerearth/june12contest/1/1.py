'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def summation(n):
    if (n==0):
        return 0;
    if (n&1):
        return (int((n + 1) // 2)**2 + summation(int(n // 2)))
    else:
        return (int(n // 2)**2 + summation(int(n // 2)))

n = int(input())
for _ in range(n):
    N,M = list(map(int, input().split()))
    s = 0
    print(summation(N)%M)
