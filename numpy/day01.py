# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-27 20:40:14
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-29 11:00:00

import numpy as np

# 定义矩阵变量并输出变量的一些属性
# 用np.array()生成矩阵
arr = np.array(
    [[1,2,3],
    [4,5,60]])

print(arr)
# 二维矩阵
print("number of arr dimensions:",arr.ndim)

print("~ ~ ~ shape: ",arr.shape)
print("~ ~ ~ size: ",arr.size)

# 输出结果:
# [[1 2 3]
#  [4 5 6]]
# number of arr dimensions:  2
# ~    ~    ~   shape:  (2, 3)
# ~    ~    ~   size:  6


# 定义一些特殊矩阵
# 指定矩阵数据类型
arr = np.array(
    [[1,2,3],
    [4,5,6]],
    dtype=np.float64)  # 我的电脑是np.int 是int32,还可以使用np.int32/np.int64/np.float32/np.float64

print(arr.dtype)  # float64


# 用np.zeros()生成全零矩阵
arr_zeros = np.zeros((2,3))
print(arr_zeros)

# 用np.ones()生成全一矩阵
arr_ones = np.ones((2,3))
print(arr_ones)

# 生成随机矩阵np.random.random()
arr_random = np.random.random((2,4))
print(arr_random)

# 用np.arange()生成数列
arr = np.arange(6,12)
print(arr)

# 用np.arange().reshape()将数列转成矩阵
arr = np.arange(6,12).reshape((2,3))
print(arr)

# 用np.linspace(开始，结束，多少点划分线段)，同样也可以用reshape()
arr = np.linspace(1,5,3)
print(arr)


# 矩阵运算
arr1 = np.array([1,2,3,6])
arr2 = np.arange(4)

# 矩阵减法,加法同理
arr_sub = arr1 - arr2
print(arr1)
print(arr2)
print(arr_sub)


# 矩阵乘法
arr_multi = arr**3      # 求每个元素的立方,在python中幂运算用**来表示
print(arr_multi)


arr_multi = arr1 * arr2  # 元素逐个相乘
print(arr_multi)


# 维度1*4和4*1矩阵相乘
arr_multi = np.dot(arr1,arr2.reshape((4,1)))
print(arr_multi)


# 维度4*1和1*4矩阵相乘
arr_multi = np.dot(arr1.reshape((4,1)),arr2.reshape((1,4)))
print(arr_multi)


# 三角运算: np.sin()/np.cos()/np.tan()
arr_sin = np.sin(arr1)
print(arr_sin)



# 逻辑运算
# 查看arr1矩阵中哪些元素小于3,返回[ True  True False False]
print(arr1<3)



# 矩阵求和,求矩阵最大最小值
arr1 = np.array([[1,2,3,],[4,5,6]])
print(arr1)
print(np.sum(arr1))  # 矩阵求和
print(np.sum(arr1,axis=0))  # 矩阵每列求和
print(np.sum(arr1,axis=1).reshape(2,1))  # 矩阵每行求和


print(np.min(arr1))  # 求矩阵的最小值
print(np.min(arr1,axis=0))  # 求矩阵最小值的那一行
print(np.min(arr1,axis=1))  # 求矩阵最小值的那一列

print(np.max(arr1))  # 求矩阵最大值
print(np.mean(arr1)) # 输出矩阵平均值,也可以用arr1.men()
print(np.median(arr1))  # 输出矩阵中位数

# 输出矩阵某些值的位置
arr1 = np.arange(2,14).reshape((3,4))
print(arr1)


# 输出矩阵最小值的位置 0
print(np.argmin(arr1))
# 输出矩阵最大值的位置 11
print(np.argmax(arr1))


# 输出前一个数的和,前两个数的和,等等
print(np.cumsum(arr1))
# 输出相邻两个数的差值
print(np.diff(arr1))



arr_zeros = np.zeros((3,4))
# 输出矩阵非零元素位置,返回多个行向量,第i个行向量表示第i个维度
print(np.nonzero(arr_zeros))
print(np.nonzero(arr1))

# 矩阵逐行排序
print(np.sort(arr1))
# 矩阵转置,也可以用arr1.T
print(np.transpose(arr1))

# 将矩阵中小于5的数置5,大于9的数置9
print(np.clip(arr1,5,9))




































