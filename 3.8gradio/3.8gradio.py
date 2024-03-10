import gradio as gr
from docx import Document


def echo(message, history, file_dir):
    print(f'{file_dir}已经上传')

    # 判断文件是否存在
    if file_dir:
        print(type(str(file_dir)))
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
    return message


demo = gr.ChatInterface(
    fn=echo,
    # examples=["纳税人根据《财政部 税务总局公告2023年第1号》公告规定应予减免增值税，在公告下发前已征收的是否可以申请退税？"
    #     ,
    #           "按月申报的增值税小规模纳税人，2023年1月发生适用3%征收率的销售额15万元，已在1号公告下发前开具发票，其中10万元开具免税发票，5万元开具3%征收率的增值税普通发票，按规定可以适用3%减按1%征收率政策，应当如何办理1月税款所属期的增值税纳税申报?"
    #     , "个人在一个纳税年度内取得两次或者两项以上股权激励所得，如何计算个人所得税？"],
    title="税务问答机器人",
    submit_btn=gr.Button('提交', variant='primary'),
    clear_btn=gr.Button('清空记录'),
    retry_btn=None,
    undo_btn=None,
    additional_inputs=[gr.File()],
    additional_inputs_accordion='上传文件',
)

if __name__ == "__main__":
    gr.close_all()
    demo.launch(debug=True, show_error=True)