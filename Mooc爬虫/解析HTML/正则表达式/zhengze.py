import re
# re.search(pattern, string, flags)
# 返回一个match结果
match = re.search(r'[1-9]\d{5}', 'BIT /236000 236001')
if match:
    print(match.group(0))
# re.match(pattern, string, flags)
# 返回一个match结果
match = re.match(r'[1-9]\d{5}', 'BIT /236000')
if match:
    print(match.group(0))
# 为空
match = re.match(r'[1-9]\d{5}', '236000 BIT')
if match:
    print(match.group(0))
# 因为re.match()匹配的是该匹配符开头的字符串

# re.findall(pattern, string, flags)
# 返回的是一个列表类型
list = re.findall(r'[1-9]\d{5}', 'BIT /236000 .236002 236003b')
if match:
    print(list)

# re.split(pattern, string, maxsplit, flags)
# maxsplit 最大分割数
# 返回一个列表类型
ls = re.split(r'[1-9]\d{5}', 'HF236001 HI236002 HA236003 HB236004 HC236005', maxsplit=1)
if match:
    print(ls)
# ['HF', ' HI', ' HA', ' HB', ' HC', ''] 将匹配的字符之外的字符串输出
# maxsplit = 1时结果为 ['HF', ' HI236002 HA236003 HB236004 HC236005'] 只匹配第一个


# re.finditer(pattern, string, flags)
# 返回一个迭代类型 而每一个迭代元素又是match对象
for match in re.finditer(r'[1-9]\d{5}', 'HF236001 HI236002 HA236003 HB236004 HC236005'):
    if match:
        print(match.group(0))
# 能循环的获得每一个元素
# re.sub(pattern, repl, string, cont=0, flags=0)
# 能够替换所有匹配的字符串 ，返回替换后的结果
# count 匹配的最大次数 repl 替换的字符串
replace = re.sub(r'[1-9]\d{5}', '邮编', 'HF236001 HI236002 HA236003 HB236004 HC236005')
if replace:
    print(replace)
# 结果:HF邮编 HI邮编 HA邮编 HB邮编 HC邮编 字符串已被替换
