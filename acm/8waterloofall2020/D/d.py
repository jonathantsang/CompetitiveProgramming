from collections import defaultdict, deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N, edges, countries, origin):
	sortedCountries = sorted(list(countries))
	#print(sortedCountries)
	#print(origin)

	queue = deque([(origin, 1)]) # (country, time)
	times = defaultdict(lambda: 0) # country -> time
	
	while queue:
		country, time = queue.popleft()

		if country in times:
			continue
		times[country]=time

		for adj in edges[country]:
			if adj not in times:
				queue.append((adj, time+1))

	for country in sortedCountries:
		print(times[country])


N=rri() # countries
edges = defaultdict(list)
countries = set()
start = None

for i in range(N):
	places = rr().split()

	origin = places[0]
	if start == None:
		start = origin

	# reverse edge
	allows = places[4:]
	#print(origin, allows)

	for country in allows:
		edges[country].append(origin)

	#print(origin)
	#print(allows)

	countries.add(origin)
	for country in allows:
		countries.add(country)

	#print(countries)
#print(edges)
solve(N, edges, countries, start)
