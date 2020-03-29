v = int(input())
e = int(input())

songs = {i: set() for i in range(0, v+1)} # n -> set() of songs
new_song = 0

# 1 is the bard
for _ in range(0, e):
    present = list(map(int, input().split()))[1:]
    if 1 in present:
        for i in present:
            songs[i].add(new_song)
        new_song += 1
    else:
        # exchange
        total = set()
        for i in present:
            for song in songs[i]:
                total.add(song)
        for i in present:
            for song in total:
                songs[i].add(song)

#print(songs, new_song)
for person in songs:
    if len(songs[person]) == new_song:
        print(person)
