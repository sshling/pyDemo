


"""
 set,集合
    无序，不可重复
    大括号
"""
x=set("hello") #转为 set
#print(x) #{'e', 'l', 'o', 'h'}  # 大括号、无序、去重

#
li=(1,3,5)
x=set(li)  # -> set
li=list(x) # -> list

#set的函数
#print(dir(set))
"""
 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 
 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""



#help(set.add)
#help(set.update)
"""
 add/update
 
 add(...)
    Add an element to a set.
    This has no effect if the element is already present.
 
 update(...)
    Update a set with the union of itself and others.
    从另个集合合并元素
       
"""

"""
 pop/remove/discard/clear
 
 pop()
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.
 remove(member)
    Remove an element from a set; it must be a member.
    If the element is not a member, raise a KeyError.   
 discard(member)
    Remove an element from a set if it is a member.
    --> If the element is not a member, do nothing. 这是与remove(...)的区别
"""
#help(set.clear)


"""
set()创建的是可原地修改的集合
frozenset() 不可原地修改的集合
"""
fset=frozenset('hello')
#print(fset) #frozenset({'l', 'e', 'h', 'o'})


"""
 集合元素：
1. 元素 与 集合：  in
2. 集合 与 集合： 
    ==  !=
    A<B A是子集  
    a.issubset(b)
    b.issuperset(a)

    A|B , 并集  
        A.union(B)
    A&B ,交集    
        A.intersection(B)
    A-B , 差(补), A有B没有的
        A.difference(B)
    对称差集，AB交集取反，即抛去2个集合共有的，剩余元素的集合
      A.symmetric_difference(B)      
"""
A=set('abc')
B=set('abcd')

