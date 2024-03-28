from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    # Oyun verileri (şimdilik basit olarak bir sözlük içinde)
    oyunlar = [
        {"ad": "2048", "resim": "2048-game.png",
         "detaylar": "2048, sayıları hareket ettirerek 2048'i elde etmeye çalıştığınız bağımlılık yaratan bir bulmaca oyunudur.",
         "link": "/oyna/2048"},
        {"ad": "Angry Birds", "resim": "angrybirds.jpeg",
         "detaylar": "Angry Birds, kuşların domuzlara karşı savaştığı eğlenceli bir fizik tabanlı bulmaca oyunudur.",
         "link": "/oyna/angry-birds"},
        {"ad": "Connect-4", "resim": "connect4.jpeg",
         "detaylar": "Connect-4, sıranızı kullanarak dört parçayı dikey, yatay veya çapraz olarak birleştirmeye çalıştığınız bir strateji oyunudur.",
         "link": "/oyna/connect-4"},
        {"ad": "Flappy Bird", "resim": "flappy bird.jpeg",
         "detaylar": "Flappy Bird, engeller arasından uçarak puan kazandığınız basit ve bağımlılık yaratan bir oyunudur.",
         "link": "/oyna/flappy-bird"},
        {"ad": "RememberMe", "resim": "rememberme.jpg",
         "detaylar": "RememberMe, hafızanızı test etmek için kartları eşleştirdiğiniz bir hafıza oyunudur.",
         "link": "/oyna/rememberme"},
        {"ad": "Sudoku", "resim": "sudoku_logo.png",
         "detaylar": "Sudoku, sayılarla dolu bir kareyi doldururken mantık ve strateji kullanmanızı gerektiren bir bulmaca oyunudur.",
         "link": "/oyna/sudoku"},
        {"ad": "Super Mario Brothers", "resim": "supermario.jpg",
         "detaylar": "Super Mario Brothers, Mario'nun maceralarını yaşadığı klasik bir platform oyunudur.",
         "link": "/oyna/super-mario-brothers"}
    ]

    return render_template('index.html', oyunlar=oyunlar)

if __name__ == '__main__':
    app.run(debug=True)
