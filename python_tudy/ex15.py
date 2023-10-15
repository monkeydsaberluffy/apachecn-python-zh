# -*- coding: utf-8 -*-
from sys import argv
# 解包参数,赋值变量
script,file_name = argv
# 打印提示
print "this is your file name %r" %file_name
# 打开文件,并赋值非变量
txt = open(file_name)
# 打印文件内容
print txt.read()

# 使用raw input 实现上面逻辑
print "type your file"
file_name = raw_input('>')
txt = open(file_name)
print txt.read()