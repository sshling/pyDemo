# encoding:utf-8

# import codecs
# codecs.open('file',encoding='utf-8')

# int float str 之外 列表对象 list, 方括号
x = []
print(bool(x) == False)  # 空的
x = [1, 2]
x = ['a', 'c']

# 类似Java中的数组，但有区别，Java中要求元素类型必须一致，类型要提前声明的！


#  索引和切片 , 参考 str

# 反转
x = [1, 2, 3]
print(x[::-1] == [3, 2, 1])  # 玩玩，不推荐使用
print(x == [1, 2, 3])  # 原来的不变的
y = reversed(x)
print(y)  # list_reverseiterator object
print(list(reversed(x)) == [3, 2, 1])

# 操作
# len
# +
# * 重复元素
x = ['a', 'b']
y = x * 3
print(y == ['a', 'b', 'a', 'b', 'a', 'b'])
# in
# max/min()
# > <

# 函数
# apend extend
x = [1, 3]
y = ['a', 'b']
x.extend(y)
print(x == [1, 3, 'a', 'b'])
x = [1, 3]
z = 'ab'  # 字符串当成 字符列表了
x.extend(z)
print(x == [1, 3, 'a', 'b'])
# 列表是可以修改的，这种修改不是复制一个新的，是在原地修改——所以不返回值

x = [1, 2]
x.append(['b', 'd'])
print(x == [1, 2, ['b', 'd']]) # append 团体式扩充 ，extend 是个体化扩充

x = 'python'
print(hasattr(x, '__iter__') == True)  # 判断对象是否可迭代




