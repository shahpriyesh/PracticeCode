class RankTeamByVotes:
    def rankTeams(self, votes):
        hmap = {}

        for team in votes[0]:
            hmap[team] = 0

        max_score = len(votes[0])
        for vote in votes:
            score = max_score
            for team in vote:
                hmap[team] += score
                score -= 1

        return ''.join([k for k, v in sorted(hmap.items(), key=lambda i: i[1], reverse=True)])


object = RankTeamByVotes()
print(object.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))