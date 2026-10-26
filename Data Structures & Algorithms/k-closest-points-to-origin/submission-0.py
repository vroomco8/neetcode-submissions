class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        mxheap = []

        for x,y in points:

            d = -(x**2 + y**2)
            heapq.heappush(mxheap, [d, x, y])
            if len(mxheap) > k:
                heapq.heappop(mxheap)

        res = []

        while mxheap:
            dist, x, y = heapq.heappop(mxheap)
            res.append([x, y])

        return res
        