seq = input()

p1=0
p2=0
p3=0
prev = seq[0]
# up
for i in range(1, len(seq)):
    if seq[i] != prev:
        p1 += 1
        prev = seq[i]
    if seq[i] == 'D':
        p1 += 1
        prev = 'U'
prev = seq[0]
# down
for i in range(1, len(seq)):
    if seq[i] != prev:
        p2 += 1
        prev = seq[i]
    if seq[i] == 'U':
        p2 += 1
        prev = 'D'
# left
for i in range(1, len(seq)):
    if seq[i] != seq[i-1]:
        p3 += 1

print(p1)
print(p2)
print(p3)
