from flask import Flask,url_for , render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    message = "Hello World!"
    return render_template("yuuai-home.html", message)

@app.route('/second')
def second_page():
    return "This is the second page"

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port = 80)
