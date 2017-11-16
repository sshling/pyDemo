# Python 皆对象

# 字符串
x = 'ab c "d"'  # 单引号里有双引号
x = "what's your name"  # 双引号 里 单引
x = 'what\'s your name';  # 转义,让某个符号不再表示某种含义

# 连接
x = 'py' + 'thon'
a = 3
x = x + str(a)
print(x == 'python3')
a = '3'
print(3 == int(a))
a = 2
print(x + repr(a) == "python32")
# repr 是函数,mainly useful for debugging and exploring
# str、int是对象类型
# str 能做的 就不用repr

# 原始字符串 ,r 开头
x = r"c:\news\n"  # c:\news\n

# raw_input -> input(P3)

# x=input("name:")
# print("your' name is:"+x)


# 索引和切片 ，字符串 统称 序列
x = "abcd"
print(x[0] == 'a')
print(x.index('a') == 0)
print(x[0:2] == 'ab')  # 前包含，后不
# 通过索引得到字符的过程：切片
print(x[1:] == 'bcd')
print(x[:2] == 'ab')

print(x[-2:] == 'cd')
print(x[-1] == 'd')
print(x[:-2] == 'ab')

print(len(x) == 4)
print(x[:2] + "cd" == x)  # 列表/元祖都能用+连接
print(x[0] * 2 == 'aa')  # *重复
print(('fe' in x) == False)  # in 某个字符串是不是在另一个字符串内
y = "adbc"
print(max(y) == 'd')  # 计算机内部，每个字符都是有编码的，对应着一个数字

# 2个字符串比较，先将字符串中的符号转化为对应的数字，然后再比较
print(ord('a') == 97)  # ord 字符对应的ASCII值
print(chr(65) == 'A')

# cmp ->  {P3: > or <}
print('ab' < 'ac')
print('ba' > 'ab')
print(x.isalnum() == True)
print(x.isalpha() == True)
print(x.isnumeric() == False)

x = 'a b c'
print(x.split(' ') == ['a', 'b', 'c'])
x.strip()
x.lstrip()
x.rstrip()
x.upper()
x.lower()
print(x.capitalize() == 'A b c')  # 创建新的字符串，原字符串不可变
x = ['a', 'c']
print('#'.join(x) == 'a#c')  # join(self, iterable)

# old 格式化输出字符串
x = "hi,%s age=%d ,weight=%.2f" % ('tom', 22, 21.032)  # 符号 "%s" 是占位符，可以被其它字符串代替
print(x == 'hi,tom age=22 ,weight=21.03')
x = 'hi,%s' % 'tom'
print(x == 'hi,tom')

# 占位符 %
# s  str()
# r  repr()
# c 单个字符
# b  二进制整数
# d  十进制整数
# e  指数（底数为e）
# f  浮点数

# 新格式化
x = "hi {} ".format('tom')
print(x == 'hi tom ')  # 元字符末尾有空格...
x = "a={} b={} c={}".format('tom', 22, 32.232)
print(x == 'a=tom b=22 c=32.232')

x = "a={0} b={1} c={2}".format('tom', 22, 32.232)  # 0起
print(x == 'a=tom b=22 c=32.232')

x = "a={1} b={0} c={2}".format(1, 2, 3)  # 注意序号的变更
print(x == 'a=2 b=1 c=3')

x = 'name={name},age={age}'.format(name='tom', age=23)  # 字典格式化
print(x == 'name=tom,age=23')

# 字符编码，也称为字集码,是把字符集中的字符编码为指定集合中的某一对象，以便文本在计算机中存储和通过通信网络的传递。
# ASCII
# Unicode(万国码/国际码/统一码/单一码)
# UTF-8 针对Unicode的可变长度字符编码，也是一种前缀码，可用来表示Unicode标准中的任何字符，且其编码中的第一个字节与ASCII兼容

# encode/decode
x = '中'
print(len(x) == 1)
print(x.encode('utf-8'))  # b'\xe4\xb8\xad'

# 文件首
# coding：uft-8
