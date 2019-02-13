#!/bin/python3

import math
import os
import random
import re
import sys



def degreeOfArray(arr):
    # Write your code here
    deg,itemList = arrDegree(arr)
    print(itemList)
    min_subarray = len(arr)
    for item in itemList:
        cut_head = arr[arr.index(item):]
        cut_head.reverse()
        i2 = cut_head.index(item)
        cut_tail = cut_head[cut_head.index(item):]
        min_subarray = min(min_subarray,len(cut_tail))
    return min_subarray



def arrDegree(array):
    degree = 0
    itemList = []
    for item in array:
        d = 0
        for item2 in array:
            if item == item2:
                d+=1
        # degree = d if d>=degree else degree
        # itemList = item if d > degree else itemList
        if d > degree:
            degree = d
            itemList = [item]
        elif d == degree and (item not in itemList):
            itemList.append(item)
        
    return degree,itemList



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = 7

    a = [5,1,2,2,3,1]


    res = degreeOfArray(a)

    print(res)