from flask import Flask, render_template
from Animeparser import list_i

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/anime')
def anime():
    page_title = 'Anime'
    return render_template('anime.html', title=page_title)

@app.route('/manga')
def manga():
    return render_template('manga.html')

@app.route('/latest_anime')
def latest_anime():
    content_text = list_i
    page_title = '10 anime'
    return render_template('latest.html', title=page_title, content=content_text)

if __name__ == "__main__":
    app.run(debug=True)

