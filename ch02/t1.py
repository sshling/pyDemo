print('运算符')
"""
 + - * /
 %  取余
 // 取整除
 ** 冥
"""

"""
 比较...:
 ==
 !=
 >
 >=
 <
 <=
"""

"""
 逻辑...:
 and 
 or
 not
"""


def x_setvalue():
    a = 2
    c = d = 2  # 链式赋值
    print(id(c) == id(d))  # 指向同一对象
    print(c is d)  # 另外的方法 is


"""
 复合赋值:
 += 
"""

"""
 语句：循环/条件/
"""


def x_if():
    a = 2
    if a == 2:
        print('a=2')


def x_elif():
    if a < 2:
        print("a<2")
    elif a == 2:
        print("a=2")
    else:
        print("a>2")


def x_pass():
    '''
        TODO
    :return:
    '''
    pass


def x_three():
    """
     三元操作：
     A=Y if X else Z
     1. X=True ,A=Y
     2. X=Flase, A=Z
    """
    a = 2
    x = 3 if a > 2 else 4
    print(x == 4)


def x_for():
    li = list('hello')
    for i in li:
        print("for list->" + i)

    dict = {'a': 1, 'b': 3}
    for k, v in dict:
        print('k,v=' + k + "," + v)


def x_assert():
    a = 2
    assert a == 2


def x_for_range():
    # start,stop,step
    step = 3
    for n in range(1, 10, step):
        print(n)


def x_for_dict():
    d = {'a': 'aa', 'b': 'bb'}
    for k in d:
        print("raw:"+k + "->" + d[k])
    for k,v in d.items():
        print("kv:"+k+"->"+v)

#跟老齐学python p128
x_for_dict()
