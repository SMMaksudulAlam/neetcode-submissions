class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        row = 0

        while(top<=bottom):
            mid = (top+bottom)//2
            if(matrix[mid][0]<=target<=matrix[mid][-1]):
                row = mid
            if(matrix[mid][0] > target):
                bottom = mid-1
            else:
                top = mid+1
        print(row)
        left = 0
        right = len(matrix[0])-1

        while(left<=right):
            mid = (left+right)//2
            if(matrix[row][mid]==target):
                return True
            if(matrix[row][mid] > target):
                right = mid-1
            else:
                left = mid+1
        return False