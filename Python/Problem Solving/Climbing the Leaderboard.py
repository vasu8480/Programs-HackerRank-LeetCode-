def climbingLeaderboard(ranked, player):
		# Write your code here
		ranked = list(set(ranked))
		ranked.sort(reverse=True)
		rank = []
		for i in player:
				while len(ranked) > 0 and i >= ranked[-1]:
						ranked.pop()
				rank.append(len(ranked)+1)
		return rank
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
#---------------------------------------------------------------------------------------------------
from bisect import bisect_right as br
def climbingLeaderboard(ranked, player):
	ranked= sorted(set(ranked))
	grades= list(range(len(ranked)+1,0,-1))
	print([grades[br(ranked,i)] for i in player])
	return [(grades[br(ranked, i)]) for i in player]

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))