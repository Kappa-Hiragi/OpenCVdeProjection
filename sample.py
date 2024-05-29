import sys
import pygame
from pygame.locals import *
def main():
    pygame.init()                                               # Pygameの初期化
    screen = pygame.display.set_mode((600, 500))                # 大きさ600*500の画面を生成
    pygame.display.set_caption("image")                         # タイトルバーに表示する文字
    logo = pygame.image.load("test.png")                     #　ペンギンの画像取得

    while (1):
        screen.fill((0,0,0))                                    # 画面全体を黒色に塗りつぶし
        screen.blit(logo,(20,50))                               # 左上(20,50)の配置に画像描画（表示）
        pygame.display.update()                                 # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:                              # 閉じるボタンが押されたら終了
                pygame.quit()                                   # Pygameの終了(画面閉じられる)
                sys.exit()

if __name__ == "__main__":
    main()