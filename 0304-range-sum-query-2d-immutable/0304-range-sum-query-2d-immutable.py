
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        m, n = len(matrix), len(matrix[0])
        
        # rowwise sum
        for idx in range(m):
            for jdx in range(1, n):
                matrix[idx][jdx] += matrix[idx][jdx-1]
                print(matrix[0][0])
# what about the value of 00
        # colwise sum
        for idx in range(1, m):
            for jdx in range(n):
                matrix[idx][jdx] += matrix[idx-1][jdx]

        self.prefix_sum_matrix = matrix

        print(self.prefix_sum_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        out = self.prefix_sum_matrix[row2][col2]
        if row1-1 >= 0:
            out -= self.prefix_sum_matrix[row1-1][col2] 
        if row1-1 >=0 :
            # col2
            out -= self.prefix_sum_matrix[row2][col1-1] 
    
        if row1-1 >= 0 :
            out += self.prefix_sum_matrix[row1-1][col1-1]

        return out
   
    
        
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     print(row1,col1,row2,col2)

    #     out = self.prefix_sum_matrix[row2][col2] - self.prefix_sum_matrix[row1-1][col2] - self.prefix_sum_matrix[row2][col1-1] + self.prefix_sum_matrix[row1-1][col1-1]








# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)