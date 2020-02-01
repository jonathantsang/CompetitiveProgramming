import sys

def countIn(sub, orig):
    count = 0
    for i in range(0, len(orig)-len(sub)+1):
        if orig[i] == sub[0]:
            # check match?
            match = True
            for j in range(1, len(sub)):
                if i + j > len(orig):
                    break
                if orig[i+j] != sub[j]:
                    match = False
                    break
            if match:
                count += 1
    return count
for line in sys.stdin:
    if line == "0\n":
        break
    else:
        SL = line.split()
        s = SL[0]
        l = SL[1]
        same = 0
        delete = 0
        insert = 0
        # same
        same = countIn(s, l)

        # delete
        deleted = {}
        for i in range(0, len(s)):
            constructed = s[:i] + s[i+1:]
            if constructed not in deleted and constructed in l:
                delete += countIn(constructed, l)
                deleted[constructed] = 1
        # insert
        inserted = {}
        for i in range(0, len(s)+1):
            for c in ['A', 'G', 'C', 'T']:
                constructed = s[:i] + c + s[i:]
                if constructed not in inserted and constructed in l:
                    insert += countIn(constructed, l)
                    inserted[constructed] = 1

        print(str(same) + " " + str(delete) + " " + str(insert))
