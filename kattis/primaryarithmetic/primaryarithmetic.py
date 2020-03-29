
while True:
    n1, n2 = input().split()
    n1 = n1[::-1]
    n2 = n2[::-1]
    if len(n1) < len(n2):
        n1, n2 = n2, n1
    if n1 == '0' and n2 == '0':
        break

    carries = 0
    carry = 0
    for i in range(0, len(n1)):
        if i < len(n2):
            v = int(n1[i]) + int(n2[i]) + carry
            if v >= 10:
                carries += 1
                carry = 1
            else:
                carry = 0
        else:
            v = int(n1[i]) + carry
            if v >= 10:
                carries += 1
                carry = 1
            else:
                carry = 0
    if carries == 0:
        print("No carry operation.")
    elif carries == 1:
        print("1 carry operation.")
    else:
        print("{0} carry operations.".format(carries))
