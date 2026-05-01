def breakingRecords(scores):
    # Write your code here
    max_scores = scores[0]
    min_scores = scores[0]
    max_beat = 0
    min_beat = 0

    n = len(scores)
    if len(scores) == 1:
        return 0,0

    for i in range(1,n):
        if min(min_scores,scores[i]) < min_scores:
            min_beat += 1
            min_scores = min(min_scores,scores[i])
        if max(max_scores, scores[i]) > max_scores:
            max_beat += 1
            max_scores = max(max_scores, scores[i])
    return max_beat, min_beat

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores))