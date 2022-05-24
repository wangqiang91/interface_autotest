from tracemalloc import start

str1 = "every ending is a new beginning,every people \
shoud study new knowledge"
str2 = " a_huan"
# print(str1.title())
# print(str1.upper())
# print(str1.lower())
# print(str2*2)
# print("huan1" in str2)
# print(str1[4:10:2])  #左闭右开

# print("我叫 %s ,今年%d岁，哈哈" %("阿欢",30))
list1 = str1.split(" ")
for i in range(0,len(list1)-1):
    if "," in list1[i]: 
        list1.extend(list1[i].split(","))
        list1.remove(list1[i])
print(list1)
list1.reverse()
print(list1)
