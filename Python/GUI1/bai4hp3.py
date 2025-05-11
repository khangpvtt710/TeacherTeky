import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút "Login"
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Kiểm tra thông tin đăng nhập (demo với giá trị cố định)
    if username == "admin" and password == "123456":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Login Window")
root.geometry("300x200")

icon = tk.PhotoImage(file="khang.png")
root.iconphoto(False, icon)

# Label và Entry cho Username
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Label và Entry cho Password
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Button Login
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack(pady=10)

# Khởi chạy giao diện
root.mainloop()