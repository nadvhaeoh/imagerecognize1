import cv2

camera = cv2.VideoCapture(1)                # カメラCh.(ここでは0)を指定

#github_test

# 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
while True:
    ret, frame = camera.read()              # フレームを取得
    cv2.imshow('camera', frame)             # フレームを画面に表示

    # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
import cv2
 
camera = cv2.VideoCapture(1)                # カメラCh.(ここでは0)を指定//内蔵カメラは'0'、USBでのカメラは'1'
 
# 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
while True:
    ret, frame = camera.read()              # フレームを取得
    cv2.imshow('camera', frame)             # フレームを画面に表示
 
    # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()