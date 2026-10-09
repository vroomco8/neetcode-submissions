class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binSearch(lis, l, r):
            if l>r:
                return False
            m = (l + r) // 2
            print(m, lis[m])
            if lis[m] == target:
                return True
            elif lis[m] < target:
                l = m + 1
            elif lis[m] > target:
                r = m - 1
            return binSearch(lis, l, r)

        for r in matrix:
            if target <= r[-1]:
                return binSearch(r, 0, len(r)-1)
        return False
        
