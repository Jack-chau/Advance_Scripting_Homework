from flask import Flask, request, render_template, make_response, url_for, redirect
app = Flask( __name__ )

@app.route('/')
def index():
    return render_template( 'setcookie.html' )

@app.route('/setcookie', methods=["POST"])
def setcookie():
    if request.method == "POST" :
        user = request.form["id"]
        resp = make_response( redirect( url_for("readcookie")))
        resp.set_cookie("userID",user)
        return resp

@app.route('/readcookie')
def readcookie():
    if "userID" in request.cookies:
        name = request.cookies.get("userID")
        return f"<h1>Welcome {name} </h1>"
    else :
        return f"<h1>Cookie 'userID' NOT found</h1>"

if __name__ == "__main__":
    app.run()