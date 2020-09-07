'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:

    # 方法一 循环迭代查找
    def judgeInArray(self, target, array):
        if not array:
            return
        for item in array:
            if target in item:
                return True
        else:
            return False

    # 方法二 从右上（或左下）开始搜索
    #        如果数组中的数比输入的数大则向左移动
    #        如果数组中的数比输入的数小则向下移动

    def judgeInArray_02(self, target, array):

        row = len(array)
        col = len(array[0])
        i = 0
        j = col - 1
        while i < row and j >= 0:
            if array[i][j] > target:
                j -= 1
            if array[i][j] < target:
                i += 1
            else:
                return True
        return False
