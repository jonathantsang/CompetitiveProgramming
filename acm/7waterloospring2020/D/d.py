from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

# at most 100,000 cards in all hands

def solve(N, H):
    blocked = []
    while True:
        seen = defaultdict(list)
        popped = False
        for i in range(N):
            hand = H[i]
            if hand and hand[-1] in seen:
                seen[hand[-1]].append(i)
                popped = True
            else:
                if hand:
                    seen[hand[-1]].append(i)

        best = float('inf')
        for val in seen:
            if len(seen[val]) > 1:
                for idx in seen[val]:
                    H[idx].pop()
                # we pop all, but theoretically we keep one
                blocked.append(set(seen[val]))

        if popped:
            break

    amt = 0
    for hand in H:
        amt += len(hand)
    return amt + blocked

v = "abc"
while True:
    v = rrm()
    if len(v) == 1 and v[0] == 0:
        break

    cardHands = v[0]
    hands = []
    for _ in range(cardHands):
        hands.append(rr().split()[1:]) # all but first element which is length

    print(solve(cardHands, hands))
