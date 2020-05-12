'''
    LeetCode   面试题08.06   汉诺塔问题
    在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
    (1) 每次只能移动一个盘子;
    (2) 盘子只能从柱子顶端滑出移到下一根柱子;
    (3) 盘子只能叠在比它大的盘子上。

    请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。


    递归：
    1、找出最基础的部分
    2、无线向着最基础的部分靠近
    3、递归函数

    第一步：找出最基础的部分：假设  N = 5 ,  (1,2,3  号杆)  最初都在1号杆


    1号5    借助3号杆移动四个到2号杆   剩下的一个3号杆 （1:0 2:4 3:1）

    2号4个   借助1号杆移动3个到3号杆   剩下一个到1号  （1:1  2:0  3:4）

            借助2号杆移动两个到一号杆

    fromPole  从那个杆子
    withPole  借助那个杆子
    toPole    到那个杆子
    num       移动多少个
    move(num, fromPole, withPole, toPole)

def move(num, fromPole, withPole, toPole):
    if num >= 1:

        move(num-1, fromPole, withPole, toPole)

        moveDisk(fromPole, toPole)

        move(num-1, withPole, toPole, fromPole)


def moveDisk(fromPole, toPole):

    print('移动盘子从',fromPole, '到', toPole)


move(5, 'A', 'B', 'C')

'''



'''
迷宫： 参考LeetCode1210题：穿过迷宫的最好移动次数

1、初始位置尝试向上走一步
2、如果上面走不通则尝试走下面，再开始递归
3、上下都不通，走左边，再开始递归
4、上下都不通，走右边，再开始递归

四种节本情况
1、碰到‘墙壁’， 方格被占用无法通行
2、方格被访问过，为避免陷入循环不在此位置继续寻找
3、碰到边缘， 表示成功
4、四个方向探索失败 游戏失败 

turtle

__init__   用来读取迷宫的数据，初始化迷宫的内部，并找到精灵的初始位置


draw_maze   用来在屏幕上绘制迷宫

update_position  用来更新迷宫的状态和游戏精灵的位置

is_exit  用来判断当前位置是否是出口

'''
import turtle
from turtle import Turtle
# 迷宫的地图：从txt文件中获取, 地图是一个只包含+ 空格 的文件

# 用到的绘制迷宫的符号：+   空格 
# turtle  GUI库绘制迷宫地图
   

class Maze():

    def __init__(self, mazeFileName):

        rowsInMaze = 0
        columnsInMaze = 0
        self.mazeList = []

        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:

            rowList = []
            col = 0
            for ch in line[:-1]:

                rowList.append(ch)

                if ch == 'Q':

                    self.startRow = rowsInMaze
                    self.startCol = col
            rowsInMaze = rowsInMaze+1
            self.mazeList.append(rowList)

            colimnsMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = colimnsMaze

        self.xTranslate = columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        turtle.setup(width=600, height=600)
        turtle.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    # 绘制屏幕
    def draw_maze(self, x, y, color):
        tracer(0)

        self.t.up()
        self.t.goto(x-0.5, y-.5)
        self.t.color('black', color)
        self.t.heading(90)
        self.t.down
        self.t.begin_fill()
        for i in range(4):

            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

        turtle.update()
        turtle.tracer()


mazeFileName = 'DS4_Recursion/maze.txt'

maze = Maze(mazeFileName)

