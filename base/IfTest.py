
citys = ["beijing", "tianjin", "shanghai"]
for city in citys:
    if city == "tianjin":
        print(city.upper())
    else:
        print(city)

city = "TianJin"
print(city.lower() == "tianjin")

age = 21
age_result = (age >= 20 and age <= 30)
print(age_result)

age = 21
age_result = (age >= 20 or age <= 20)
print(age_result)

citys = ["北京", "天津", "上海"]
city_result_1 = "北京" in citys
print(city_result_1)
city_result_2 = "合肥" in citys
print(city_result_2)
city_result_3 = "北京" not in citys
print(city_result_3)
city_result_4 = "合肥" not in citys
print(city_result_4)

# if语句
age = 20
if age >= 20:
    print("age >= 20")
if age < 20:
    print("age < 20")
# if else语句
age = 30
if age >= 30:
    print("age >= 30")
    print("age >= 30")
else:
    print("age < 30")
    print("age < 30")
# if-elif-else结构
age = 40
if age < 20:
    print("age < 20")
elif age >= 20 and age < 30:
    print("20 <= age < 30")
elif age >= 30 and age < 40:
    print("30 <= age < 40")
elif age >= 40 and age < 50:
    print("40 <= age < 50")
else:
    print("age >= 50")

# 5.4 使用if语句处理列表
# 检查特殊元素
citys = ["北京", "上海", "天津"]
for city in citys:
    if city == "上海":
        print("this is shanghai")
    else:
        print(f"this is {city}")
# 在if语句中将列表名用作条件表达式时，Python将在列表至少包含一个元素时返回True，并在列表为空时返回False。
citys = []
if citys:
    for city in citys:
        print(city)
else:
    print("this is a empty list")

# 不报错
for city in citys:
    print("city")


citys_dir = ["上海", "天津"]
citys = ["北京", "上海", "天津"]
for city in citys:
    if city in citys_dir:
        print(city)
    else:
        print("do nothing")




