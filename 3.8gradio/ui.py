import gradio as gr
import random
from docx import Document

css = """
.file{
height: 70px; 
text-align:center;
}
.example{
background-color: #fff;
height: 30px;
font-size: 20px
border: 2px solid #000; 

.title{
    text-align: center;
}

.title {
    border: none !important;
}
"""

# 例子
example1 = '纳税人根据《财政部 税务总局公告2023年第1号》公告规定应予减免增值税，在公告下发前已征收的是否可以申请退税？'
example2 = '按月申报的增值税小规模纳税人，2023年1月发生适用3%征收率的销售额15万元，已在1号公告下发前开具发票，其中10万元开具免税发票，5万元开具3%征收率的增值税普通发票，按规定可以适用3%减按1%征收率政策，应当如何办理1月税款所属期的增值税纳税申报?'
example3 = '个人在一个纳税年度内取得两次或者两项以上股权激励所得，如何计算个人所得税？'
# 设计界面 使用blocks
with gr.Blocks(css=css) as demo:
    gr.Label(value='税务问答机器人', elem_classes='title', show_label=False)
    # 聊天界面
    chatbot = gr.Chatbot()
    # 消息接受框
    msg = gr.Textbox()
    # 水平布局 存放清除和提交按钮
    with gr.Row():
        clear = gr.ClearButton([msg, chatbot])
        upload = gr.File(elem_classes='file', show_label=False)
        submit_btn = gr.Button('提交', variant='primary')

    with gr.Column():
        gr.Label(label='examples:', value='', elem_classes='example')
        example_btn1 = gr.Button(value=example1, elem_classes='button', size='sm')
        example_btn2 = gr.Button(value=example2, elem_classes='button', size='sm')
        example_btn3 = gr.Button(value=example3, elem_classes='button', size='sm')


    def respond(message, chat_history, file_dir):
        print(f'{file_dir}已经上传')

        # 判断文件是否存在
        if file_dir:
            # 切出文件名称
            file_dir = str(file_dir)  # 转为str类型
            file_name = file_dir.split('\\')[-1]
            print(file_name)

            # 判断文件名称
            if file_name.endswith('.docx'):
                # 打开文档
                doc = Document(file_dir)
                print(doc)

                # 创建输出文件并写入文本内容
                output_file = f"{file_name}.txt"
                with open(output_file, "w") as f:
                    for para in doc.paragraphs:
                        f.write(para.text)
                        f.write("\n")
                    print('成功!')

        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))

        return "", chat_history

    submit_btn.click(respond, [msg, chatbot, upload], [msg, chatbot])
    example_btn1.click(fn=lambda text: text, inputs=gr.Textbox(value=example1, visible=False), outputs=msg)
    example_btn2.click(fn=lambda text: text, inputs=gr.Textbox(value=example2, visible=False), outputs=msg)
    example_btn3.click(fn=lambda text: text, inputs=gr.Textbox(value=example3, visible=False), outputs=msg)
    msg.submit(respond, [msg, chatbot, upload], [msg, chatbot])


if __name__ == '__main__':
    demo.launch(debug=True, show_error=True)
