# 第一章 Python基础数据类型

## 第一集 Python核心基础知识之数据类型

- Python中的数字类型支持哪几种数值？

  - 整型：可正可负，不带小数点。在Python3中，整型没有大小限制，所以也可以存储长整型

  - 浮点型：可正可负，带小数点，可以使用科学计数法表示 1.1e2 = 110

    print(1.1e2)

  - 检查数字类型可以使用type()

    print(type(114514))

    ![](E:\Python\笔记截图\第一章\图片类型.png)

  - 复数：复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型，因用的较少，不做过多阐述，有兴趣可自行拓展（懒狗你不许学习Python.jpg）

- 数字类型有什么特点？

  - 数字类型这种类型是不可变的，如果改变数字数据类型的值，将重新分配内存空间。（详情见数字类型的特点.drawio）		![](E:\Python\笔记截图\第一章\改变分配空间.png)

在这里我使用了id函数来查看值变化前后的id的地址是否发生了变化

当a = 1时，内存中存储的地址为140714655838464；当a=2时，内存中存储的地址为140714655838496。可见改变数字数据类型的值，将重新分配内存空间。

## 第2集 Python核心基础知识之整数

**二进制：**它的基数为2，进位规则是“逢二进一”

十进制快速转换为其他进制的转换规则：用十进制数，每次除与对应的数，记下余数，直到最终结果为

0，之后将余数倒过来写，如果是16进制，余数大于10，转换成字母即可

将十进制的21，转换成二进制表示

![image-20240212094616159](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20240212094616159.png)将余数倒过来写一起，就是该数字的二进制表示方式，即10101

**八进制：**它的基数为8，进位规则是“逢八进一”

**十进制：**日常中使用的最多的就是10进制

**十六进制：**它的基数为16，进位规则是“逢十六进一”，跟其他几个进制不同的地方是该进制大于十的时

候，会使用A-F进行表示



既然在计算机的世界里有那么多种进制，如果输入10，Python如何进行分辨？各种进制之间如何进行转换？

- 在Python，如果没有显式指定进制，那么所有的数字默认是按10进制算

  使用如下方式显式指定进制

  | **二进制**                    | 八进制                         | 十进制 | 十六进制              |
  | ----------------------------- | ------------------------------ | ------ | --------------------- |
  | 前面加0b或0B（0为阿拉伯数字） | 0o或0O（前阿拉伯数字，后字母） | 默认   | 0x或0X（阿拉伯数字0） |

- 进制之间的转换

| 原进制（下） 待转换进制（右） | 二进制    | 八进制    | 十进制         | 十六进制  |
| ----------------------------- | --------- | --------- | -------------- | --------- |
| 二进制                        | 无        | oct(0b10) | int('0b10',2)  | hex(0b10) |
| 八进制                        | bin(0o10) | 无        | int('0o10',8)  | hex(0o10) |
| 十进制                        | bin(10)   | oct(10)   | 无             | hex(10)   |
| 十六进制                      | bin(0x10) | oct(0x10) | int('0x10',16) | 无        |



## 第3集Python核心基础知识之布尔类型及bool函数

什么是布尔类型？

- 对与错、是与非、0和1（不是那个0和1！！！）、正与反，都是传统意义上的布尔类型，在Python中，统一使用True和False来表示布尔类型

- 在布尔类型一般用于表示条件是否成立，成立用True，不成立用False

- 布尔类型是数字类型的一个子集

- 在Python中，bool函数可以用来测试一个表达式的布尔值结果

  bool(0)、bool(-1)、bool(0b10)、bool('')..............
  
- 可以使用print(isinstance(a,int))判断a的数据类型是否为int

  例如：a = 15
  print(isinstance(a, int))

  ![判断a的数据类型](E:\Python\笔记截图\第一章\判断a的数据类型.png)

  

## 第4集 Python核心基础知识之字符串及其编码

**字符串的定义**：字符串是由数字、字母、符号组成的一串字符。它是编程语言中表示文本的数据类型。

在Python中，使用双引号、单引号、三引号括起来的一系列字符就是字符串,无论是使用单引号还是双引号，都必须成对出现.

