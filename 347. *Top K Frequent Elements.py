class Solution(object):
    def topKFrequent(self, nums, k):
        new_dict = dict()
        for item in nums:
            if not new_dict.has_key(item):
                new_dict[item] =1;
            else:
                new_dict[item] +=1;
        sorted_dict = sorted(new_dict, key=new_dict.get, reverse=True)
        return sorted_dict[:k]
