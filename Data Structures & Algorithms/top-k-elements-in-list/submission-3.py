'''
Given integers. Need to return k most frequent elements in the array.
Answer always unique.
Can return answer in any order.

Can I group numbers based on their frequency?
Have an array where each index stores a list of numbers with that frequency. It will be 0-indexed.

Need to have a Counter to get all the freqs.

Then just iterate backwards in array till we have k numbers?

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        array_of_buckets = [[] for _ in range(10000)]

        for value, frequency in count.items():
            array_of_buckets[frequency - 1].append(value)

        res = []
        for i in range(len(array_of_buckets)-1,-1,-1):
            for num in array_of_buckets[i]:
                if len(res) < k:
                    res.append(num)
        
        return res


        