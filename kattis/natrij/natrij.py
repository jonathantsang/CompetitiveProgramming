t1 = list(map(int, input().split(':')))
t2 = list(map(int, input().split(':')))

diff = 0
m1 = t1[0] * 3600 + t1[1] * 60 + t1[2]
m2 = t2[0] * 3600 + t2[1] * 60 + t2[2]
if m2 < m1:
    m2 += 24 * 3600

diff = m2 - m1

h = diff // 3600
m = (diff % 3600) // 60
s = (diff % 3600) % 60

if m1 == m2:
    print("24:00:00")
else:
    print("{0}:{1}:{2}".format(str(h).zfill(2),str(m).zfill(2),str(s).zfill(2)))
