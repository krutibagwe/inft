from flask import Flask
app = Flask(__name__)

@app.route('/Page1/<int:age>')
def hello_Subpage(age):
    return "age: %d"%age

if __name__ == '__main__' :
    app.run()
