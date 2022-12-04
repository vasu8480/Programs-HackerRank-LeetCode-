from bisect import bisect_right as br
def climbingLeaderboard(ranked, player):
	ranked= sorted(set(ranked))
	grades= list(range(len(ranked)+1,0,-1))
	print([grades[br(ranked,i)] for i in player])
	return [(grades[br(ranked, i)]) for i in player]

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))