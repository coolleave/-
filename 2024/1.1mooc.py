import re

with open('原始文件.txt', 'r', encoding='utf-8') as file:
    txt = file.read()
    # 标准化处理文档
    txt = re.sub(r".*?单选", '【】', txt)
    txt = re.sub(r".*?多选", '【】', txt)
    # 去除冗余字符
    txt = re.sub(r".*?/.*?", '', txt)
    txt = re.sub(r"总分", '', txt)
    txt = re.sub(r"2.00", '', txt)
    txt = re.sub(r"你选对了", '', txt)
    txt = re.sub(r"你错选.*?", '', txt)
    txt = re.sub(r"你没选择任何选项", '', txt)
with open('1-1.txt', 'w', encoding='utf-8') as w:
    w.write(txt)

with open('1-11.txt', 'w', encoding='utf-8') as w:
    lst = []
    with open('1-1.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        chapter_content = ''
        for line in lines:
            line = line.strip()
            # print(line)
            if line.startswith('【】'):
                # 保存上一个题的内容
                if chapter_content:
                    chapter_content = re.sub(r'\n', r"", chapter_content)
                    # print(chapter_content)
                    lst.append(chapter_content)

                    chapter_content = ''

                # 提取新章节的标题
                chapter_title = line
            else:
                # 拼接章节内容
                chapter_content += line + '\n'

        # 保存最后一个题的内容
        if chapter_content:
            chapter_content = re.sub(r'\n', r"", chapter_content)  # 去除每一个题的换行
            # print(chapter_content)
            lst.append(chapter_content)

        # 题目去重
        # 存储已经出现过的关键字
        seen_keywords = set()
        print(lst)
        # 去除重复项
        result = []
        for item in lst:
            keyword = item[:6]  # 提取前6个字作为关键字
            if keyword not in seen_keywords:
                result.append(item)
                seen_keywords.add(keyword)

        i = 1
        for topic in result:
            topic = re.sub('正确答案', '\n正确答案', topic)
            topic = re.sub('。', '。\n', topic)
            w.write(f'{i}.' + topic + '\n')

            # print(topic)
            i += 1
