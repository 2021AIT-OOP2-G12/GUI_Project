from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_upload")
def search_upload():
    return()

@app.route("/search_result")
def search_result():
    return()



if __name__ == '__main__':
    app.run()
