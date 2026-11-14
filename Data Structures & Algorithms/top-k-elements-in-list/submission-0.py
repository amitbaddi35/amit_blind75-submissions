class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        max_heap = []
        counter = Counter(nums)
        res = []
        
        
        for num, freq in counter.items():
            heapq.heappush(max_heap, (freq, num))
        
        print(max_heap)
        for i in range(len(max_heap)):
            if i >= k:
                heapq.heappop(max_heap)
        print(max_heap)
        return [i[1] for i in max_heap]



        