# line comment

# 对象三维度：身份(地址) 类型 值
# 数学中的小数 -> 程序中的浮点数

id(3)  # 地址
type(3)

# 变量 ,对象有类型，变量无类型,只是标签
x = 5
x = "hello"
# print(x)

# 超过Int范围的将转换成Long类型

print(5 / 2 == 2.5)
print(2 / 5 == 0.4)

# 浮点数 计算有误差，非常精确 --decimal模块
# fractions模块 有理数

# SciPy , Numerical Python

# 导入模块的2种方式
# import module-name
# from module-name import submodule-name  大模块里有小模块


# 求余数
print(5 % 2 == 1)

# 四舍五入
print(round(1.23456, 3) == 1.235)
print(round(1.23456, 2) == 1.23)

# 常用数学函数及模块
import math

print(math.pi)
print(dir(math))  # dir(module) 查看模块包含的工具

print(help(math.pow))  # help 方法使用方法

# abs

# 运算规则
# lambda
# or and
# not x

# in ,not in
# is ,is not

# < <= > >= != ==
# | ^ &  >> <<
# + - * / %
# +x -x
# ~x 按位翻转
# ** 指数

'''
多行注释1
'''

"""
多行注释
"""

