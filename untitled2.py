# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:51:56 2020

@author: mac
"""
#
#import numpy as np
#nums=[1,1,1,1,1]
#lens=len(nums)
#a=np.zeros(lens,dtype=int)
#a=list(a)
#print(a)
#a[0]=nums[0]
#for i in range(1,lens):
#            a[i]=a[i-1]+nums[i]

#a=[1,2,3,4,5,6,19,20,21,24]
#b=[2,3,19,21,27]
#               
#print([x for x in a if x in b])
#class Solution:
#    def intersection(self, nums1, nums2) :
#        nums1.sort()
#        nums2.sort()
#        length1, length2 = len(nums1), len(nums2)
#        intersection = list()
#        index1 = index2 = 0
#        while index1 < length1 and index2 < length2:
#            num1 = nums1[index1]
#            num2 = nums2[index2]
#            if num1 == num2:
#                # 保证加入元素的唯一性
#                if not intersection or num1 != intersection[-1]:
#                    intersection.append(num1)
#                index1 += 1
#                index2 += 1
#            elif num1 < num2:
#                index1 += 1
#            else:
#                index2 += 1
#        return intersection

# a=[1,2,3,4,5,6]
# print(a[:0])


import urllib.request
response = urllib.request.urlopen('http://www.zhihu.com')
html = response.read()
print(html)






































