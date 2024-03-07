import cv2
import gradio as gr


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
        # 复选框
        gr.CheckboxGroup(['option1', 'option2', 'option3']),
        # 颜色选择器
        gr.ColorPicker(),
        # 表格选择器
        gr.DataFrame(headers=3),

        gr.Dropdown(['option1', 'option2', 'option3']),

        gr.File(),

        gr.Image(),

        gr.Number(),

        gr.Radio(),


    ]


if __name__ == '__main__':
    test2()
