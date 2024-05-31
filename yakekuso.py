import cv2
import pygame
import sys

# 動画を読み込む
cap = cv2.VideoCapture('sample.mp4')

# pygameを初期化
pygame.init()

# 画面の大きさを設定
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
screen = pygame.display.set_mode(size)

try:
    while True:
        # 動画から1フレーム読み込む
        ret, frame = cap.read()
        if not ret:
            break

        # OpenCVの画像データをpygameで扱える形に変換
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame.transpose((1, 0, 2))
        frame = pygame.surfarray.make_surface(frame)

        # 画像を画面に描画
        screen.blit(frame, (0, 0))

        # 画面を更新
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

finally:
    cap.release()
    pygame.quit()
    sys.exit()