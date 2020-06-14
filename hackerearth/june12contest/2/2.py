'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N,Q = list(map(int, input().split()))
arr = list(map(int, input().split()))
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))
