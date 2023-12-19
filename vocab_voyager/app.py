import os
from flask import Flask, redirect, request, url_for, render_template
from word import Word

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('definition', word = request.form.get('query')))
    else:
        return render_template("base.html")

@app.route('/<word>/')
def definition(word):
    current_word = Word(word)
    if current_word.meanings is None:
        return render_template('error.html')
    else:
        return render_template('result.html', search_query = current_word)

if __name__ == "__main__":
    app.run(debug=True)
