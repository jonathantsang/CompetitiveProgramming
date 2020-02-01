import sys

for line in sys.stdin:
    dice = list(map(int, line.split()))
    if dice[0] == 0 and dice[1] == 0 and dice[2] == 0 and dice[3] == 0:
        break
    p1 = [dice[0], dice[1]]
    p2 = [dice[2], dice[3]]
    p1.sort()
    p2.sort()

    # same?
    if p1[0] == p2[0] and p1[1] == p2[1]:
        print("Tie.")
        continue
    else:
        # Mia?
        if 1 in p1 and 2 in p1:
            print("Player 1 wins.")
            continue
        elif 1 in p2 and 2 in p2:
            print("Player 2 wins.")
            continue

        # doubles
        if p1[0] == p1[1] or p2[0] == p2[1]:
            # both doubles
            if p1[0] == p1[1] and p2[0] == p2[1]:
                if p1[0] > p2[0]:
                    print("Player 1 wins.")
                    continue
                else:
                    print("Player 2 wins.")
                    continue
            else:
                if p1[0] == p1[1]:
                    print("Player 1 wins.")
                    continue
                else:
                    print("Player 2 wins.")
                    continue

        # highest number
        if p1[1] > p2[1]:
            print("Player 1 wins.")
            continue
        elif p2[1] > p1[1]:
            print("Player 2 wins.")
            continue
        else:
            if p1[0] > p2[0]:
                print("Player 1 wins.")
                continue
            elif p2[0] > p1[0]:
                print("Player 2 wins.")
                continue
            else:
                print("Tie.")
                continue
