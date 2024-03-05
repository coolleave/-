import gradio as gr


def test1():
    # 定义实现功能的函数
    def sayhi(name):
        return 'hello' + name + '!'

    # 创建demo并向demo里传入参数
    demo = gr.Interface(fn=sayhi, inputs='text', outputs='text')

    # 运行demo
    demo.launch()


def test2():
    def text_to_upper(text):
        return text.upper()

    iface = gr.Interface(
        fn=text_to_upper,
        inputs=gr.Textbox(lines=2, label="输入文本"),
        outputs="text",
        title="文本转大写"
    )

    iface.launch()


def test3():

    def sayhi(name, is_morning, tempterature):
        greet = name + '早上好' if is_morning else'晚上好'
        tempterature1 = (int(tempterature-32)) * 5 / 9
        return greet, tempterature1

    iface = gr.Interface(
        fn=sayhi,
        inputs=['text', 'check_box', gr.Slider(0, 100)],
        outputs=['text', 'number']
    )

    iface.launch()


if __name__ == '__main__':
    test3()
