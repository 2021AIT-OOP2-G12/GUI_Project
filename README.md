# GUI_Project
GUIアプリケーションリポジトリ

##作成するアプリケーション

アップロードされた文字を含んだ画像から文字を検索して検索された文字列をハイライトして表示するWebアプリケーション

##レイアウト案

https://xd.adobe.com/view/e66639b4-d04e-43ca-868b-30ccef939812-b335/

[GUI_Project_demo.pdf](https://github.com/2021AIT-OOP2-G12/GUI_Project/files/7767050/GUI_Project_demo.pdf)

## 役割分担

| 氏名           | 役割分担   |
| -------------- | ----------- |
| 髙木　健路     | リーダー      |
| 中山　龍之介     | WEB      |
| 豊島　侑晟     | WEB      |
| 玉腰　英聖     | 画像処理      |
| 江葉　皓平     | 画像処理      |
| 杉坂　侑哉     | 画像処理      |
| 横山　結一     | 画像処理      |


## 使用するモジュール

下記の通りインストールしてください
pip install pyocr
brew install tesseract
wget https://github.com/tesseract-ocr/tessdata/raw/4.00/jpn.traineddata
mv jpn.traineddata /usr/local/Cellar/tesseract/4.1.3/share/tessdata/
