from flask import Flask, session, redirect, url_for, request, render_template
app = Flask(__name__)
app.secret_key = "any random string"

@app.route('/')
def index():
    if "username" in session:
        username = session["username"]
        return render_template( 'content.html', nm=username )
    return render_template( 'login.html' )

@app.route( '/login', methods=['POST'])
def login():
    if request.method == "POST":
        session["username"] = request.form['username']
        return redirect( url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect( url_for('index'))

if __name__ == "__main__":
    app.run()