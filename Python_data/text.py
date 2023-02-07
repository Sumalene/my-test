# @FileName   :text.py
# @Time       :2023/1/29 1:17
# @Author     :riyo
"""写"""
# 直接冲洗
f = open("text_write2", "w",encoding="UTF-8")  # 存在一个变量里 打开 文件不存在则新建
content= ["hello\n","宸心"]
content2= ["hello","叶"]
#f.writelines(content)
f.write("\n".join(content2))
#f.write("hello world\n叶宸心")
f.close()  # 关闭文件资源

"""相对 绝对 路径"""

# f = open(r"D:\Python_data\text_write","w") # 直接读 忽略转义
# f.write("hello IDEA 叶")
# f.close()