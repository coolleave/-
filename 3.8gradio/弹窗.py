import gradio as gr

def open_popup():
    return "点击了打开弹窗按钮"

def close_popup():
    return "关闭弹窗"

iface = gr.Interface(
    fn=open_popup,
    inputs=None,
    outputs="text",
    title="模拟弹窗示例",
    theme="light",
    layout="vertical",
    description="点击下面的按钮打开弹窗：",
    buttons=[
        gr.Button("打开弹窗")
    ],
    oninit=lambda: gr.Interface(fn=open_popup, inputs=None, outputs="text").launch()
)

iface.launch()