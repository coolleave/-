from flask import Flask, render_template, request, abort


app = Flask(__name__)


@app.route("/index", methods=["get", "post"])
def info():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        if username == "admin" and password == "123":
            return "login successedly"
    else:
        abort(404)


@app.errorhandler(404)
def handle_404_error(err):
    return render_template("hand_404.html")


if __name__ == '__main__':
    app.run()
