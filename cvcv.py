import cv2
import time
import sample
import sys
import pygame
from pygame.locals import *
movie = cv2.VideoCapture(0)

red = (28, 187, 255) # 枠線の色
before = None # 前回の画像を保存する変数
fps = int(movie.get(cv2.CAP_PROP_FPS)) #動画のFPSを取得
#pygameの初期化
pygame.init()
screen = pygame.display.set_mode((2032, 1143),FULLSCREEN)
pygame.display.set_caption("image")
back_img = pygame.image.load("back.png")
rect_back_img = back_img.get_rect()
img1 = pygame.image.load("test.png")
#movie_sample = cv2.VideoCapture("sample.mp4")
def main(x,y):
    px=x
    py=y
    screen.fill((255,255,255))
    screen.blit(back_img,(rect_back_img))
    screen.blit(img1,(px,py))
    pygame.display.update()
while True:
    # 画像を取得
    ret, frame = movie.read()
    # 再生が終了したらループを抜ける
    if ret == False: break
    # 白黒画像に変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if before is None:
        before = gray.astype("float")
        continue
    #現在のフレームと移動平均との差を計算
    cv2.accumulateWeighted(gray, before, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(before))
    #frameDeltaの画像を２値化
    thresh = cv2.threshold(frameDelta, 3, 255, cv2.THRESH_BINARY)[1]
    #輪郭のデータを得る
    contours = cv2.findContours(thresh,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[0]

    # 差分があった点を画面に描く
    for target in contours:
        x, y, w, h = cv2.boundingRect(target)
        #if w < 30: continue # 小さな変更点は無視
        if w < 400: continue
        #cv2.rectangle(frame, (x, y), (x+w, y+h), red, 2)
        #やってみる
        main(x,y)
    #ウィンドウでの再生速度を元動画と合わせる
        time.sleep(1/fps)
    # ウィンドウで表示
        cv2.imshow('target_frame', frame)
    # Enterキーが押されたらループを抜ける
        if cv2.waitKey(1) == 13: break

movie.release()
cv2.destroyAllWindows() # ウィンドウを破棄