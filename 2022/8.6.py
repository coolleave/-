import re
s = """
<<div align="left"><font size="1">平泉市黄土梁子中学
<<div align="left"><font size="2">平泉市杨树岭中学
<<div align="left"><font size="3">平泉市第二中学
<<div align="left"><font size="4">平泉市第三中学
<<div align="left"><font size="5">平泉市四海中学
"""
obj = re.compile(r'<<div align="left"><font size="(?P<id>\d)">(?P<school>.*)')
resp = obj.finditer(s)
print(resp)
for i in resp:
    print(i.group('id'))

    print(i.group('school'))




