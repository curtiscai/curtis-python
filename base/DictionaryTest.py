
# 字典
# 使用字典
# 在Python中，字典是一系列键值对。每个键都与一个值相关联，你可使用键来访问相关联的值。
# 与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
dict = {"name": "curtis", "age": 21}
# print(dict[0])
print(dict["name"])
print(dict["age"])

# 添加键值对
dict = {"name": "curtis", "age": 21}
dict["height"] = 171.5
dict["weight"] = 70
print(dict)

# 先创建一个空字典
dict = {}
dict["height"] = 171.5
dict["weight"] = 70
print(dict)

# 修改字典中的值
dict = {"name": "curtis", "age": 21}
dict["name"] = "curtis2"
dict["age"] = 22
print(dict)

# 删除键值对
dict = {"name": "curtis", "age": 21}
del dict["age"]
print(dict)

# 使用get()来访问值
# 使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的键不存在就会出错。
dict = {"name": "curtis", "age": 21}
# print(dict["height"])
name = dict.get("name")
print(name)
height = dict.get("height")
# 调用get()时，如果没有指定第二个参数且指定的键不存在，Python将返回值None。这个特殊值表示没有相应的值。None并非错误，而是一个表示所需值不存在的特殊值
# None
print(height)

# 遍历字典
# 遍历字典的所有键值对，也可仅遍历键或值
dict = {"name": "curtis", "age": 21, "weight": 70}
for k,v in dict.items():
    print(f"key: {k}, value: {v}")
for k in dict.keys():
    print(f"key: {k}")
for v in dict.values():
    print(f"value: {v}")

# 嵌套
# 字典列表
dict_1 = {}
dict_1["name"] = "curtis1"
dict_1["age"] = 21
dict_2 = {}
dict_2["name"] = "curtis2"
dict_2["age"] = 22
dict_list = []
dict_list.append(dict_1)
dict_list.append(dict_2)
print(dict_list)
# 在字典中存储列表
province_list = ["河北"]
city_list = ["石家庄", "保定", "唐山"]
province_city_dict = {}
province_city_dict["province"] = province_list
province_city_dict["city"] = city_list
print(province_city_dict)








