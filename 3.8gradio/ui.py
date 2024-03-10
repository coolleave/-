import gradio as gr
import random


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    with gr.Row():
        clear = gr.ClearButton([msg, chatbot])
        submit_btn = gr.Button('提交', variant='primary')

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        return "", chat_history
    submit_btn.click(respond,[msg, chatbot], [msg, chatbot])
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
demo.launch()
