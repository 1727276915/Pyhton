# - Python中的数字类型支持哪几种数值？
#   - 整型：可正可负，不带小数点。在Python3中，整型没有大小限制，所以也可以存储长整型
#   - 浮点型：可正可负，带小数点，可以使用科学计数法表示 1.1e2 = 110
# print(1.1e2)
#     检查数字类型可以使用type()
print(type(114514))
#   - 复数：复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型，因用的较少，不做过多阐述，有兴趣可自行拓展（懒狗你不许学习Python.jpg）
# - 数字类型有什么特点？
#   - 数字类型这种类型是不可变的，如果改变数字数据类型的值，将重新分配内存空间。
a = 1
print(id(a))
a = 2
print(id(a))
