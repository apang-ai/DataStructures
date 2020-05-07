'''
    队列： 是一系列有顺序的元素的集合，新元素加入在队列的一端， 这一端叫做"队尾(rear)"
          已有元素的移除发生在队列的另一端，叫做“队首(front)”。
    特点： 当一个元素被加入到队列之后，他就从队尾向队首前进，直到他成为下一个即将被移除队列的元素

    先进先出(FIFO)：最新被加入的元素处于队尾，在队列中停留的最长时间的元素处于队首

    ----------------------------------
    rear                        front
    ----------------------------------

    抽象数据类型(ADT):
        Queue()   创建一个空队列， 无需参数， 返回空的队列
        enqueue(item)   将数据项添加到队尾，无返回值
        dequeue()  从队首移除数据项，无需参数，返回值是队首数据项
        isEmpty()  是否队列为空  无需参数  返回值为布尔值
        size()  返回队列中的数据项的个数，无需参数

    
    用python list实现队列
    enqueue     insert()
    dequeue     pop()
'''

# class Queue():
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):

#         self.items.insert(0, item)

#     def dequeue(self):

#         return self.items.pop()

#     def isEmpty(self):

#         return self.items == []

#     def size(self):

#         return len(self.items)

# q = Queue()

# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)

# print(q.size())
# print(q.isEmpty())

# print(q.dequeue())


# q = Queue()

# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# q.dequeue()

#     # =============================
# rear(尾) 3  dog                               front(首)  
#     # =============================


'''
    马铃薯游戏(击鼓传花) 选定一个人作为开始的人，经过num个人，物品在谁手里谁将被淘汰
'''
from pythonds.basic.queue import Queue


name_list = ['红', '明', '强', '丽', '马', '玉', '赵', '三', '四', '五', '六']
num = 7
def send_flower(name_list, num):
    q = Queue()
    for name in name_list:

        q.enqueue(name)

    while q.size() > 1:

        for i in range(1, num):
            q.enqueue(q.dequeue())

        n = q.dequeue()
        print(n)
    return q.dequeue()


print(send_flower(name_list, num))

'''
    模拟打印机
'''


