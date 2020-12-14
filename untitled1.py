# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:09:18 2020

@author: mac
"""
import numpy as np
class Solution:
    def runningSum(self,nums):
        lens=len(sums)
        a=np.zeros(lens,dtype=int)
        a[0]=nums[0]
        for i in range(1,lens-1):
            a[i]=a[i-1]+nums[i]
        print(a)