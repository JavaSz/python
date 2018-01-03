# -*- coding:utf-8 -*-
# 将文件重命名
import os, sys

# 列出目录
print "目录为: %s"%os.listdir(os.getcwd())

# 重命名
os.rename("rename_files.py","rename.py")

print "重命名成功。"

# 列出重命名后的目录
print "目录为: %s" %os.listdir(os.getcwd())
