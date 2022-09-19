# 1582. Special Positions in a Binary Matrix
# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements 
# in row i and column j are 0 (rows and columns are 0-indexed).

class Solution(object):    
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                if (mat[i][j] == 1 and sum(mat[i]) + self.sumColumn(mat, j) == 2):
                    count += 1
        return count
    
    def sumColumn(self, mat, j):
        count = 0
        for i in range(len(mat)):
            count += mat[i][j]
        return count