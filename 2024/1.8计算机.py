import re

with open('5.txt', 'r', encoding='utf-8') as file:
    txt = file.read()
    # 标准化处理文档
    txt = re.sub(r".*?\(单选题\).*?", '【】\n', txt)
    # 去除冗余字符
    txt = re.sub(r"我的答案.*?;", '', txt)
    txt = re.sub(r"5分", '', txt)
    txt = re.sub(r"0分", '', txt)
with open('1.1.txt', 'w', encoding='utf-8') as w:
    w.write(txt)
with open('1.11.txt', 'w', encoding='utf-8') as w:
    with open('1.1.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        chapter_content = ''
        for line in lines:
            line = line.strip()
            # print(line)
            if line.startswith('【】'):
                # 保存上一个题的内容
                if chapter_content:
                    w.write(chapter_content)
                    chapter_content = ''
                # 提取新章节的标题
                chapter_title = line
            else:
                # 拼接章节内容
                chapter_content += line + '\n'

        # 保存最后一个题的内容
        if chapter_content:
            w.write(chapter_content)
