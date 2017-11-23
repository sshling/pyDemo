x = {}
x = {'a': 2, 'b': 3}
# print(type(x))  #<class 'dict'>
# 增加 KV
x['c'] = 4
# print(x)
id(x)  # 内存地址 ，字典可以原地修改

# 元组构建字典
x = (['a', 1], ['b', 2])
d = dict(x)
# print(d) #{'a': 1, 'b': 2}

#
d = dict(a=2, b=4)
# print(d) #{'b': 4, 'a': 2}

#
d = {}.fromkeys(('a', 'b'), 22)
# print(d) #{'b': 22, 'a': 22}

"""
字典的key必须是不可变对象

 基本操作
 len(d)
 d[k]
 d[k]=v
 del d[k]
 k in d
 
"""

"""
 字典实现格式化字符串
"""
d = {'wait': 10}
s = "###wait=%(wait)s###" % d  # %(wait)s
s = "###wait=%(wait)d###" % d  # %(wait)d
# print(s)


"""
 相关概念： 关联数组、映射、散列表
"""

"""
 字典函数： 
"""
# copy deepcopy
a = 5
b = a  # 对象有类型，变量无类型，变量其实是一个标签， a,b都是指向同一内存地址
# print(id(a)==id(b))

x = {'a': 2}
d = x.copy()  # 浅拷贝 ，没有解决深层次
# print(id(x) != id(d))

d1 = {'a': [1, 3]}
d2 = d1.copy()
d1['a'].remove(3)
# print(d2) #{'a': [1]}

import copy

d3 = {'a': [1, 3]}
d4 = copy.deepcopy(d3)
d3['a'].remove(3)
# print(d4) #{'a': [1, 3]}

"""
 clear(dict) ,remove all items from dict
 dict={}
"""

"""
 dict.get() , dict['key'] 区别
"""
d = {'a': 3}
print(d.get('a') == 3)
print(d.get('b', 4) == 4)  # 默认值
x = d.setdefault('c', 5)  # 若存在c这个key，则返回值;否则设置值为5且返回,
# print(x) # 5
# print(d) #{'c': 5, 'a': 3}

"""
 items/
 keys
 values
"""


