#列表，元组，字典，集合
#print("hello 老登")

#列表-创建
maomao=[1,1,2,3,5,8,13,21]
print(maomao)
#列表-查询
print(maomao[0])
#列表-修改
maomao[1]=99
print(maomao)
#列表-插入
maomao.append("小登")
print(maomao)
#列表-删除
maomao.remove(1)
print(maomao)

#字典
math={"张三":85,"李四":54,"王五":61}
print(math)
#添加
math.update({"赵刚":78})
print(math)
#修改
math["赵刚"]=99
print(math)
#删除
popped_value=math.pop("张三")
print(popped_value)
print(math)
#遍历
for name, score in math.items():
    print(f"学生: {name}, 分数: {score}")

#集合
aaa={1,3,5,7,9}
bbb={1,2,3,4,5}
print(aaa)
print(bbb)
#交集
set1=aaa&bbb
print(set1)
#并集
set2=aaa|bbb
print(set2)

#元组
life=(1,2,3,"shit","shi","dabian",[1,11,111],{"huo":"zhe"})
print(life)
element="shit"
# 统计元素出现次数
count = life.count(element)
print(f"元素 '{element}' 出现次数: {count}")
#查询下标
if element in life:
    index=life.index(element)
    print(f"下标:{index}")
else:
    print("no")