import tkinter as tk
from PIL import Image, ImageTk

# Kullanıcı adı ve şifre bilgileri
user_credentials = {
    "username": "user",
    "password": "123"
}

image_paths = [
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/2048-game.png",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/angrybirds.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/connect4.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/connect4.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/flappy_bird.jpeg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/rememberme.jpg",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/sudoku_logo.png",
    "C:/Users/90541/PycharmProjects/OyunSkor/static/images/supermario.jpg"
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


def play_button_clicked(image_index):
    print(f"PLAY button clicked for image {image_index + 1}!")
    # Launcher burada yüklensin

def show_images_with_play_buttons():
    # Create the main window
    root = tk.Tk()
    root.title("Game Console")

    # Create a frame to hold the images and buttons
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Define the number of columns for images
    num_columns = 4

    # Iterate through each image path and create corresponding labels and buttons
    for i, image_path in enumerate(image_paths):
        # Load the image
        image = Image.open(image_path)

        # Resize the image to fit into the frame
        image.thumbnail((200, 200))

        # Convert image to PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        label = tk.Label(frame, image=photo)
        label.grid(row=i // num_columns * 2, column=i % num_columns)

        # Function to prevent garbage collection of the PhotoImage object
        label.image = photo

        # Create PLAY button for each image
        play_button = tk.Button(frame, text="PLAY", command=lambda idx=i: play_button_clicked(idx))
        play_button.grid(row=i // num_columns * 2 + 1, column=i % num_columns, pady=(0, 10))

    # Center the frame
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - (200 * num_columns)) // 2
    y = (screen_height - (200 * ((len(image_paths) + num_columns - 1) // num_columns * 2))) // 2
    root.geometry(f"{200 * num_columns + 10}x{200 * ((len(image_paths) + num_columns - 1) // num_columns * 2)}+{x}+{y}")

    # Run the Tkinter event loop
    root.mainloop()

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
