# # 冒泡法
# def bubbleSort(alist):
#     for passnum in range(len(nums)-1, 0, -1):
#         for i in range(passnum):

#             if nums[i] > nums[i+1]:

#                 temp = nums[i]
#                 nums[i] = nums[i+1]
#                 nums[i+1] = temp

# nums = [5,2,3,1,9,0] 
# bubbleSort(nums)
# print(nums)

# 选择排序
# def seletcSort(alist):
#     positionMax = 0
#     for fillslot in range(len(nums)-1, 0, -1):

#         for location in range(1, fillslot+1):
#             if nums[location] > nums[positionMax]:

#                 positionMax = location
#         temp = nums[fillslot]
#         nums[fillslot] = nums[positionMax]
#         nums[positionMax] = temp

# nums = [5,2,3,1]
# seletcSort(nums)
# print(nums)

'''
    给你一个整数数组 nums，请你将该数组升序排列。

    nums = [5,2,3,1]    [1,2,3,5]


    [54,26,93,17,77,31,44,55,20]
    一、冒泡排序:对一个列表多次遍历，比较相邻的两项，并且交换顺序排错的项。
        每对列表进行一次遍历，就有一个最大项排在了正确的位置，大体上讲，
        列表的每一个数据项都会在其相应位置 “冒泡”
        第一次遍历：n-1次
        [54,26,93,17,77,31,44,55,20]    第1次    交换
        [26,54,93,17,77,31,44,55,20]    第2次    不交换
        [26,54,17,93,77,31,44,55,20]    第3次    交换
        [26,54,17,77,93,31,44,55,20]    第4次    交换
        [26,54,17,77,31,93,44,55,20]    第5次    交换
        [26,54,17,77,31,44,93,55,20]    第6次    交换
        [26,54,17,77,31,44,55,93,20]    第7次    交换
        [26,54,17,77,31,44,55,20,93]    第8次    交换
        结果：[26,54,17,77,31,44,55,20,93]
        第二次遍历： n-2次
# 实现冒泡排序
# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):  
#         for i in range(passnum):   
#             if alist[i] > alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#                 # alist[i],alist[i+1] = alist[i+1],alist[i]
# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)
# 假设输入的是一个已经排好序的列表  [17, 20, 26, 31, 44, 54, 55, 77, 93]
# 如果列表整个排序过程没有交换，说明列表已经完成了排序，因此可以通过判断有没有发生交换，改良冒泡排序
# 改良完了之后，就是：短路冒泡排序
# 实现短路冒泡排序
def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):   
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum -1
                
alist = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(alist)
print(alist)
# 练习：[19,1,9,7,3,10,13,15,8,12]  写出第三次遍历之后的列表
'''




'''
    二、选择排序：每遍历一次列表只交换一次数据，也就是进行一次遍历时找到最大的项
        完成遍历后，再把它换到正确的位置

        每次遍历都是找最大值，放在最后
           alist = [26,54,93,17,77,31,44,55,20]
        第1次遍历   [26,54,20,17,77,31,44,55,93]   93
        第2次遍历   [26,54,20,17,55,31,44,77,93]   77
        第3次遍历   [26,54,20,17,44,31,55,77,93]   55
        第4次遍历   [26,31,20,17,44,54,55,77,93]   54
        第5次遍历   [26,31,20,17,44,54,55,77,93]   44
        第6次遍历   [26,31,20,17,44,54,55,77,93]   31
        第7次遍历   [20,17,26,31,44,54,55,77,93]   26
        第8次遍历   [17,20,26,31,44,54,55,77,93]   20


        def seletcSort(alist):
            for fillslot in range(len(alist)-1,0,-1):
                positionMax = 0
                
                for location in range(1,fillslot+1):
                    if alist[location] > alist[positionMax]:
                        positionMax = location

                temp = alist[fillslot]
                alist[fillslot] = alist[positionMax]
                alist[positionMax] = temp

        alist = [26,54,93,17,77,31,44,55,20]
        seletcSort(alist)
        print(alist)
'''

