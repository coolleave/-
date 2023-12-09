import re


def remove_reporters(text):  # 处理文本
    pattern1 = r'（记者.+）'
    pattern2 = r'https?://\S+'
    pattern3 = r'（实习记者.+）'
    pattern4 = r'（通讯员.+）'
    pattern5 = r'（.+）\'}"'
    pattern6 = r''
    cleaned_text = re.sub(pattern1, '', text)  # 去除（记者**）部分
    cleaned_text = re.sub(pattern2, '', cleaned_text)  # 去除网址部分
    cleaned_text = re.sub(pattern3, '', cleaned_text)  # 去除（实习记者**）部分
    cleaned_text = re.sub(pattern4, '', cleaned_text)  # 去除（通讯员**）部分
    cleaned_text = re.sub(pattern5, '\'}"', cleaned_text)  # 直接去除文末括号部分
    cleaned_text = cleaned_text.replace('相关论文信息：', '')  # 去除相关论文信息：部分
    cleaned_text = cleaned_text.replace('相关论文信息:', '')
    cleaned_text = cleaned_text.replace('图片来源：视觉中国', '')  # 去除图片来源：视觉中国部分

    return cleaned_text


if __name__ == '__main__':

    with open('../../项目/测试文件/result.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        # print(content)
        text2 = remove_reporters(content)
    with open('../../项目/测试文件/2.txt', 'w', encoding='utf-8') as w:
        w.write(text2)
