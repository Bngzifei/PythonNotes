# -*- coding: utf-8 -*-

# bubble:n. 气泡，泡沫，泡状物；透明圆形罩，圆形顶
# 在打印图形中,外循环控制行数,内循环控制列数<即一行有几个元素>
def bubble_sort(nums):
    # 注意:这里的len(nums) - 1不是通常意义的生成元素的索引.形式一样,表示的含义不同.
    for i in range(len(nums) - 1):  # 外循环控制排序次数,因为是相邻两个进行比较,所以比较次数就是 元素个数 - 1<类似于5个手指有4个空隙>
        for j in range(len(nums) - i - 1):  # 内循环控制列表下标,即控制列表元素
            # len(nums) - i - 1 这里的含义是每次比较之后,需要进行比较的元素的索引.
            # 并不是通俗理解的元素索引.是每一次排序之后需要进行排序的元素的索引.
            # 因为排过序的元素在下次排序的时候不需要进行排序操作.
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print('----', nums)
        print('****', nums)

    # 循环结束,返回排序结果
    return nums


list1 = [2, 1, 0, 5, 8, 9]
print(bubble_sort(list1))
# 输出:[2, 3, 4, 5, 6, 9, 12, 56]
