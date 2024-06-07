import random
import smtplib
import string
import subprocess
import tkinter as tk
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
from pymongo import MongoClient

# MongoDB bağlantısı
client = MongoClient("mongodb://localhost:27017/")
db = client["OyunSkorPythonProject"]
users_collection = db["users"]


def generate_password_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


def send_email(to_address, subject, message):
    from_address = "oyunskorpythonprojesi@gmail.com"
    password = "bjex ufup tdss xmnr"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Hata: {e}")
        return False


def register():
    user_name = entry_name.get()
    user_mail = entry_mail.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    user_emotion = emotion_var.get()
    user_age = entry_age.get()

    if password != confirm_password:
        messagebox.showerror("Hata", "Şifreler uyuşmuyor!")
        return

    password_key = generate_password_key()

    user_data = {
        "user_name": user_name,
        "user_mail": user_mail,
        "password": password,
        "user_emotion": user_emotion,
        "user_age": int(user_age),
        "user_password_key": password_key
    }

    users_collection.insert_one(user_data)

    subject = "Kayıt Başarılı - Şifre Anahtarınız"
    message = f"Merhaba {user_name},\n\nKayıt işleminiz başarılı. Şifre sıfırlama anahtarınız: {password_key}\n\nİyi günler dileriz."

    if send_email(user_mail, subject, message):
        messagebox.showinfo("Başarılı", "Kayıt başarılı ve e-posta gönderildi!")
    else:
        messagebox.showerror("Hata", "Kayıt başarılı ancak e-posta gönderilemedi.")

    show_login_frame()


def login():
    user_mail = entry_login_mail.get()
    password = entry_login_password.get()

    user = users_collection.find_one({"user_mail": user_mail, "password": password})

    if user:
        messagebox.showinfo("Başarılı", f"Hoşgeldiniz, {user['user_name']}!")
        root.destroy()  # Giriş penceresini kapat
        show_images_with_play_buttons()  # Menü ekranını göster
    else:
        messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")


def show_login_frame():
    frame_register.pack_forget()
    frame_reset_password.pack_forget()
    frame_login.pack()


def show_register_frame():
    frame_login.pack_forget()
    frame_reset_password.pack_forget()
    frame_register.pack()


def show_reset_password_frame():
    frame_login.pack_forget()
    frame_register.pack_forget()
    frame_reset_password.pack()


def reset_password():
    user_mail = entry_reset_mail.get()
    password_key = entry_reset_key.get()
    new_password = entry_new_password.get()
    confirm_new_password = entry_confirm_new_password.get()

    if new_password != confirm_new_password:
        messagebox.showerror("Hata", "Yeni şifreler uyuşmuyor!")
        return

    user = users_collection.find_one({"user_mail": user_mail, "user_password_key": password_key})

    if user:
        users_collection.update_one(
            {"user_mail": user_mail},
            {"$set": {"password": new_password}}
        )
        messagebox.showinfo("Başarılı", "Şifre başarıyla güncellendi!")
        show_login_frame()
    else:
        messagebox.showerror("Hata", "Geçersiz e-posta veya şifre sıfırlama anahtarı!")


# Oyunların görüntülerinin yol listesi
image_paths = [
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/2048-game.png",
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/angrybirds.jpeg",
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/connect4.jpeg",
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/connect4againstai.jpeg",
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/flappy_bird.jpeg",
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/rememberme.jpg",
    "C:/Users/ebube/PycharmProjects/OyunSkor/static/images/sudoku_logo.png",
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/tetris-logo.png",
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/BaloonShooter.png",
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/pingpong.jpg",

    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/pingpong.jpg", #chess
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/pingpong.jpg", #snake
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/pingpong.jpg", #8ballpool
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/pingpong.jpg", #target practice
    "c:/Users/ebube/PycharmProjects/OyunSkor/static/images/pingpong.jpg", #car racing

]

