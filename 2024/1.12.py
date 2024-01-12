import random


def topic_collect():
    # 从题目文档中拆分题目
    with open('选择题.txt', 'r') as r:
        content = r.read()
        # 创建题目列表
        topic_list = content.split(';')
        topic_list.remove('\n')  # 去除列表最后一个元素，是换行符

        # 创建题目字典
        topic_dic = {}
        for topic in topic_list:
            problem = topic.split('正确答案:')[0]  # 切出问题
            answer = topic.split('正确答案:')[1]   # 切出答案
            topic_dic[problem] = answer   # 将问题和答案以键值对的形式存入字典

    test(topic_dic)


# 定义测试函数
def test(dic):
    score = 0
    errors_lst = []
    for i in range(20):
        print(f"{i + 1}.", end='')
        question = random.choice(list(dic.items()))
        anwser = dic[question[0]].split(':')
        print(question[0].strip())
        uerser_anwser = input("请输入答案")

        if uerser_anwser.upper() == anwser[0].strip():
            print('回答正确！')
            score += 5
        else:
            print("回答错误！")
            errors_lst.append(question[0]+'正确答案'+anwser[0])
        print('\n')

    print(f'\n\n你的得分是:{score}\n')

    if errors_lst:
        print("错题：")
        for error in errors_lst:
            print(error.strip())

    else:
        print("恭喜你！全部做对了！")


if __name__ == '__main__':
    topic_collect()
    a = input('按任意键退出')


