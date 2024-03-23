import subprocess

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Statik dosyalar için klasör yapılandırması
app.config['STATIC_FOLDER'] = 'static'
app.config['STATIC_URL_PATH'] = '/static'

@app.route('/main')
def ana_sayfa():
    oyunlar = [
        {"ad": "2048", "resim": "2048-game.png", "detaylar": "2048 oyunu hakkında detaylar...", "link": "#"},
        {"ad": "Angry Birds", "resim": "angrybirds.jpeg", "detaylar": "Angry Birds oyunu hakkında detaylar...",
         "link": "#"},
        {"ad": "Connect-4", "resim": "connect4.jpeg", "detaylar": "Connect-4 oyunu hakkında detaylar...", "link": "#"},
        {"ad": "Flappy Bird", "resim": "flappy bird.jpeg", "detaylar": "Flappy Bird oyunu hakkında detaylar...",
         "link": "#"},
        {"ad": "RememberMe", "resim": "rememberme.jpg", "detaylar": "RememberMe oyunu hakkında detaylar...",
         "link": "#"},
        {"ad": "Sudoku", "resim": "sudoku_logo.png", "detaylar": "Sudoku oyunu hakkında detaylar...", "link": "#"},
        {"ad": "Super Mario Brothers", "resim": "supermario.jpg",
         "detaylar": "Super Mario Brothers oyunu hakkında detaylar...", "link": "#"}
    ]
    return render_template('index.html', oyunlar=oyunlar)


@app.route('/oyna/2048')
def oyna_2048():
    subprocess.run(['python', 'C:\\Users\\90541\\PycharmProjects\\OyunSkor\\2048 Oyunu\\2048.py'])
    return redirect(url_for('ana_sayfa'))


@app.route('/oyna/angry-birds')
def oyna_angry_birds():
    subprocess.run(['python', 'C:\\Users\\90541\\PycharmProjects\\OyunSkor\\Angry Birds\\sourcecode\\Angry Birds.py'])
    return redirect(url_for('ana_sayfa'))


@app.route('/oyna/connect-4')
def oyna_connect_4():
    subprocess.run(['python', 'C:\\Users\\90541\\PycharmProjects\\OyunSkor\\Connect-4\\connect4.py'])
    return redirect(url_for('ana_sayfa'))


@app.route('/oyna/flappy-bird')
def oyna_flappy_bird():
    subprocess.run(['python', 'C:\\Users\\90541\\PycharmProjects\\OyunSkor\\Flappy Bird\\final\\FlappyBird.py'])
    return redirect(url_for('ana_sayfa'))


@app.route('/oyna/sudoku')
def oyna_sudoku():
    subprocess.run(['python', 'C:\\Users\\90541\\PycharmProjects\\OyunSkor\\Sudoku\\sudoku.py'])
    return redirect(url_for('ana_sayfa'))


if __name__ == '__main__':
    app.run(debug=True)
