'''
前序：首先访问根节点，然后递归低做左侧子树的前序遍历，随后是右子侧树的递归前序遍历（根左右）
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        print(tree.getLeftChild())
        print(tree.getRightChild())
中序：递归的对左子树进行一次遍历，访问根节点，最后递归遍历右子树（左根右）
def inorder(tree):
    if tree:
        print(tree.getLeftChild())
        print(tree.getRootVal())
        print(tree.getRightChild())
后序：递归地对左子树和右子树进行后续遍历，然后访问根节点（左右根）
def postorder(tree):
    if tree:
        print(tree.getLeftChild())
        print(tree.getRightChild())
        print(tree.getRootVal())
'''

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def buildParseTree(fpexp):

    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)

    for i in fplist:

        if i == '(':
            # 如果当前的符号是"("，添加一个新节点作为当前节点的左子节点，并下降到左子节点
            eTree.insertLeft('')
            pStack.push(eTree)
            eTree = eTree.getLeftChild()

        elif i not in ['+','-','*','/', ')']:
            # 如果当前符号是数字，将当前节点的根值设置为该数字并返回该节点
            eTree.setRootVal(int(i))
            parent = pStack.pop()
            eTree = parent

        elif i in ['+','-','*','/']:
            eTree.setRootVal(i)
            eTree.insertRight('')
            pStack.push(eTree)
            eTree = eTree.getRightChild()

        elif i == ')':
            
            eTree = pStack.pop()

        else:

            raise ValueError

    return eTree



fpexp = '( ( 7 + 3 ) * ( 5 - 2 ) )'
parseTree = buildParseTree(fpexp)
# parseTree.postorder()
# parseTree.getLeftChild().postorder()

# 定义一个函数，使用以上的构建函数，计算出完全表达式 ( ( 7 + 3 ) * ( 5 - 2 ) )  的结果
# 左子树+右子树
import operator

def evaluate(parseTree):

    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    if leftChild and rightChild:
        result = opers[parseTree.getRootVal()](evaluate(leftChild), evaluate(rightChild))
        return result
 
    else:
        return parseTree.getRootVal()

print(evaluate(parseTree))



# 练习 使用中序遍历  恢复表达式的完全括号版本

def printexp(tree):

    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str( tree.getRootVal() )
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    
    return sVal

print(printexp(parseTree)

# 重点 二叉树的前序 中序  后序

# LeetCode:  144 题， 94题  145题

# [1, null,2,3] --> tree --> []