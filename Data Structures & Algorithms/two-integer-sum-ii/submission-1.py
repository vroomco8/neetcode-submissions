class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        lp = 0
        rp = len(numbers)-1

        while numbers[lp] + numbers[rp] != target:

            cur = numbers[lp] + numbers[rp]

            if cur < target:
                lp += 1
            elif cur > target:
                rp -= 1

        return [lp+1, rp+1]