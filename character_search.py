import pyocr
import pyocr.builders
from PIL import Image
import cv2
import bin_img
import os


def character_search(name,str):
    # tesseractをインストールしたフォルダにパスが通っていること
    tools = pyocr.get_available_tools()
    tool = tools[0]
    #画像読み込み
    sorce_img = cv2.imread(name)
    img = Image.open(name)
 
    #画像から文字を読み込む
    builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
    #textは一文字ずつのlist型
    text = tool.image_to_string(img, lang="jpn", builder=builder)
    
    '''i=0
    for line_box in text:
        print(f"{i}:{line_box}")
        i+=1
    i=0'''
    
    #print(text[0])
    #　指定された文字の検索、ハイライト処理 
    # とりあえず”小路”で実行する
    # "小路"を一文字ずつに分ける
    serch = list(str)
    
    #現在の文字数のインデックス
    j=0
    i=0
    #　指定された文字の検索、ハイライト処理 
    # とりあえず”小路”で実行する
    print(len(text))
    for line_box in text:
        #print(type(line_box))

        #line_boxはbox型なのでfindを使うためにstr型に
        t = line_box.content
        u = text[j+1].content
        print(f"{t}&{u}")
        print(f"{i}:{line_box}")
        #print(line_box.position[0][0])
        i=i+1
        num_y = line_box.position[0][1]
        num_x = line_box.position[0][0]
        
        #print(line_box.content, line_box.position)
        if t.find(serch[0]) != -1:
            if u.find(serch[1]) != -1:
                print("-------------検知-----------")
                #tate=文字の縦の長さ　tate_amp=文字の縦方向塗り潰しの増幅度
                tate = line_box.position[1][1] - line_box.position[0][1]
                tate_amp = tate/2
                print(tate)
                #yoko=文字の横の長さ　yoko_amp=文字の横方向塗り潰しの増幅度
                yoko = (line_box.position[1][0] - line_box.position[0][0])
                yoko_amp = yoko/2
                #print(tate)
                #print(yoko)
                #print('-----------------!')
                #print(len(line_box.content))
                
                #塗り潰し文字の左したの画素
                num_y = line_box.position[0][1]

                #塗り潰し文字の左うえの画素
                num_x = line_box.position[0][0]
            
                #2値化画像をtmpに代入
                tmp = bin_img.bin(sorce_img)
                #2値化画像が黒い座標の色を変える
                for y in range(num_y-int(yoko_amp),num_y+int(yoko)+int(yoko_amp)):
                    for x in range(num_x-int(tate_amp),num_x+int(tate)+int(tate_amp)):
                        s = tmp[y, x]
                        b, g, r = sorce_img[y, x]
                        if s == 255:
                            continue
                        sorce_img[y, x] = 0, g, r #元の画像がb=0だと変わらない
                #for word_box in line_box.word_boxes:
                    #print('  ', word_box.content, word_box.position)
                    #cv2.rectangle(sorce_img, word_box.position[0][:], word_box.position[1][:], (255, 0, 0), thickness=1, lineType=cv2.LINE_8, shift=0)
        if text[j+1]!=None:
            j+=1
        if len(text)==j+1:break
        print(f"番目：{j}")
    cv2.imwrite('sample.png',sorce_img)
    print("終了")


if __name__ == "__main__":
    character_search('sample1.png','個人')