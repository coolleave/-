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


if __name__ == '__main__':
    test1()
