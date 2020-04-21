import collections

class TopKFrequent:
    def topKFrequent(self, nums, k):
        c = collections.Counter(nums)
        mostCommon = c.most_common(k)
        return [i[0] for i in mostCommon]


object = TopKFrequent()
print(object.topKFrequent([1,1,1,2,2,3], 2))
print(object.topKFrequent([1], 1))