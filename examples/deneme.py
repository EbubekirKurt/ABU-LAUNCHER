import subprocess
import tkinter as tk
import webbrowser

import cv2
import pafy
from PIL import Image, ImageTk

# Kullanıcı adı ve şifre bilgileri
user_credentials = {
    "username": "user",
    "password": "123"
}

# Oyunların görüntülerinin yol listesi
image_paths = [
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/2048-game.png",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/angrybirds.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/connect4.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/connect4againstai.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/flappy_bird.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/rememberme.jpg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/sudoku_logo.png",
    "c:/Users/90541/PycharmProjects/OyunSkor/static/images/tetris-logo.png",
    "c:/Users/90541/PycharmProjects/OyunSkor/static/images/BaloonShooter.png",
    "c:/Users/90541/PycharmProjects/OyunSkor/static/images/pingpong.jpg",
]

# Oyunların detayları listesi
game_details = [
    {
        "title": "2048",
        "description": "Bu popüler sayı bulmaca oyununda 2048 sayısını oluşturun!",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/2048.py"
    },
    {
        "title": "Angry Birds",
        "description": "Domuzlara karşı kuşlarınızı fırlatın ve seviyeleri geçin.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/AngryBirdsOyunu/AngryBirds.py"
    },
    {
        "title": "Connect 4",
        "description": "Dört aynı rengin yatay, dikey veya çapraz hizalanmasını sağlayın.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/connect4.py"
    },
    {
        "title": "Connect 4 (Yapay Zeka Karşı)",
        "description": "Yapay zekaya karşı Connect 4 oynayın.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/connect4withai.py"
    },
    {
        "title": "Flappy Bird",
        "description": "Engeller arasından geçerek mümkün olduğunca uzağa uçun.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/FlappyBird.py"
    },
    {
        "title": "Remember Me",
        "description": "Daha sonra eklenecek.",
        "youtube_url": "",
        "executable_path": ""
    },
    {
        "title": "Sudoku",
        "description": "Sayı bulmacalarını çözerek beyninizi zorlayın.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/sudoku.py"
    },
    {
        "title": "Tetris",
        "description": "Blokları düşürerek tam sıralar oluşturun ve puan kazanın.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/tetris.py"
    },
    {
        "title": "Baloon Shooter",
        "description": "Hedefteki balonları vurarak puan kazanın.",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/BaloonShooter.py"
    },
    {
        "title": "Pong",
        "description": "Klasik Pong oyununu oyna ve rakibini yen!",
        "youtube_url": "https://www.youtube.com/watch?v=-rqRWzSP2iM&pp=ygUNMjA0OCB0dXRvcmlhbA%3D%3D",
        "executable_path": "C:/Users/90541/PycharmProjects/OyunSkor/Pong.py"
    }
]


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == user_credentials["username"] and password == user_credentials["password"]:
        login_window.destroy()  # Giriş penceresini kapat
        show_images_with_play_buttons()  # Menü ekranını göster
    else:
        # Hatalı giriş uyarısı
        error_label.config(text="Invalid username or password")


def play_button_clicked(game_index):
    executable_path = game_details[game_index]["executable_path"]
    if executable_path:
        subprocess.Popen(["python", executable_path])
    else:
        print("Bu oyun için yürütülebilir bir dosya bulunamadı.")


def show_images_with_play_buttons():
    # Create the main window
    root = tk.Tk()
    root.title("Game Console")

    # Welcome label
    welcome_label = tk.Label(root, text="Hoşgeldin. Oynamak istediğin oyunu seç.", font=("Helvetica", 14))
    welcome_label.pack(pady=(10, 20))

    # Create a frame to hold the images and buttons
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Define the number of columns for images
    num_columns = 5

    # Iterate through each game and create corresponding labels and buttons
    for i, game_info in enumerate(game_details):
        # Load the image
        image = Image.open(image_paths[i])

        # Resize the image to fit into the frame
        image.thumbnail((200, 200))

        # Convert image to PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        label = tk.Label(frame, image=photo)
        label.grid(row=i // num_columns * 4, column=i % num_columns)

        # Function to prevent garbage collection of the PhotoImage object
        label.image = photo

        # Create "Detaylar" button for each game
        details_button = tk.Button(frame, text="Detaylar", command=lambda idx=i: show_game_details(idx))
        details_button.grid(row=i // num_columns * 4 + 1, column=i % num_columns, pady=(0, 5))

        # Create PLAY button for each game
        play_button = tk.Button(frame, text="PLAY", command=lambda idx=i: play_button_clicked(idx))
        play_button.grid(row=i // num_columns * 4 + 2, column=i % num_columns, pady=(0, 5))

        # Create video frame for each game
        video_frame = tk.Frame(frame, width=200, height=100)
        video_frame.grid(row=i // num_columns * 4 + 3, column=i % num_columns, pady=(0, 5))

        # Display video if available
        youtube_url = game_details[i]["youtube_url"]
        if youtube_url:
            video_url = youtube_url
            video = pafy.new(video_url)
            best = video.getbest(preftype="mp4")
            video_url = best.url
            cap = cv2.VideoCapture(video_url)
            _, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame.thumbnail((200, 100))
            video_photo = ImageTk.PhotoImage(frame)
            video_label = tk.Label(video_frame, image=video_photo)
            video_label.image = video_photo
            video_label.pack()
        else:
            no_video_label = tk.Label(video_frame, text="Video Yok")
            no_video_label.pack()

    # Center the frame
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - (200 * num_columns)) // 2
    y = (screen_height - (200 * ((len(image_paths) + num_columns - 1) // num_columns * 4))) // 2
    root.geometry("1200x600")

    # Run the Tkinter event loop
    root.mainloop()


def show_game_details(game_index):
    details_window = tk.Toplevel()
    details_window.title("Oyun Detayları")
    details_window.geometry("400x250")

    title_label = tk.Label(details_window, text=game_details[game_index]["title"], font=("Helvetica", 16, "bold"))
    title_label.pack(pady=(10, 5))

    description_label = tk.Label(details_window, text=game_details[game_index]["description"], wraplength=380)
    description_label.pack(pady=5)

    youtube_url = game_details[game_index]["youtube_url"]
    if youtube_url:
        video_label = tk.Label(details_window, text="Oyun Videosu", font=("Helvetica", 12, "underline"), fg="blue",
                               cursor="hand2")
        video_label.pack(pady=5)
        video_label.bind("<Button-1>", lambda event, url=youtube_url: webbrowser.open(url))
    else:
        no_video_label = tk.Label(details_window, text="Bu oyun için bir video bulunmamaktadır.")
        no_video_label.pack(pady=5)


# Giriş ekranını oluştur
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("310x200")  # Pencere boyutunu ayarla

# Kullanıcı adı ve şifre girişi bileşenleri
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=(10, 0))  # Yükseklik boşluğunu ayarla
username_entry = tk.Entry(login_window)
username_entry.pack(pady=(0, 5))  # Yükseklik boşluğunu ayarla

password_label = tk.Label(login_window, text="Password:")
password_label.pack()  # Yükseklik boşluğunu ayarla
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=(0, 5))  # Yükseklik boşluğunu ayarla

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()  # Yükseklik boşluğunu ayarla

error_label = tk.Label(login_window, fg="red")
error_label.pack()  # Yükseklik boşluğunu ayarla

# Giriş ekranını göster
login_window.mainloop()
