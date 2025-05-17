class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        topK = list(sorted_map)[0:k]
        print(f"{sorted_map}:{topK}")
        return topK