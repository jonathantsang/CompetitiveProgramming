class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        scores = {}
        for vote in votes:
            for i, team in enumerate(vote):
                if team in scores:
                    scores[team][i] += 1
                else:
                    scores[team] = [0 for _ in range(0, 26)]
                    scores[team][i] = 1
        #print(scores)
        teams = []
        for t in scores:
            teams.append([scores[t], -ord(t), t])
        teams = sorted(teams, reverse=True)
        #print(teams)
        return "".join([t[2] for t in teams])
        