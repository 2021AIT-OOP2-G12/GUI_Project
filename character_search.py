import pyocr
import pyocr.builders
from PIL import Image
import cv2
import bin_img

def character_search(name,str):
    # tesseractをインストールしたフォルダにパスが通っていること
    tools = pyocr.get_available_tools()
    line_boxs=tools[0].image_to_string(
        Image.open(name),
        lang='jpn',
        builder=pyocr.builders.LineBoxBuilder()
    )
    sorce_img = cv2.imread(name)

    #　指定された文字の検索、ハイライト処理 
    # とりあえず”小路”で実行する
    str_count = len(str)

    for line_box in line_boxs:


        t = line_box.content.replace(' ', '')

        # 小の左肩の座標
        #print(line_box.content, line_box.position)
        if t.find(str) != -1:
            tate = line_box.position[1][1] - line_box.position[0][1]
            yoko = (line_box.position[1][0] - line_box.position[0][0])/len(line_box.content)
            #print(tate)
            #print(yoko)
            #print('-----------------!')
            #print(len(line_box.content))
            
            # 空白がある場合の処理
            if line_box.content.find(str) == -1:
                str_count = len(str)*2-1
            for s in range(len(line_box.content)):
                if line_box.content[s] == str[0]:
                    num_y = line_box.position[0][0]+s*int(yoko)
                    num_x = line_box.position[0][1]

                    #print('-----------------')
                    #print(line_box.position[1][1])
                    #print(num_x)
                    #print(num_y)

                    #2値化画像をtmpに代入
                    tmp = bin_img.bin(sorce_img)
                    #2値化画像が黒い座標の色を変える
                    for y in range(num_y,num_y+int(yoko)*str_count):
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