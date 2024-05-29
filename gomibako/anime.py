import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import time
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        # Canvas(画像を描画する領域)を宣言、配置
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        # 画像ファイル読み込みとリサイズ
        self.file = Image.open("test.png")
        self.file = self.file.resize((200, 200))
        # オブジェクトに
        self.image = ImageTk.PhotoImage(self.file)
        # 配置！
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.time.sleep(10)
        self.canvas.create_image(100, 0, image=self.image, anchor='nw')
        self.time.sleep(10)
        self.canvas.create_image(200, 0, image=self.image, anchor='nw')
        self.time.sleep(10)
        self.canvas.create_image(-100, 0, image=self.image, anchor='nw')
if __name__ == "__main__":
    application = Application()
    application.mainloop()