'''
    插入排序：总是保存一个位置。靠前的已经排序好的字表[54] [26,93,17,77,31,44,55,20],然后每一个新的数据项被‘插入’到前面的子表中，配好的第一字表就增加了一项

    alist = [54,26,93,17,77,31,44,55,20]
    分成两个表 [54] [26,93,17,77,31,44,55,20]
    第1步  [26, 54]                                [93,17,77,31,44,55,20]      插入26
    第2步  [26, 54, 93]                            [17,77,31,44,55,20]         插入93
    第3步  [17, 26, 54, 93]                        [77,31,44,55,20]            插入17
    第4步  [17, 26, 54, 77, 93]                    [31,44,55,20]               插入77
    第5步  [17, 26, 31, 54, 77, 93]                [44,55,20]                  插入31
    第6步  [17, 26, 31, 44, 54, 77, 93]            [55,20]                     插入44
    第7步  [17, 26, 31, 44, 54, 55, 77, 93]        [20]                        插入55
    第8步  [17, 20, 26, 31, 44, 54, 55, 77, 93]    []                          插入20

def insertSort(alist):

    for index in range(1, len(alist)):

        currentValue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentValue:

            alist[position] = alist[position -1]

            position = position -1

            alist[position] = currentValue


alist = [54,26,93,17,77,31,44,55,20]

insertSort(alist)

print(alist)

''' 


'''
    四、希尔排序(缩小间隔排序): 以插入排序为基础，将原来要排序的列表划分成一些子列表，在对每一个子列表执行插入，从而实现对插入排序的性能的改进。
    关键：划分子列表的特定的方法

    alist = [54,26,93,17,77,31,44,55,20]

    1、以3为间隔来划分，分为3个子列表
        [54,17,44]   [17,26,93,44,77,31,54,55,20]
        [26,77,55]   [17,26,93,44,55,31,54,77,20]
        [93,31,20]   [17,26,20,44,55,31,54,77,93]

        再进行标准插入排序 [17] [26,20,44,77,31,54,55,93]
        优化了比对和移动的次数

    2、以2为间隔，划分了5个子列表
        [54,77]   [54,26,93,44,20,77,31,54,55]
        [26,31]   [54,26,93,44,20,77,31,54,55]
        [93,54]   [54,26,54,44,20,77,31,93,55]
        [44,55]   [54,26,54,44,20,77,31,93,55]
        [20]

# Leetcode  第147题 对列表进行排序
# def shellSort(alist):
#     sublistcount = len(alist)//3
#     for i in range(sublistcount):
#         Sort =  gapInsertionSort(alist, i, sublistcount)
#     print('希尔排序后: ', Sort )

#     sublistcount = sublistcount//3

# 特定间隔分子列表，然后执行标准插入排序
def gapInsertionSort(alist, gap):

    gap2 = len(alist)//gap
    

    while gap2:
        # print('gap2的值为：',gap2)
        for i in range(gap2, len(alist)):
            # print('i的值为：', i)

            while i >= gap2 and alist[i-gap2] > alist[i]:
                alist[i-gap2], alist[i] = alist[i], alist[i-gap2]
                # print(alist)

                i -= gap2
        gap2//=gap

       

    return alist


alist = [54,26,93,17,77,31,44,55,20]

print(gapInsertionSort(alist, 3))

'''


'''
    五、 归并排序(mergeSort)
        具体做法：递归算法，不断地将列表拆分成一半。
        如果列表为空或者只有一个元素，那么根据定义，他就被排好了
        alist = [54,26,93,17,77,31,44,55,20]

        第一次拆分： [54,26,93, 17]  [77,31,44,55,20]
        第二次拆分： [54,26][93,17]   [77,31][44,55,20]
        第二次拆分： [54] [26] [93] [17]  [77] [31] [44] [55, 20]
        第四次拆分： [54] [26] [93] [17]  [77] [31] [44] [55] [20]

        [54] [26] [93] [17]   [77] [31]  [44] [55] [20]
        [26, 54]    [17, 93]   [31, 77]        [20, 55]
          [17, 26, 54, 93]     [31, 77]    [20, 44, 55]
          [17, 26, 54, 93]          [20, 31, 44, 55, 77]
                  [17,20,26,31,44,54,55,77,93]
            
'''
def mergeSort(alist):

    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j< len(righthalf):

            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]

                i += 1
            
            else:

                alist[k] = righthalf[j]

                j += 1
            
            k+=1
        
        while i< len(lefthalf):

            alist[k] = lefthalf[i]
            i+=1
            k+=1
        
        while j < len(righthalf):

            alist[k] = righthalf[j]
            j+=1
            k+=1


alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


'''
    六、 快速排序
'''
