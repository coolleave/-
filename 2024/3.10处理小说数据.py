import os
import re
import xlwt

def novelchapters2(book_name):
    # 创建 Workbook 对象
    wb = xlwt.Workbook()
    # 创建工作表
    ws = wb.add_sheet('Sheet1')
    # print(f'{book_name}.txt')
    # 打开小说文件
    with open(f'./{book_name}.txt', 'r', encoding='utf-8') as r:
        txt = r.read()
        lst = txt.split('==================================================')  # 用双换行符切
        # 写入表格
        a = 0
        for i in range(1, len(lst)):
            lst[i] = re.sub('.*?第.*?章.*', '', lst[i])  # 去掉卷标题
            lst[i] = re.sub('.*?第.*?卷.*', '', lst[i])  # 去掉章标题
            lst[i] = re.sub('\n\n\n', '\n\n', lst[i], flags=re.DOTALL)
            lst[i] = re.sub('\n\n', '', lst[i], flags=re.DOTALL)  # 去掉开头双换行符
            lst[i] = re.sub('\n', r'\\n', lst[i], flags=re.DOTALL)  # 把换行符替换成\n
            lst[i] = re.sub(r'\s\s', r'', lst[i], flags=re.DOTALL)  # 把换行符替换成\n
            # print(lst[1])
            # worksheet.cell(row=i, column=1, value=lst[i])
            if lst[i] == '\\n' or lst[i].startswith('内容简介') or lst[i].startswith('\\n内容简介'):
                a += 1
            else:
                ws.write(i-1-a, 0, lst[i])

        # 保存表格
        wb.save(f'./excel/{book_name}.xls')
        print(f'{book_name} over!')


# 找到txt文件名称，并传入章节处理函数
def handle_txt(folder_path):
    for file_name in os.listdir(folder_path):  # 遍历文件夹内所有的文件
        if file_name.endswith('.txt'):  # 找到txt文件名称
            file_name = file_name.split('.')[0]  # 切走后缀
            print(file_name)
            novelchapters2(file_name)


if __name__ == '__main__':
    os.mkdir('excel')
    handle_txt('./')
