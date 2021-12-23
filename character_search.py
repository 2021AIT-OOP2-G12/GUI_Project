import pyocr
import pyocr.builders
from PIL import Image
import cv2

def character_search(name):
    # tesseractをインストールしたフォルダにパスが通っていること
    tools = pyocr.get_available_tools()
    line_boxs=tools[0].image_to_string(
        Image.open(name),
        lang='jpn',
        builder=pyocr.builders.LineBoxBuilder()
    )
    sorce_img = cv2.imread(name)

    for line_box in line_boxs:
        # 件 名 : バブ リッ クコ メン ト へ の 意見 ((68, 182), (235, 191))
        print(line_box.content, line_box.position)
        for word_box in line_box.word_boxes:
            print('  ', word_box.content, word_box.position)
            cv2.rectangle(sorce_img, word_box.position[0][:], word_box.position[1][:], (255, 0, 0), thickness=1, lineType=cv2.LINE_8, shift=0)
    cv2.imwrite('sample.png',sorce_img)


if __name__ == "__main__":
    character_search('test.png')