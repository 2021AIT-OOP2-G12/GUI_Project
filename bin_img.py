import cv2
import numpy as np

def bin(img):

    tmp_img = img.copy()

    #グレースケール化
    tmp_img = cv2.cvtColor(tmp_img, cv2.COLOR_BGR2GRAY)

    #2値化
    ret, tmp_img = cv2.threshold(tmp_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    pixel_number = np.size(tmp_img) #全ピクセル数をpixel_numberに代入
    pixel_sum = np.sum(tmp_img) #全ピクセルの輝度の合計をpixel_sumに代入
    white_pixel_number = pixel_sum/255 #白いピクセルの数を計算しwhite_pixel_numberに代入
    black_pixel_number = pixel_number - white_pixel_number #黒いピクセルの数を計算しblack_pixel_numberに代入

    #白いピクセルの方が多かったら白黒反転
    if black_pixel_number < white_pixel_number:
        tmp_img = cv2.bitwise_not(tmp_img)

    #文字が白色の2値化を返す
    return tmp_img