class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)

        while len(stones) > 1:
            l1, l2 = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if l1!=l2:
                heapq.heappush_max(stones, abs(l1-l2))
        
        return stones[0] if len(stones) == 1 else 0
        