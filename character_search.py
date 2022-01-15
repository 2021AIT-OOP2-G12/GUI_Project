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
    # 検索する文字を一文字ずつに分ける
    serch = list(str)
    
    #現在の文字数のインデックス
    j=0
    #　指定された文字の検索、ハイライト処理 
    # とりあえず”小路”で実行する
    #print(len(text))
    for line_box in text:
        #print(type(line_box))

        #print(f"{i}:{line_box}")
        #print(line_box.position[0][0])
        num_y = line_box.position[0][1]
        num_x = line_box.position[0][0]
        
        #print(line_box.content, line_box.position)

        #length = 検索する　文字の文字数
        length = len(serch)
        #検索する文字が無いとき
        if length == 0:
            break
        
        #t=検知した文字を探したい文字の文字数分、一文字ずつ持つリスト
        t = []
        for l in range(length):
            try:
                t += text[j+l].content
                print(f"{text[j+l].content} & ",end='')
            except IndexError:
                break
            if len(t) >= length:
                break
        print()

        #print(t)

        if len(t) < len(serch):
            break
        #一文字目か二文字目が検索する文字の一文字目と一致したとき(length=1のときはt[1]がないので無条件で通すようにしている)
        elif t[0] == serch[0] or length == 1 or t[1] == serch[0]:
            #print(t)
            #m=検索する文字の場所を管理
            m = 0 
            for k in range(len(t)):
                if t[k] == serch[m]:
                    if m < length-1:
                        m+=1
                    if t[k] == serch[length-1]:
                        #print(t)
                        print("-------------検知-----------")
                        #tate=文字の縦の長さ　tate_amp=文字の縦方向塗り潰しの増幅度
                        tate = line_box.position[1][1] - line_box.position[0][1]
                        tate_amp = tate/4
                        #print(tate)
                        #yoko=文字の横の長さ　yoko_amp=文字の横方向塗り潰しの増幅度
                        yoko = (line_box.position[1][0] - line_box.position[0][0])/len(line_box.content)
                        yoko_amp = yoko/2
                        #print(tate)
                        #print(yoko)
                        #print(line_box.position[1][0] - line_box.position[0][0])
                        #print('-----------------!')
                        #print(len(line_box.content))
                        
                        #塗り潰し文字の左したの画素
                        num_y = line_box.position[0][1]

                        #塗り潰し文字の左うえの画素
                        num_x = line_box.position[0][0]

                        if t[0] == serch[0]:
                            scope = length
                        else:
                            scope = len(t)
                    
                        #2値化画像をtmpに代入
                        tmp = bin_img.bin(sorce_img)
                        #2値化画像が黒い座標の色を変える
                        for y in range(num_y-int(tate_amp),num_y+int(tate)+int(tate_amp)):
                            for x in range(num_x-int(yoko_amp),num_x+(int(yoko)*scope)):#文字数分範囲を増やしている
                                try:
                                    s = tmp[y, x]
                                    b, g, r = sorce_img[y, x]
                                    if s == 255:
                                        continue
                                    sorce_img[y, x] = 0, g, r #元の画像がb=0だと変わらない
                                except IndexError:
                                    break
                #for word_box in line_box.word_boxes:
                    #print('  ', word_box.content, word_box.position)
                    #cv2.rectangle(sorce_img, word_box.position[0][:], word_box.position[1][:], (255, 0, 0), thickness=1, lineType=cv2.LINE_8, shift=0)
        '''
        if text[j+length-1]!=None:
            j+=1
        if len(text)-length-1==j+1:break
        #print(f"番目：{j}")
        '''
        try:
            text[j+1]
            j+=1
            #print(f"番目：{j}")
        except IndexError:
            break

    cv2.imwrite('sample.png',sorce_img)
    print("終了")



if __name__ == "__main__":
    character_search('sample1.png','課題')

    #デバック用文字列
    '''
    課題
    個人
    作業
    報告書テンプレート
    main
    下さい
    い

    '''