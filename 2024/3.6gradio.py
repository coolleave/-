import cv2
import gradio as gr
import matplotlib
matplotlib.use('TkAgg')


def test1():

    def handle_img(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 为图像去色
        return gray

    iface = gr.Interface(
        fn=handle_img,
        inputs='image',
        outputs=gr.Image()
    )

    iface.launch()


# 总结一下gradio的输入和输出
def test2():

    input_list = [
        # 语音
        gr.Audio(sources=['microphone', 'upload'], label='audio'),
        # 单选框
        gr.Checkbox(['option1', 'option2', 'option3'], label='checkbox'),
        # # 复选框
        gr.CheckboxGroup(['option1', 'option2', 'option3']),
        # # 颜色选择器
        gr.ColorPicker(),
        # # 表格选择器
        gr.DataFrame(),
        # 下拉选择器
        gr.Dropdown(['option1', 'option2', 'option3']),
        # 上传文件
        gr.File(),
        # 上传图像
        gr.Image(),
        # 输入数字
        gr.Number(),
        # 单选框
        gr.Radio(),
        # 滑块
        gr.Slider(minimum=100, maximum=200, step=5),
        # 文本框
        gr.Textbox(lines=3, max_lines=7, placeholder='请输入'),
        # 文本区域
        gr.TextArea(),
        # 视频区域
        gr.Video(sources=['webcam', 'upload'])

        ]

    output_list = [
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
    ]

    def fun(*args):
        return args

    iface = gr.Interface(
        fn=fun,
        inputs=input_list,
        outputs=output_list,
        title='input&ouput',
        description='This is for inputs and outputs',
        live=True

    )

    iface.launch()


if __name__ == '__main__':
    test2()
