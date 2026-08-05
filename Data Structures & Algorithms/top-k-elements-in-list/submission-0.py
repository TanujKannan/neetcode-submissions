class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        counts = Counter(nums)
        print(counts)

        for num, count in counts.items():
            buckets[count].append(num)

        print(buckets)
        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
                