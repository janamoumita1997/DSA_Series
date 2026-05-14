"""

"""
ranked = [100,90,90,80,75,60]
player = [50,65,77,90,102]
# def climbingLeaderboard(ranked, player):

# new_ranked = sorted(list(set(ranked)),reverse=True)
# for i in player:
#     new_ranked.append(i)
#     new_ranked = sorted(list(set(new_ranked)),reverse=True)
#     print(new_ranked.index(i)+1)

import bisect


played = [50,65,77,90,102]
# Step 1: deduplicate, sort ascending (for bisect)
asc_ranked = sorted(set(ranked))
results = []

for score in played:
    pos = bisect.bisect_left(asc_ranked, score)

    # insert only if not duplicate
    if pos >= len(asc_ranked) or asc_ranked[pos] != score:
        asc_ranked.insert(pos, score)

    # rank = total elements - index of score
    rank = len(asc_ranked) - bisect.bisect_left(asc_ranked, score)
    results.append(rank)

print(results) 
        