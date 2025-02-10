class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 建立一個Hash Table
        num_hash = {}
        # 迴圈從頭開始找元素
        for i, num in enumerate(nums):
            # 檢查Target減掉當前值，是否已存在Hash Table中
            element = target - num
            # 如果已存在Hash Table，則回傳那個值與當前值的位置
            if element in num_hash :
                return [num_hash[element],i]
            # 否則將當前值加入Hash Table中
            num_hash[num] = i

        # 題目保證有一解，且只有一解，所以不會到這
        return []
        
