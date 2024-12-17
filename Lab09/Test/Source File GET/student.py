from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def student_form():
    return render_template('student_form.html')

@app.route('/student', methods=["GET"])
def student_result():
    name = request.args.get('html_name')
    marks = int( request.args.get('html_marks'))
    return render_template( 'student_result.html', html_name=name, html_marks=marks)

if __name__ == "__main__":
    app.run()