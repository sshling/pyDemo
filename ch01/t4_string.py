

#双引号包裹 单引号
x="I'am"
#转义
x='I\'m'
#字符串连接
x = 'I'+' am'

a=2
# TypeError: Can't convert 'int' object to str implicitly
#这里 str(a) 将 整数对象 转换为字符串对象，虽然 str 是一种对象类型，但它也能够实现对象类型的转换，起到了一个函数的作用
x='ab'+str(a)
# repr() 是函数，能把结果字符串转化为合法的Python表达式
x='ab'+repr(a)


# repr() str() 区别：
# 大多情况用str()
# repr() ,mainly useful for debugging and exploring.

#原是字符 r
x=r'c:\news'

# input()

