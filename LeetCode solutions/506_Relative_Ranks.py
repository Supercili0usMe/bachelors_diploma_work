from typing import List


class Solution:
    def findRelativeRanks(score: List[int]) -> List[str]:
        place_dict = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        sorted_score = sorted(score, reverse=True)
        for i, sc in enumerate(sorted_score):
            if i < 3:
                place_dict[sc] = medals[i]
            else:
                place_dict[sc] = str(i+1)

        return [place_dict[sc] for sc in score]


print(Solution.findRelativeRanks([5,4,3,2,1]))
print(Solution.findRelativeRanks([10,3,8,9,4]))
print(Solution.findRelativeRanks([0]))
print(Solution.findRelativeRanks([7, 0]))
print(Solution.findRelativeRanks([14, 7, 0]))
print(Solution.findRelativeRanks([21,14,0,7]))
print(Solution.findRelativeRanks([56,42,28,63,21,14,7,49,70,0,35]))