```
计算机中储存的信息都是用二进制数表示的；而我们在屏幕上看到的英文、汉字等字符是二进制数转换之后的结果。通俗的说，按照何种规则将字符存储在计算机中，如'a'用什么表示，称为"编码"；反之，将存储在计算机中的二进制数解析显示出来，称为"解码".
```

**字符常见的字符集有哪些？**

- **ASCII**

  计算机一开始是外国人发明的，他们日常使用就是一些日常符号加上大小写的字母、数字。所以在字符

  集的设计上，也只兼容这样的一些字符。

  ![ASCII控制字符](E:\Python\笔记截图\第一章\ASCII控制字符.png)

![ASCII显示字符](E:\Python\笔记截图\第一章\ASCII显示字符.png)

- GBXXXX

  ACSII码那玩意只能存英文，那国人咋办？弄一套自己中文编码呗。所以GB2312编码规则出现，它所收

  录的汉字已经覆盖中国大陆99.75%的使用频率。对于人名、古汉语等方面出现的罕用字，GB2312不能

  处理，所以有了GBK编码。（漂亮滴很呐~）

- Unicode

  主要的编码方式有：UTF-32、UTF-16、UTF-8（最常用的一种）

```
关于字符集的更多详情，可参考：

https://www.cnblogs.com/skynet/archive/2011/05/03/2035105.html#*2.2.*GBXXXX%E5%AD%

97%E7%AC%A6%E9%9B%86&%E7%BC%96%E7%A0%81
```

Python 3版本中，所有的字符串都是使用Unicode编码的字符串序列

字符串的特性：不可变，如果改变字符串的值，相当于重新分配了空间



## 第5集 Python核心基础知识之单引号、双引号、三引号与转义字符串

**单引号、双引号的使用场景**

一般情况下，如果我们要表示字符串，使用单引号或双引号括起来基本没啥区别，但是，当字符串中带

有单引号或双引号时，我们可能需要使用转义字符。但是，此时字符串看起来并不优雅，此时可以考虑

如下情况

当字符串中有单引号时，使用双引号括起来

当字符串中有双引号时，使用单引号括起来



**在**Python**中，当输入的字符串比较多，需要换行的时候怎么办？**

我们可以使用成对出现的三个单引号，将字符串括起来即可



在Python中，如果某些字符本身有特殊含义或无法使用ASCII码进行表示的时候，需要对其进行转义操

作，一般用单一反斜杠 \ 进行转义



常见的转义字符

| 转义字符 | 含义         |
| -------- | ------------ |
| \a       | 发出系统铃声 |
| \'       | 单引号       |
| \n       | 换行         |
| \\       | 反斜杠       |
| \"       | 双引号       |
| \b       | 退格         |
| \n       | 换行         |
| \t       | 纵向制表符   |
| \v       | 横向制表符   |
| \r       | 回车         |
| \f       | 换页         |



## 第6集 Python核心基础知识之字符串常见的操作

- 获取字符串中的某一部分

  | 操作                     | 输出             |
  | ------------------------ | ---------------- |
  | “my name is Huang"[0]    | m                |
  | “my name is Huang"[3]    | n                |
  | “my name is Huang"[-1]   | g                |
  | “my name is Huang"[-2]   | n                |
  | “my name is Huang"[0:2]  | my               |
  | “my name is Huang"[0:-1] | my name is Huan  |
  | “my name is Huang"[0:15] | my name is Huang |
  | “my name is Huang"[0:22] | my name is Huang |
  | “my name is Huang"[0:]   | my name is Huang |
  | “my name is Huang"[:7]   | my name          |

- 字符串的格式化

  在字符串中，可以将一个值插入到有格式化符号的地方

​		如：

​		print("My name is %s and my age is %d" %("Huang",24))

- 常用的格式化符号

  | **符合** | **作用**                             |
  | -------- | ------------------------------------ |
  | %c       | 格式化字符及其ASCII码                |
  | %s       | 格式化字符串                         |
  | %d       | 格式化整数                           |
  | %f       | 格式化浮点数字，可指定小数点后的精度 |

  