# Oyunların detayları listesi
game_details = [
    {
        "title": "2048",
        "description": "Bu popüler sayı bulmaca oyununda 2048 sayısını oluşturun!",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "2048.py"
    },
    {
        "title": "Angry Birds",
        "description": "Domuzlara karşı kuşlarınızı fırlatın ve seviyeleri geçin.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "AngryBirdsOyunu/AngryBirds.py"
    },
    {
        "title": "Connect 4",
        "description": "Dört aynı rengin yatay, dikey veya çapraz hizalanmasını sağlayın.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "connect4.py"
    },
    {
        "title": "Connect 4 (Yapay Zeka Karşı)",
        "description": "Yapay zekaya karşı Connect 4 oynayın.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "connect4withai.py"
    },
    {
        "title": "Flappy Bird",
        "description": "Engeller arasından geçerek mümkün olduğunca uzağa uçun.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "FlappyBird.py"
    },
    {
        "title": "Match Me!",
        "description": "Bir kart eşleştirme oyunu.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "app.py"
    },
    {
        "title": "Sudoku",
        "description": "Sayı bulmacalarını çözerek beyninizi zorlayın.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "sudoku.py"
    },
    {
        "title": "Tetris",
        "description": "Blokları düşürerek tam sıralar oluşturun ve puan kazanın.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "tetris.py"
    },
    {
        "title": "Baloon Shooter",
        "description": "Hedefteki balonları vurarak puan kazanın.",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "BaloonShooter.py"
    },
    {
        "title": "Pong",
        "description": "Klasik Pong oyununu oyna ve rakibini yen!",
        "youtube_url": "https://www.youtube.com/watch?v=6FQDXpNtwts",
        "executable_path": "Pong.py"
    },
    {
        "title": "Chess",
        "description": "Satranç oyunları yüzyıllardır oynanan bir strateji oyunudur.",
        "youtube_url": "https://www.youtube.com/watch?v=",
        "executable_path": "chess/chess.py"
    },
    {
        "title": "Classic Snake",
        "description": "Yılan oyunu.",
        "youtube_url": "https://www.youtube.com/watch?",
        "executable_path": "snake.py"
    },
    {
        "title": "8 Ball Pool",
        "description": "Bilardo oyunu.",
        "youtube_url": "https://www.youtube.com/watch?",
        "executable_path": "8ballpool.py"
    },
    {
        "title": "Poligon",
        "description": "Poligon oyunu.",
        "youtube_url": "https://www.youtube.com/watch?",
        "executable_path": "ShootingGallery/poligon.py"
    },
    {
        "title": "Car Racing",
        "description": "Poligon oyunu.",
        "youtube_url": "https://www.youtube.com/watch?",
        "executable_path": "CarRacing/car_racing.py"
    }

]


def play_button_clicked(game_index):
    executable_path = game_details[game_index]["executable_path"]
    if executable_path:
        subprocess.Popen(["python", executable_path])
    else:
        print("Bu oyun için yürütülebilir bir dosya bulunamadı.")


