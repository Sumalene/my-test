# @FileName   :read.py
# @Time       :2023/1/30 22:30
# @Author     :riyo
"""
f = open("read_text", 'w', encoding="UTF-8")
f.write("data 叶宸心" * 6)
f.close()

f = open("read_text", 'r', encoding="UTF-8")
data = f.read(6) # 记得返回;空指定,返回所有数值
print("txt::",data)

data = f.read(6) # 记得返回;空指定,返回所有数值
print("txt::",data) # 按字符一个个读
f.close()
"""

f = open("read_text", 'w', encoding="UTF-8")
f.write("data 叶宸心" * 6)
f.close()
f = open("read_text", 'r', encoding="UTF-8")
data = f.read(2) # 记得返回;空指定,返回所有数值
print("txt::",data)
f.seek(4)
data = f.read(6)
print("txt::",data)
print("loca:",f.tell())  # 拿到位置字节 中文三个字节 8
