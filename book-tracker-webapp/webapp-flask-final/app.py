from flask import Flask, render_template

app = Flask(__name__)

books = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/completed_books')
def completed_books():
    return render_template('completed_books.html')

@app.route('/favorite_books')
def favorite_books():
    return render_template('favorite_books.html')

@app.route('/author')
def favorite_books():
    return render_template('author.html')

if __name__ == '__main__':
    app.run(debug=True)
