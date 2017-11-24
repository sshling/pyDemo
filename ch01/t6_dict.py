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
 items , list of k-v pairs,as 2-tuples
    Python 3’s changes is that  items() now return iterators,
     and a list is never fully built. The iteritems() method is also gone,
    
 keys,
 
 values,
"""
x={'a':1,'b':3}
x2=x.items()
#print(type(x2)) #<class 'dict_items'>
#print(x2)  #dict_items([('b', 3), ('a', 1)])


"""
 list :
    list.remove(item) ,参数为元素
    list.pop(idx)   ,参数为索引
    
 pop, popitem
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised
    
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.
        不是最后元素，dict无序，也就没有最后和最先，是随机删一个，并将删除的返回
    
 dict是无序的   
"""
#help(dict.pop)
#help(dict.popitem)


#help(dict.update)
"""
 D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
"""

help(dict.has_key)
"""
some_dict.keys() & another_dict.keys()
    in Python 3.x. This returns the common keys of the two dictionaries as a set.

[key for key in some_dict if key in another_dict]

P3 remove dict.has_key() – use the in operator instead.   
    d = {'a': 1, 'b': 2}
   'a' in d
    
"""

"""
学过的对象类型归纳：
可索引的, list/str ,有index所以元素可重复
可变的, list/dict , 元素/键值对 可以原地修改
不可变的 , str/int ,不能原地修改
无索引序列的 ,dict, 元素无序！
"""