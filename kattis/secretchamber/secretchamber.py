m, n = list(map(int, input().split()))

def enumerate(old, new, i, translate, seen):
    if "".join(old) == "".join(new):
        return True
    if len(old) == i:
        return False

    if old[i] == new[i]:
        return enumerate(old, new, i+1, translate, seen)

    if old[i] not in translate:
        return False

    for change in translate[old[i]]:
        original = old[i]
        old[i] = change
        if "".join(old) in seen:
            continue

        seen.add("".join(old))
        v = enumerate(old, new, i, translate, seen)
        old[i] = original
        if v:
            return v
    return False

translate = {}
for _ in range(0, m):
    old, new = input().split()
    if old in translate:
        translate[old].append(new)
    else:
        translate[old] = [new]
for _ in range(0, n):
    old, new = input().split()
    a = False
    if len(old) == len(new):
        a = enumerate(list(old), list(new), 0, translate, set())
    if a:
        print("yes")
    else:
        print("no")