def show_images_with_play_buttons():
    # Create the main window
    root = tk.Tk()
    root.title("Game Console Developed by Ebubekir Kurt")

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
        label.grid(row=i // num_columns * 3, column=i % num_columns)

        # Function to prevent garbage collection of the PhotoImage object
        label.image = photo

        # Create "Detaylar" button for each game
        details_button = tk.Button(frame, text="Detaylar", command=lambda idx=i: show_game_details(idx))
        details_button.grid(row=i // num_columns * 3 + 1, column=i % num_columns, pady=(0, 5))

        # Create PLAY button for each game
        play_button = tk.Button(frame, text="OYNA!", command=lambda idx=i: play_button_clicked(idx))
        play_button.grid(row=i // num_columns * 3 + 2, column=i % num_columns, pady=(0, 10))

    # Center the frame
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - (200 * num_columns)) // 2
    y = (screen_height - (200 * ((len(image_paths) + num_columns - 1) // num_columns * 3))) // 2
    root.geometry("1200x950")

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


# Tkinter arayüzü
root = tk.Tk()
root.title("Kullanıcı Kayıt ve Giriş")

# Kayıt Formu
frame_register = tk.Frame(root, padx=10, pady=10)

label_name = tk.Label(frame_register, text="İsim")
label_name.grid(row=0, column=0, sticky=tk.W, pady=2)
entry_name = tk.Entry(frame_register)
entry_name.grid(row=0, column=1, pady=2)

label_mail = tk.Label(frame_register, text="Mail :")
label_mail.grid(row=1, column=0, sticky=tk.W, pady=2)
entry_mail = tk.Entry(frame_register)
entry_mail.grid(row=1, column=1, pady=2)

label_password = tk.Label(frame_register, text="Şifre :")
label_password.grid(row=2, column=0, sticky=tk.W, pady=2)
entry_password = tk.Entry(frame_register, show="*")
entry_password.grid(row=2, column=1, pady=2)

label_confirm_password = tk.Label(frame_register, text="Şifre (Tekrar) :")
label_confirm_password.grid(row=3, column=0, sticky=tk.W, pady=2)
entry_confirm_password = tk.Entry(frame_register, show="*")
entry_confirm_password.grid(row=3, column=1, pady=2)

label_emotion = tk.Label(frame_register, text="Duygu :")
label_emotion.grid(row=4, column=0, sticky=tk.W, pady=2)
emotion_var = tk.StringVar()
emotion_dropdown = ttk.Combobox(frame_register, textvariable=emotion_var)
emotion_dropdown['values'] = ("Happy", "Sad", "Excited", "Angry", "Neutral")
emotion_dropdown.grid(row=4, column=1, pady=2)

label_age = tk.Label(frame_register, text="Yaş")
label_age.grid(row=5, column=0, sticky=tk.W, pady=2)
entry_age = tk.Entry(frame_register)
entry_age.grid(row=5, column=1, pady=2)

button_register = tk.Button(frame_register, text="Kayıt Ol", command=register)
button_register.grid(row=6, columnspan=2, pady=10)

button_show_login = tk.Button(frame_register, text="Giriş Ekranına Dön", command=show_login_frame)
button_show_login.grid(row=7, columnspan=2)

# Giriş Formu
frame_login = tk.Frame(root, padx=10, pady=10)

label_login_mail = tk.Label(frame_login, text="Mail :")
label_login_mail.grid(row=0, column=0, sticky=tk.W, pady=2)
entry_login_mail = tk.Entry(frame_login)
entry_login_mail.grid(row=0, column=1, pady=2)

label_login_password = tk.Label(frame_login, text="Şifre :")
label_login_password.grid(row=1, column=0, sticky=tk.W, pady=2)
entry_login_password = tk.Entry(frame_login, show="*")
entry_login_password.grid(row=1, column=1, pady=2)

button_login = tk.Button(frame_login, text="Giriş Yap", command=login)
button_login.grid(row=2, columnspan=2, pady=10)

button_forgot_password = tk.Button(frame_login, text="Şifremi Unuttum", command=show_reset_password_frame)
button_forgot_password.grid(row=3, columnspan=2)

button_show_register = tk.Button(frame_login, text="Kayıt Ol", command=show_register_frame)
button_show_register.grid(row=4, columnspan=2)

# Şifre Sıfırlama Formu
frame_reset_password = tk.Frame(root, padx=10, pady=10)

label_reset_mail = tk.Label(frame_reset_password, text="Mail")
label_reset_mail.grid(row=0, column=0, sticky=tk.W, pady=2)
entry_reset_mail = tk.Entry(frame_reset_password)
entry_reset_mail.grid(row=0, column=1, pady=2)

label_reset_key = tk.Label(frame_reset_password, text="Şifre Sıfırlama Anahtarı :")
label_reset_key.grid(row=1, column=0, sticky=tk.W, pady=2)
entry_reset_key = tk.Entry(frame_reset_password)
entry_reset_key.grid(row=1, column=1, pady=2)

label_new_password = tk.Label(frame_reset_password, text="Yeni Şifre :")
label_new_password.grid(row=2, column=0, sticky=tk.W, pady=2)
entry_new_password = tk.Entry(frame_reset_password, show="*")
entry_new_password.grid(row=2, column=1, pady=2)

label_confirm_new_password = tk.Label(frame_reset_password, text="Yeni Şifre (Tekrar) :")
label_confirm_new_password.grid(row=3, column=0, sticky=tk.W, pady=2)
entry_confirm_new_password = tk.Entry(frame_reset_password, show="*")
entry_confirm_new_password.grid(row=3, column=1, pady=2)

button_reset_password = tk.Button(frame_reset_password, text="Şifreyi Sıfırla", command=reset_password)
button_reset_password.grid(row=4, columnspan=2, pady=10)

button_show_login_from_reset = tk.Button(frame_reset_password, text="Giriş Ekranına Dön", command=show_login_frame)
button_show_login_from_reset.grid(row=5, columnspan=2)

# Uygulama başladığında login ekranını göster
show_login_frame()

root.mainloop()


