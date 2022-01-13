from flask import Flask, request, render_template, jsonify, Blueprint
import numpy as np
import cv2
import os
import glob

#結果画像表示定義
add_static = Blueprint('images', __name__, static_url_path='/images/results', static_folder='./images/results')

app = Flask(__name__)
app.register_blueprint(add_static)

# 指定拡張子
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# 拡張子チェック関数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# pathの作成
def basename(path):
    return os.path.basename(path)


app.jinja_env.filters['basename'] = basename

@app.route("/")
def index():
    return render_template("top.html")

@app.route("/search_upload")
def search_upload():
    return render_template('upload.html')

@app.route("/search_result")
def search_result():
    data = glob.glob('images/results/*')
    return render_template("search_result.html", data=data)

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({ "result": False, "message": "ファイルが選択されていません。" })
    keyword = request.form["keyword"]
    img_file = request.files["file"]
    fileName = request.form["fileName"]
    if keyword == "" or fileName == "":
        return jsonify({"result": False, "message": "未入力の項目があります。"})
    if img_file.filename == '':
        return jsonify({
            "result": False, "message": "選択したファイルの名前がありません。"
        })
    if not allowed_file(img_file.filename):
        return jsonify({
            "result": False, "message": "このファイル形式は読み込めません。"
        })
    if not allowed_file(fileName):
        return jsonify({
            "result": False, "message": "このファイル形式で保存することはできません。"
        })

    img_array = np.asarray(bytearray(img_file.stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    data = {
        "keyword": keyword,
        "img": img,
        "fileName": fileName
    }
    
    return jsonify({ "result": True })


if __name__ == '__main__':
    app.run()
