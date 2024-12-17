from flask import Flask, render_template, request, make_response, redirect, url_for, session
import mysql.connector

class ConnectDB :
    try:
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Jack0303',
            database = 'student_db'
        )
        print( 'Opened database successfully')
    except mysql.connector.Error as e :
        print( e )

    def create_table():
        try :
            mycursor = ConnectDB.mydb.cursor()
            query = """
                        CREATE TABLE IF NOT EXISTS student_mark(
                            id VARCHAR(100),
                            name VARCHAR(100),
                            password VARCHAR(1000),
                            marks INTEGER
                        )
                    """
            mycursor.execute(query)
            ConnectDB.mydb.commit()
            print( "Table created successfully")
        except mysql.connector.Error as e :
            print( e )
    
    def insert_student( id, name, password, marks ):
        try:
            mycursor = ConnectDB.mydb.cursor()
            query = (f"INSERT INTO student_mark (id, name, password, marks)" +
                     f"VALUES ('{id}','{name}','{password}','{marks}')")
            mycursor.execute( query )
            ConnectDB.mydb.commit()
        except mysql.connector.Error as e :
            pritn( e )
    
    def read_all_students():
        try :
            mycursor = ConnectDB.mydb.cursor()
            query = f"SELECT * FROM student_mark"
            mycursor.execute( query )
            result = mycursor.fetchall()
            print( result )
            return result
        except mysql.connector.Error as e:
            print( e )
    
    def read_single_student( id ):
        try:
            mycursor = ConnectDB.mydb.cursor()
            query = f"SELECT * FROM student_mark WHERE id = '{id}'"
            mycursor.execute( query )
            result = mycursor.fetchone()
            print( result )
            return result
        except mysql.connector.Error as e:
            print( e )
    
    def auth_student( id, password ):
        try:
            mycursor = ConnectDB.mydb.cursor()
            query = f"SELECT COUNT(*) FROM student_mark WHERE id='{id}' and password = '{password}'"
            mycursor.execute( query )
            result = mycursor.fetchone()
            print( result )
            if result[0] == 1:
                return True
            else :
                return False
        except mysql.connector.Error as e:
            print( e )

app = Flask( __name__ )
app.secret_key = "any random string"

@app.route( '/add_student', methods = ["POST"] )
def add_sutdent() :
    if request.method == "POST" :
        msg = ""
        try:
            id = request.form['id']
            name = request.form['name']
            password = request.form['password']
            marks = int( request.form['marks'] )
            print( id, name, password, marks)
            ConnectDB.insert_student( id, name, password, marks )
        except mysql.connector.Error as e:
            print( e )
        return redirect( url_for('all_students'))

@app.route( '/logout' )
def logout():
    id = session.pop( 'id', None )
    return render_template("login.html", msg=f"User id {id} logout")

@app.route("/single_student")
def single_student():
    if "id" in session:
        id = session['id']
        result = ConnectDB.read_single_student( id )
        return render_template( "single_student.html", row=result)
    else :
        return render_template('login.html', msg="Please login first")

@app.route( '/all_students' )
def all_students():
    print( session )
    if session.get("id") == "admin":
        result = ConnectDB.read_all_students()
        return render_template("all_students.html", rows=result )
    else :
        return render_template( 'login.html', msg='Please login with admin')


@app.route( '/login', methods = ["POST"] )
def login():
    msg = ""
    if request.method == "POST" :
        id = request.form[ 'id' ]
        password = request.form["password"]
        if id == "admin" and password == "admin":
            session['id'] = id
            return redirect( url_for( 'all_students' ) )
        elif ConnectDB.auth_student( id, password ) :
            session['id'] = id
            return redirect( url_for( 'single_student' ) )
        else :
            resp = render_template( 'login.html', msg = "Login Fail")
        return resp

@app.route('/')
def home():
    return render_template( 'login.html', mas= "" )

if __name__ == "__main__":
    ConnectDB.create_table()
    app.run()




            

