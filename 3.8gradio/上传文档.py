import gradio as gr


def generate_file(file_obj):

    global tmpdir
    tmpdir = tmpdir.split('/')[:-1]
    print('临时文件夹地址：{}'.format(tmpdir))
    # 在本地生成的临时文件路径'/home/extra1T/miaobr/Modelscope-Agent/local_databases/tmp2j1y8vin'


    print('上传文件的地址：{}'.format(file_obj.name)) # 输出上传后的文件在gradio中保存的绝对地址

    # 获取到上传后的文件的绝对路径后，其余的操作就和平常一致了

    # # 将文件复制到临时目录中
    # if ".docx" in file_obj.name:
    #     doc = Document(file_obj.name)
    #     text = '\n'.join(para.text for para in doc.paragraphs)
    #     with open(tmpdir/file_obj.name.split('/')[-1].replace(".docx",".txt"), 'w', encoding='utf-8') as txt:
    #         txt.write(text)
    #
    #     shutil.copy(file_obj.name, tmpdir)
    # if ".txt" in file_obj.name:
    #     shutil.copy(file_obj.name, tmpdir)
    #     #前面是临时创建的路径，后边是文件上传到本地的路径。
    # print("a")


def main():
    global tmpdir
    with tempfile.TemporaryDirectory(dir='/var/lib/docker/miaobr/Modelscope-Agent/local_databases') as tmpdir:
        # 定义输入和输出
        inputs = gr.components.File(label="上传文件")
        outputs = None

        # 创建 Gradio 应用程序g
        app = gr.Interface(fn=generate_file, inputs=inputs, outputs=outputs,   title="文件上传、并生成可下载文件demo",
                      description="上传任何文件都可以，只要大小别超过你电脑的内存即可"
      )

        # 启动应用程序
        app.launch(share=True)


if __name__=="__main__":
    main()