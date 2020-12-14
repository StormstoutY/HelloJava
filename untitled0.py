#import time
#
#class Solution:
#    def twoSum(self,nums, target):
#     start =time.clock()
#     lens = len(nums)
#     j=-1
#     for i in range(lens):
#        if (target - nums[i]) in nums:
#            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
#                continue
#            else:
#                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
#                break
#     if j>0:
#        return [i,j]
#     else:
#        return []
#     end = time.clock()
#     print('Running time: %s Seconds'%(end-start))
#
#
#    def twoSum2(self,nums, target):
#     start =time.clock()   
#     lens = len(nums)
#     j=-1
#     for i in range(1,lens):
#        temp = nums[:i]
#        if (target - nums[i]) in temp:
#            j = temp.index(target - nums[i])
#            break
#     if j>=0:
#        return [j,i]
#     end = time.clock()
#     print('Running time: %s Seconds'%(end-start))    
#
#
#    def twoSum3(self,nums, target):
#     hashmap={}
#     for ind,num in enumerate(nums):
#        hashmap[num] = ind
#     for i,num in enumerate(nums):
#        j = hashmap.get(target - num)
#        if j is not None and i!=j:
#            return [i,j]
#
#    def twoSum4(self,nums, target):
#     hashmap={}
#     for i,num in enumerate(nums):
#        if hashmap.get(target - num) is not None:
#            return [i,hashmap.get(target - num)]
#        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

a=[1,2,3,4,5]
print(a[:0])