def all_same(s):
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            return False
    return True

t = int(input().strip())
for _ in range(t):
	s = input().strip()
	if all_same(s):
	    print(s)
	else:
		new_s = ""
		for i in range(len(s)):
		    new_s += "01"
		print(new_s)