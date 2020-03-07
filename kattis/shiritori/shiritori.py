n = int(input())
heard = set()
fail = False
lastchar = None
for i in range(0, n):
    word = input().split('\n')[0]
    if word in heard:
        fail = True
        break
    if i != 0 and lastchar != word[0]:
        fail = True
        break
    lastchar = word[-1]
    heard.add(word)
if fail:
    if i % 2 == 0:
        print("Player 1 lost")
    else:
        print("Player 2 lost")
else:
    print("Fair Game")
