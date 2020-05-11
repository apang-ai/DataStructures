'''
    那些问题适合递归解决
    怎么用递归的方式写程序

    *****   递归的三大法则
    递归也是一种迭代

    一、 什么是递归
        定义：递归是一种解决问题的方法， 它把一个问题分解为越来越小的子问题,直到问题的规模小到可以被很简单直接解决。

        通常为了达到分解的问题的效果，递归过程中要引入一个***调用自身的函数***


        [1,2] [3,3] [6,4]




    计算 [1,2,3,4,5,6,7]的和

    迭代求和
    def list_num(my_list):

    the_sum = 0
    for num in my_list:

        the_sum += num
    return the_sum

print(list_num([1,2,3,4,5,6,7]))


    不能使用循环，计算和
    (((1+2)+3)+4)  

    列表中的第一个元素和剩余所有的元素列表的和之和
    listSum(numlist) = first(numList)+listSum(rest[numList])

    转换成Python

    numList[0] + numList[1:]

    # 递归函数
    def listSum(numList):
        # 函数结束运行的必要条件
        if len(numList) == 1:

            return numList[0]
        else:

            return numList[0] + listSum(numList[1:])

    print(listSum([1,2,3,4,5,6,7]))


    二、递归的三大定律
        1、递归算法必需有个基本结束条件（成都为1的列表）
        2、递归算法必须改变自己的状态并向基本结束条件演进
        3、递归算法必需递归地调用自身（核心）

    三、 练习
        1、用list_sum 计算[2,4,6,8,10]  要进行多少次递归调用
        2+sum(4,6,8,10)
        4+sum(6,8,10)
        6+sum(8,10)
        8+sum(10)
        2、 计算某个数的阶乘的递归算法（最适合的基本结束条件）
        # 0的阶乘等于1
        def fact(num):

            if num == 1 or num == 0:

                return 1
            else:
                return num*fact(num-1)

        print(fact(1))

    四、递归  LeetCode  第405题
        给定一个整数， 编写一个算法将这个数转换成为十六进制数。对于负整数，我们同城使用补码的运算方式

        给定一个整数，转换成任意进制表示的字符串格式

        769  转换成 字符串  769

        str = '0123456789'

        769/10   =   76    9
        76/10    =   7     6
        7/10     =   0     7

        str[9]+str[6]+str[7]
        # 2, 8, 10, 16
        def to_str(num, base):

            convert_str = '0123456789ABCDEF'

            if num<base:

                return convert_str[num]
            
            else:

                return to_str(num//base, base)+convert_str[num%base]

        print(to_str(769, 10))
        print(to_str(769, 2))
        print(to_str(769, 8))
        print(to_str(769, 16))



        301
        3*16^2+0+1*16^0

        1401
        1*8^3+4*8^2+0+1*8^0

        # 967 => 769   栈     后进先出

            --------------
        底   9   6    7     顶 769
            --------------

        可以用栈的方式实现递归
'''
from pythonds.basic.stack import Stack

s = Stack()
# 2, 8, 10, 16
def to_str(num, base):

    convert_str = '0123456789ABCDEF'
    while num>0:
        if num < base:

            s.push(convert_str[num])
        
        else:
            s.push(convert_str[num%base])

            # return to_str(num//base, base)
        num = num//base

    result = ''
    while not s.isEmpty():
        result += s.pop()

    return result

print(to_str(769, 10))
print(to_str(769, 2))
print(to_str(769, 8))
print(to_str(769, 16))







