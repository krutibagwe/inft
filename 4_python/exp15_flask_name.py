from flask import Flask
app = Flask(__name__)

@app.route('/Page1/<name>')
def hello_Subpage(name):
    return 'Hello %s!' % name

if __name__ == '__main__' :
    app.run()
