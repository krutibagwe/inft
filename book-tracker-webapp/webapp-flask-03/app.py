from flask import Flask, render_template

app = Flask(__name__)

books = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/completed-books')
def completed_books():
    return render_template('completed_books.html')

@app.route('/favorite-books')
def favorite_books():
    return render_template('favorite_books.html')

if __name__ == '__main__':
    app.run(debug=True)
