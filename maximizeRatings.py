# ratings = [9,-1,-3,4,5]
ratings = [-1,-2,-3,-4,-5]
def maximizeRatings(i, rating, force) -> int:
    global ratings
    if i == len(ratings):
        return rating
    if force:
        return maximizeRatings(i+1, rating+ratings[i], False)
    else:
        return max(maximizeRatings(i+1, rating+ratings[i], False), maximizeRatings(i+1, rating, True))

print(maximizeRatings(0, 0, False))