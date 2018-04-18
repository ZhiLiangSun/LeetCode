nums = [2, 7, 11, 15]
target = 9


class TwoSum:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 將list內的value存在dictionary的key，index存在dictionary的value
        # enumerate的作用為將iterable的物件組成一個索引序列，利用它可以獲得索引和值
        # in的作用為測試key是否存在dictionary中

        dic = {}
        for key, value in enumerate(nums):
            sol = target - value
            if sol in dic:
                return [dic[sol], key]
            else:
                dic[value] = key

        # for num in nums:
        #     if (target - num) in nums:
        #         return nums.index(num), nums.index((target - num))


answer = TwoSum

print(answer.twoSum(answer, nums, target))
