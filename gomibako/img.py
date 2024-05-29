#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk

#
# GUI設定
#
root = tk.Tk()
#root.title(u"tkのCanvasを使ってみる")
root.geometry("800x450")

#キャンバスエリア
canvas = tk.Canvas(root, width = 800, height = 450)

#キャンバスバインド
canvas.place(x=0, y=0)


#
# GUIの末端
#
root.mainloop()