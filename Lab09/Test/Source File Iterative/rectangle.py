from flask import Flask, render_template
class Rectangel:
    def __init__( self, length, width ):
        self.__length = length
        self.__width = width
    def get_length( self ):
        return self.__length
    def get_width( self ):
        return self.__width
    def find_area( self ) :
        return self.__length * self.__width

list_rectangle = list()
list_rectangle.append( Rectangel(1,1))
list_rectangle.append( Rectangel(1,2))
list_rectangle.append( Rectangel(2,2))
list_rectangle.append( Rectangel(2,3))
list_rectangle.append( Rectangel(3,3))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template( 'rectangle.html', html_list=list_rectangle)

if __name__ == "__main__":
    app.run()