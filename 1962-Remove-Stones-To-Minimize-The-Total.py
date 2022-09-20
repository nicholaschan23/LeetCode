"""
You are given a 0-indexed integer array piles, where piles[i] represents 
the number of stones in the ith pile, and an integer k. 
You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
"""
from heapq import heappop, heappush
import math

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in piles:
            heapq.heappush(heap, -i) # negative = max queue
        
        for i in range(k):
            num_pop = heapq.heappop(heap)
            num_pop += int(math.floor(-num_pop/2))
            heapq.heappush(heap, num_pop)
        return -sum(heap)
        
        # for k_times in range(0, k):
        #     i_max = piles.index(max(piles))
        #     piles[i_max] -= int(math.floor(piles[i_max]/2))
        # return sum(piles)