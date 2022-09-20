"""
You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point [0, 0], 
and you are given a destination point target = [xtarget, ytarget] that you are trying to get to. 
There are several ghosts on the map with their starting positions given as a 2D array ghosts, 
where ghosts[i] = [xi, yi] represents the starting position of the ith ghost. 
All inputs are integral coordinates.

Each turn, you and all the ghosts may independently choose to either move 1 unit in any of the four 
cardinal directions: north, east, south, or west, or stay still. All actions happen simultaneously.

You escape if and only if you can reach the target before any ghost reaches you. 
If you reach any square (including the target) at the same time as a ghost, 
it does not count as an escape.

Return true if it is possible to escape regardless of how the ghosts move, otherwise return false.
"""
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        ghost_moves = []
        for i in range(0, len(ghosts)):
            dist = abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1])
            ghost_moves.append(dist)
        moves = abs(target[0]) + abs(target[1])
        
        for g in ghost_moves:
            if (g <= moves):
                return False
        return True
    
"""
Runtime: 34 ms, faster than 87.50% of Python online submissions for Escape The Ghosts.
Memory Usage: 13 MB, less than 100.00% of Python online submissions for Escape The Ghosts.
"""