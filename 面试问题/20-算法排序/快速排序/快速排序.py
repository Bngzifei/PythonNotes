# -*- coding: utf-8 -*-
def quick_sort(alist, start, end):
    """快速排序"""
    # 递归退出的条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low 为list左边的 从左向右移动的索引值
    low = start
    # high是list右边从右向左移动的索引
    high = end
    # 记住:循环中的判断也是实现过滤的功能.即满足了才执行循环体,
    # 不满足直接跳过循环体.往下执行即可
    while low < high:
        # 如果low与high未重合,high指向的元素不比基准元素小,则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 如果...
        # 将high指向的元素放到low的位置
        alist[low] = alist[high]
        # 如果low和high未重合,low指向的元素比基准元素小.则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后,low与high重合,此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    print(alist)


b = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
quick_sort(b, 0, len(b) - 1)
