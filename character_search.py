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
    '''line_boxs=tools[0].image_to_string(
        Image.open(name),
        lang='jpn',
        builder=pyocr.builders.LineBoxBuilder()
    )'''
    sorce_img = cv2.imread(name)
    img = Image.open(name)
 
    #画像から文字を読み込む
    builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
    text = tool.image_to_string(img, lang="jpn", builder=builder)
    print(type(text))
    i=0
    
    #print(text[0])
    #　指定された文字の検索、ハイライト処理 
    # とりあえず”小路”で実行する
    str_count = len(str)
    serch = list(str)
    #print(s)
    for line_box in text:
        #print(type(line_box))

        t = line_box.content
        print(f"{i}:{line_box}")
        i=i+1
        # 小の左肩の座標
        #print(line_box.content, line_box.position)
        if t.find(serch[0]) != -1:
            tate = line_box.position[1][1] - line_box.position[0][1]
            yoko = (line_box.position[1][0] - line_box.position[0][0])
            #print(tate)
            #print(yoko)
            #print('-----------------!')
            #print(len(line_box.content))
            
            # 空白がある場合の処理
            num_y = line_box.position[0][0]
            num_x = line_box.position[0][1]

            #print('-----------------')
            #print(line_box.position[1][1])
            #print(num_x)
            #print(num_y)

            #2値化画像をtmpに代入
            tmp = bin_img.bin(sorce_img)
            #2値化画像が黒い座標の色を変える
            for y in range(num_y,num_y+int(yoko)):
                for x in range(num_x,num_x+int(tate)):
                    s = tmp[x, y]
                    b, g, r = sorce_img[x, y]
                    if s == 255:
                        continue
                    sorce_img[x, y] = 0, g, r #元の画像がb=0だと変わらない

            #for word_box in line_box.word_boxes:
                #print('  ', word_box.content, word_box.position)
                #cv2.rectangle(sorce_img, word_box.position[0][:], word_box.position[1][:], (255, 0, 0), thickness=1, lineType=cv2.LINE_8, shift=0)
    cv2.imwrite('sample.png',sorce_img)


if __name__ == "__main__":
    character_search('test.png','小路')