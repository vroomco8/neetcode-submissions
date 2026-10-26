class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cnt = {}
        queue = deque()
        time = 0
        
        for t in tasks:
            cnt[t] = cnt.get(t, 0) + 1

        heap = [-c for c in cnt.values()]
        heapq.heapify(heap)

        while heap or queue:
            time += 1

            if not heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time
        

        