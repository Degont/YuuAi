from flask import Flask,url_for , render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    message = "Hello World!"
    return render_template("yuuai-home.html", message=message)

@app.route('/second')
def second_page():
    message = "This is the second page"
    return render_template("second_page.html", message = message)

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port = 80)
