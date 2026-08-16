class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = set(nums)
        map = dict.fromkeys(keys,0)
        for n in nums:
            map[n] += 1
        sorted_items = sorted(map.items(), key=lambda item: item[1], reverse=True)
        list = []
        for i in range(k):
            list.append(sorted_items[i][0])
        return list