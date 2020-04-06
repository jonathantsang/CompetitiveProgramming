# reads files with ranks

results = open("results.txt", 'r')
total = open("total.txt", 'r')

contests = []
# grep -E "jonathantsang" *.txt -n > results.txt
for line in results.readlines():
	contest, rank, name = line.split(":")
	contests.append([contest, int(rank), 0, 0])

# xargs wc -l <contests.txt > total.txt
for i, line in enumerate(total.readlines()):
	total, contest = line.split()
	contests[i][2] = int(total)
	contests[i][3] = round((contests[i][1]/contests[i][2])*100,2)

for r in reversed(contests):
	print(r[0][3:-4], str(r[1]) + "/" + str(r[2]), "Top " + str(r[3]) + "%")