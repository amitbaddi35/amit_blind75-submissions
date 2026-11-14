class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_rows = len(matrix)
        max_cols = len(matrix[0])
        top = 0
        bottom = max_rows - 1
        # Binary Search on rows TC : log(m)
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
            
        left = 0
        right = max_cols - 1
        row = (top + bottom) // 2
        found = False
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                print(f'Array Element {target} found at location ({row,mid})')
                found = True
                return True
                break
            elif target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                break
        if not found:
            print(f'Element {target} not found in given array {matrix}')
            return False







