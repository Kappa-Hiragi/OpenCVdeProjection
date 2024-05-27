import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps  # 画像データ用
import cv2
import numpy as np

red = (28, 187, 255)  # 枠線の色
before = None  # 前回の画像を保存する変数
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.master.title("OpenCVの動画表示")       # ウィンドウタイトル
        self.master.geometry("400x300")     # ウィンドウサイズ(幅x高さ)
        # Canvasの作成
        self.canvas = tk.Canvas(self.master)
        # Canvasにマウスイベント（左ボタンクリック）の追加
        self.canvas.bind('<Button-1>', self.canvas_click)
        # Canvasを配置
        self.canvas.pack(expand = True, fill = tk.BOTH)

        # カメラをオープンする
        self.capture = cv2.VideoCapture(0)

        self.disp_id = None

    def canvas_click(self, event):
        '''Canvasのマウスクリックイベント'''

        if self.disp_id is None:
            # 動画を表示
            self.disp_image()
        else:
            # 動画を停止
            self.after_cancel(self.disp_id)
            self.disp_id = None

    def disp_image(self):
        '''画像をCanvasに表示する'''

        # フレーム画像の取得
        ret, frame = self.capture.read()
        # BGR→RGB変換
        #cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 白黒画像に変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 現在のフレームと移動平均との差を計算
        cv2.accumulateWeighted(gray, before, 0.5)
        frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(before))
        # frameDeltaの画像を２値化
        thresh = cv2.threshold(frameDelta, 3, 255, cv2.THRESH_BINARY)[1]
        # 輪郭のデータを得る
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        # 差分があった点を画面に描く
        for target in contours:
            x, y, w, h = cv2.boundingRect(target)
            if w < 30:
                continue  # 小さな変更点は無視
            cv2.rectangle(frame, (x, y), (x + w, y + h), red, 2)
            # NumPyのndarrayからPillowのImageへ変換
            pil_image = Image.fromarray(frame)

        # キャンバスのサイズを取得
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # 画像のアスペクト比（縦横比）を崩さずに指定したサイズ（キャンバスのサイズ）全体に画像をリサイズする
        pil_image = ImageOps.pad(pil_image, (canvas_width, canvas_height))

        # PIL.ImageからPhotoImageへ変換する
        self.photo_image = ImageTk.PhotoImage(image=pil_image)

        # 画像の描画
        self.canvas.delete("all")
        self.canvas.create_image(
                canvas_width / 2,       # 画像表示位置(Canvasの中心)
                canvas_height / 2,
                image=self.photo_image  # 表示画像データ
                )

        # disp_image()を10msec後に実行する
        self.disp_id = self.after(10, self.disp_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
