# 注册牛客网  LeetCode（必刷）
# 如果a+b+c = 1000并且 a^2 + b^2 = c^2, 求出所有a, b, c 可能的组合

# 解决一个问题时间短的算法更好

# 第一种 三重循环
# import time

# start_time = time.time()

# for a in range(0, 1001):

#     for b in range(0, 1001):

#         for c in range(0, 1001):

#             if a+b+c == 1000 and a**2 + b**2 == c**2:

#                 print("a: %d, b:%d, c: %d"%(a,b,c))

# end_time = time.time()

# print('运行时间： %f'%(end_time-start_time))

'''
    a: 0, b:500, c: 500
    a: 200, b:375, c: 425
    a: 375, b:200, c: 425
    a: 500, b:0, c: 500
    运行时间： 127.097926
'''

# 为了让时间更短 提出第二种算法 优化  双重循环

# import time 

# start_time = time.time()

# for a in range(0, 1001):

#     for b in range(0, 1001):

#         c = 1000 - a - b

#         if a**2 + b**2 == c**2:

#             print("a: %d, b:%d, c: %d"%(a,b,c))

# end_time = time.time()

# print('运行时间： %f'%(end_time-start_time))

'''
    a: 0, b:500, c: 500
    a: 200, b:375, c: 425
    a: 375, b:200, c: 425
    a: 500, b:0, c: 500
    运行时间： 1.135281
'''

# 思考可以从哪些角度去优化程序




'''
    1、什么是算法？
        算法就是独立存在的一种解决问题的方法和思想！

    2、算法的五大特性
        输入： 算法具有0个或者多个输入
        输出： 算法至少有1个或者多个输出
        有穷性： 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
        确定性：算法中的每一步都有确定含义，不会出现二义性。
        可行性：算法的每一步都是可行的（每一步都能够执行有限的次数完成）

    3、 算法效率的衡量
        实现算法程序执行的时间可以反映出来算法的效率
        单纯的依靠运行的时间来比较算法的优劣不一定是客观准确的（程序的运行离不开计算机环境，所以和硬件， 操作系统有关系的）

    4、 最终算法用什么衡量？
        时间复杂度

    5、 表示法 大o记法

        假设计算机执行算法的每个基本操作的时间是固定的一个时间单位，那么有多少个基本操作就代表会花费多少时间单位，虽然对于不同的机器环境而言， 确切的时间单位是不同的， 但是对与算法进行多少个基本操作在规模数量级上是相同的，因此，可以忽略机器的环境而客观的反应算法的时间效率
        对于算法的时间效率，用“大o记法”
        o(n^3)         100n^2    1000n^2
        o(n^2)

    6、 时间复杂度分类
        最优时间复杂度：算法完成工作最少需要多少基本操作(过于理想化， 没什么参考价值)
        最坏时间复杂度： 算法完成工作最多需要多少基本操作(提供了一种保障， 表明了算法在此程度的基本操作中一定能完成工作)
        平均时间复杂度： 算法完成工作平均需要多少基本操作(对算法整体一个全面的评价，但是这种衡量方式没有保障)

        我们关注算法的最坏情况 ！！！   --->  最坏时间复杂度

    7、 时间复杂度的几条基本的计算规则
        基本的操作： 只有常数项，认为其时间复杂度为o(1)

        顺序结构： 时间复杂度按加法进行计算

        循环结构： 时间复杂度按乘法进行计算 

        分支： 取最大值

        判断一个算法的效率时只需要关注操作数量的最高次项，其他次要项和常数项可以忽略
        没有特殊情况下，我们分析的都是最坏时间复杂度

    8、 练习
        12                          o(1)
        2n +3                       o(n)
        3n^2 + 2n +1                o(n^2)
        5log n + 20                 o(log n)
        2n + 5nlog n + 20           o(nlog n)
        1000n^2 + 2*n^3 + 4         o(n^3)
        2^n                         o(2^n)

        o(1) < o(log n) < o(n) < o(nlog n) < o(n^2) < o(n^3) < o(2^n) < o(n!) < o(n^n)
    
    9、 练习： 求前n个正整数的和(高斯算法)
'''
import time

# def sum_of_n(n):
#     start_time = time.time()

#     the_sum = 0
#     for i in range(1, n+1):

#         the_sum += i

#     end_time = time.time()
#     # time_t = end_time-start_time
#     the_sum_i=end_time-start_time
#     return the_sum, the_sum_i

# for i in range(0, 5):
#     print(sum_of_n(100000000))



# def sum_of_n_2(n):
    

    
    # return (n*(n+1))/2

# start_time = time.time()
# print(sum_of_n_2(100000000))
# end_time = time.time()

# print(end_time-start_time)


'''
练习：编写函数求出列表中的最小值，
要求:  函数1： o(n^2)    两两比较
       函数2： o(n)     设置一个临时变量, 更优化的算法就是把临时变量设置成列表中的第一个元素

'''
my_list = [1000,3,4,9,5,8,100]

def get_min(my_list):

    for i in range(len(my_list)):
        print('i:%d'%i)
        for j in range(len(my_list)):
            print('j:%d'%j)
            if my_list[i] > my_list[j]:
                
                break    
            else:
                return my_list[i]
                
    
print(get_min(my_list))

# def get_min2(my_list):
#     min_num = my_list[0]

#     for i in my_list:

#         if i < min_num:

#             min_num = i

#     return min_num

# print(get_min2(my_list))
    


# 作业 计算前1000个 正整数的和（2种算法）

# 第一种算法

# import time 

# start_time = time.time()

# sum = 0

# for i in range(0, 1001):

#     sum += i

# print('sum的值：%d'%sum)

# end_time = time.time()

# print('运行的时间：%f'% (end_time-start_time))

'''
    sum的值：500500
    运行的时间：0.001076
'''

# 第二种
# import time 

# start_time = time.time()

# sum = 500

# for n in range(0, 500):

#     sum += (0 + n) + (1000 - n)


# print('sum的值：%d'%sum)

# end_time = time.time()

# print('运行的时间：%f'% (end_time-start_time))


'''
    sum的值：500500
    运行的时间：0.001017
'''