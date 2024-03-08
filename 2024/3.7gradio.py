import gradio as gr
import time
import os
def test1():

    iface = gr.Interface(fn=None, inputs=None, outputs=gr.HTML('D:\web前端\code\\2.19.html'))
    iface.launch()


def test2():
    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.3)
            yield "You typed: " + message[: i + 1]

    gr.ChatInterface(slow_echo).launch()

def test3():

    def print_like_dislike(x: gr.LikeData):
        print(x.index, x.value, x.liked)

    def add_text(history, text):
        history = history + [(text, None)]
        return history, gr.Textbox(value="", interactive=False)

    def add_file(history, file):
        history = history + [((file.name,), None)]
        return history

    def bot(history):
        response = "**That's cool!**"
        history[-1][1] = ""
        for character in response:
            history[-1][1] += character
            time.sleep(0.05)
            yield history

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(
            [],
            elem_id="chatbot",
            bubble_full_width=False,
            avatar_images=(None, (os.path.join(os.path.dirname(__file__), "龙卡通.png"))),
        )

        with gr.Row():
            txt = gr.Textbox(
                scale=4,
                show_label=False,
                placeholder="Enter text and press enter, or upload an image",
                container=False,
            )
            btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])

        txt_msg = txt.submit(add_text, [chatbot, txt], [chatbot, txt], queue=False).then(
            bot, chatbot, chatbot, api_name="bot_response"
        )
        txt_msg.then(lambda: gr.Textbox(interactive=True), None, [txt], queue=False)
        file_msg = btn.upload(add_file, [chatbot, btn], [chatbot], queue=False).then(
            bot, chatbot, chatbot
        )

        chatbot.like(print_like_dislike, None, None)

    demo.queue()

    demo.launch(share=True)


if __name__ == '__main__':
    test3()
