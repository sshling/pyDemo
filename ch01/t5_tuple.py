# 元组, 圆括号，逗号 ，也是序列，类似列表/字符串
# 特点：
# 元素不能更改，似字符串
# 元素可以是任何类型，似 list
x = (3)
print(type(x))  # <class 'int'>
x = (3,)
print(type(x))  # <class 'tuple'>
# 加了逗号才是 tuple


# 列表 元组间转化： list()/tuple()
list = [1, 3, 5]
#print(type(list)) #<class 'list'>
tuple = tuple(list)
#print(type(tuple)) #<class 'tuple'>
list=list(tuple) #


#场景
# 不变集
# 做字典的key--不可变 ,但list不可以