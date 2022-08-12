
# 1. 列表
# 列表由一系列按特定顺序排列的元素组成
# 在Python中，用方括号（[]）表示列表，并用逗号分隔其中的元素。
names = ["curtis1", 21, 178.5]
print(names)

# 1.1 访问列表元素
# 列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）告诉Python即可。要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内。
# 这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。这种约定也适用于其他负数索引。
names = ["curtis1", 21, 178.5]
print(names[0])
print(names[1])
print(names[2])
print(names[0].upper())
# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1
print(names[-1])
print(names[-2])
print(f"My Name Is {names[0].title()}")

# 1.2 修改、添加和删除元素
names = ["curtis1", "curtis2", "curtis3"]
names[0] = 11
print(names)

# 在列表末尾添加元素
# 在列表中添加新元素时，最简单的方式是将元素附加（append）到列表。给列表附加元素时，它将添加到列表末尾。
names.append("curtis4")
print(names)
ints = []
ints.append(1)
ints.append(2)
ints.append(3)
print(ints)

# 在列表中插入元素
ints = [1, 2, 3]
ints.insert(0, 10)
print(ints)
ints.insert(1, 11)
print(ints)

# 从列表中删除元素
ints = [1, 2, 3, 4, 5]
del ints[1]
print(ints)
# 方法pop()删除列表末尾的元素，并让你能够接着使用它
last_int = ints.pop()
print(last_int)
last_int = ints.pop(0)
print(last_int)

# 根据值删除元素
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除
str_vals = ["curtis1", 2, "curtis1", "curtis2", 5]
str_vals.remove("curtis1")
print(str_vals)

# 组织列表
# 方法sort()永久性地修改列表元素的排列顺序
ints = [1, 3, 2, 5, 4]
ints.sort()
print(ints)
ints.sort(reverse=True)
print(ints)

# 使用函数sorted()对列表临时排序
ints = [1, 3, 2, 5, 4]
print(sorted(ints))
print(sorted(ints, reverse=True))
print(ints)

# 倒着打印列表
# 方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用reverse()即可
ints = [1, 3, 2, 5, 4]
ints.reverse()
print(ints)

# 确定列表的长度
# 使用函数len()可快速获悉列表的长度。
ints = [1, 3, 2, 5, 4]
ints_length = len(ints)
print(ints_length)

# 2. 操作列表
## 2.1 遍历列表
# 在for循环后面，没有缩进的代码都只执行一次，不会重复执行。
names = ["curtis1", "curtis2", 21, 22]
for name in names:
    print(f"loop once: {name}")
    print(f"loop twice：{name}")
    # print(names)
print("loop end。")
# Python根据缩进来判断代码行与前一个代码行的关系。

## 2.2 创建数值列表
# Python函数range()让你能够轻松地生成一系列数
ints = range(1, 5)
print(ints)
for int_val in range(1, 5):
    print(int_val)

for int_val in range(5):
    print(int_val)

# 使用range()创建数字列表
ints = list(range(2, 5))
print(ints)

digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

# 切片
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
names = ["curtis1", "curtis2", "curtis3", "curtis4", "curtis5"]
names = names[0:3]
print(names)
names = names[1:2]
print(names)
names = ["curtis1", "curtis2", "curtis3", "curtis4", "curtis5"]
for name in names[0:3]:
    print(name)

# 复制列表
# 4.5 元组
# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
# 然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
citys = ('北京', '上海')
print(citys)

# citys[0] = '11'
# 遍历元组
for city in citys:
    print(city)

# 修改元组变量
# 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组。
citys = ("北京", "上海")
citys = ("北京", "广州")
for city in citys:
    print(city)






