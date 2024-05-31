import cv2
import numpy as np
import time
import pygame
import sys
from pygame.locals import *

# Pythonの基本処理
pygame.init()
# 全画面のサイズ
full_screen = (800, 800)
# ゲーム画面の枠
surface =pygame.display.set_mode((full_screen[0], full_screen[1]))
# テスト表示用のフォント設定
test_font = pygame.font.Font(None, 100)
# ゲームで使用する動画の読み込み
movie_sample = cv2.VideoCapture("sample.mp4")

# -------------- メイン処理 --------------
def main():
    # ゲームの時間代わりになる変数
    count = 0
    ###### メイン繰り返し処理 ######
    while True:
        # 画面を黒く塗りつぶす
        surface.fill((0,0,0))
        # 左上にテストと表示する
        surface.blit(test_font.render("TEST", True, (255,255,255)), (50, 50))
        # 時間と共に増加していく変数
        count += 1
        # 描画更新処理
        pygame.display.update()
        #  終了処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # countが1000になった場合に動画が再生される
        if count == 1000:
            # 動画の再生速度調整用変数、数字が大きくなればなるほど再生速度が速くなる
            fps_num = 8
            # 動画のプロパティを取得
            # 幅
            width = int(movie_sample.get(cv2.CAP_PROP_FRAME_WIDTH))
            # 高さ
            height = int(movie_sample.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # フレーム数+ゲームスピード この数字が大きいほど映像再生スピードが早くなる
            fps = movie_sample.get(cv2.CAP_PROP_FPS) + fps_num
            # 画面サイズ変更用パラメーター
            # 高さ
            # 設定している画面サイズが動画サイズと異なる場合
            if full_screen[1] != height:
                # 高さのリサイズ設定
                y_resize = int(height * (full_screen[1] / height))
            # 動画サイズと画面サイズが等しい場合
            else:
                y_resize = 1
            # 幅
            # 設定している画面サイズが動画サイズと異なる場合
            if full_screen[0] != width:
                # 高さのリサイズ設定
                x_resize = int(width * (full_screen[0] / width))
            # 動画サイズと画面サイズが等しい場合
            else:
                x_resize = 1
            # 動画を途中で打ち切りたい場合に再生を中止するための変数
            flag = True
            while flag:
                # retとは：画像情報が格納されていたらretはTrueを返し、格納されていなかったらFalseを返す
                # frameとは動画の画像の一コマをnumpyの配列にしたもの
                ret, frame = movie_sample.read()
                # 何らかのエラー、もしくは動画が終了したらbreakする
                if not ret:
                    break
                # 動画のサイズを画面に合わせる
                frame = cv2.resize(frame, (x_resize, y_resize))
                # ムービーの画質調整
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # numpy.rot90()を使うとNumPy配列ndarrayを90度間隔（90度、180度、270度）で回転できる。
                frame = np.rot90(frame, 3)
                # np.fliplr(frame)を使うとNumPy配列を鏡反転（水平反転）できる。
                frame = np.fliplr(frame)
                # 配列形式のデータをコピーし、Surfaceオブジェクトに変換します。
                # 配列が記録しているデータやフォーマットに最も適した状態のSurfaceオブジェクトを新規に作成します。
                # 任意の値の整数を保持した二次配列、もしくは三次配列を引数として設定できます。
                frame = pygame.surfarray.make_surface(frame)
                # 指定の位置に画像を描画します。
                surface.blit(frame, (0, 0))
                # 動画の表示速度を調整、ここで調整をしないと動画再生速度が高速になる。
                time.sleep(1 / fps)
                # スクリーンの一部分のみを更新します。
                # この命令はソフトウェア側での表示処理に最適化されています。
                pygame.display.update()
                # 動画再生中に何かしらのキーが押されたら再生終了
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        # 再生終了
                        flag = False
            # 動画の再再生が可能なようにフレーム(fps)を０にしておく
            movie_sample.set(cv2.CAP_PROP_POS_FRAMES, 0)

# メイン関数の呼び出し
if __name__ == "__main__":
    main()
