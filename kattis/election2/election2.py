n = int(input())

parties = {} # name -> party
for i in range(0, n):
    name = input().strip()
    party = input().strip()
    parties[name] = party

b = int(input())
votes = {} # name -> number
for i in range(0, b):
    name = input().strip()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
most = 0
cand = []
for p in votes:
    if votes[p] == most:
        cand.append(p)
    elif votes[p] > most:
        cand = [p]
        most = votes[p]
if len(cand) > 1:
    print("tie")
else:
    print(parties[cand[0]])
