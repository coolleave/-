import re
import xlwt


def novelchapters2():
    book_name = '《最强反派系统》（校对版全本）作者：封七月'

    # 创建 Workbook 对象
    wb = xlwt.Workbook()

    # 创建工作表
    ws = wb.add_sheet('Sheet1')
    # 打开小说文件
    with open(f'{book_name}.txt', 'r', encoding='gb18030') as r:
        txt = r.read()
        lst = txt.split('\n\n')  # 用双换行符切
        # 写入表格
        for i in range(1, len(lst)):
            lst[i] = re.sub('.*?第.*?章.*', '', lst[i])  # 去掉卷标题
            lst[i] = re.sub('.*?第.*?卷.*', '', lst[i])  # 去掉章标题
            lst[i] = re.sub('\n\n\n', '\n\n', lst[i], flags=re.DOTALL)
            lst[i] = re.sub('\n\n', '', lst[i], flags=re.DOTALL)  # 去掉开头双换行符
            lst[i] = re.sub('\n', r'\\n', lst[i], flags=re.DOTALL)  # 把换行符替换成\n
            # print(lst[1])
            # worksheet.cell(row=i, column=1, value=lst[i])
            ws.write(i-1, 0, lst[i])

        # 保存表格
        # workbook.save('novelchapters.xlsx')
        wb.save('novel10.xls')
        print('over!')


if __name__ == '__main__':
    novelchapters2()
