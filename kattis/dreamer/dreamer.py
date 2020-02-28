n = int(input())

earliest = "99999999"
count = 0

def earliestd(d1, d2):
    d1 = list(map(int, [d1[:2], d1[2:4], d1[4:]]))
    d2 = list(map(int, [d2[:2], d2[2:4], d2[4:]]))
    if d1[2] == d2[2]:
        if d2[1] == d1[1]:
            return d1[0] < d2[0]
        return d1[1] < d2[1]
    return d1[2] < d2[2]


def validDate(date):
    # DD MM YYYY
    date = list(map(int, [date[:2], date[2:4], date[4:]]))
    # print(date)

    if date[0] < 1:
        return False
    if date[1] < 1:
        return False
    if date[2] < 2000:
        return False
    if date[1] > 12:
        return False

    leap = False
    if date[2] % 400 == 0:
        leap = True
    elif date[2] % 100 == 0:
        leap = False
    elif date[2] % 4 == 0:
        leap = True

    months = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8':31, '9':30, '10':31, '11':30, '12':31}
    if leap:
        months['2'] += 1

    if date[0] > months[str(date[1])]:
        return False

    return True

def permutate(digits, sofar):
    global count
    global earliest
    if len(sofar) == 8:
        if validDate(sofar):
            count += 1
            if earliestd(sofar, earliest):
                earliest = sofar
        return
    for v in digits:
        if digits[v] > 0:
            digits[v] -= 1
            permutate(digits, sofar + v)
            digits[v] += 1

for _ in range(0, n):
    count = 0
    earliest = "99999999"

    digits = {}
    vals = "".join(input().split())
    # print(vals)
    for v in vals:
        if v in digits:
            digits[v] += 1
        else:
            digits[v] = 1

    permutate(digits, "")
    if count == 0:
        print(0)
    else:
        print(count, earliest[:2], earliest[2:4], earliest[4:])
