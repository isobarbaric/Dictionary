import os
from flask import Flask, redirect, request, url_for, render_template
from word import Word

app = Flask(__name__)

static_path = os.path.join(os.path.dirname(__file__), 'static')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('definition', word = request.form.get('query')))
    else:
        return render_template("base.html", static_path = static_path)

@app.route('/<word>/')
def definition(word):
    current_word = Word(word)
    if current_word.meanings is None:
        return render_template('error.html')
    else:
        return render_template('result.html', search_query = current_word)

if __name__ == "__main__":
    app.run(debug=True)
