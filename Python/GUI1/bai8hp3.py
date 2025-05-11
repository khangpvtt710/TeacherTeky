import subprocess
import tkinter as tk
from tkinter import Menu, Toplevel
import webbrowser

def vd():
    root1 = tk.Tk()
    root1.title("dang nhap")
    root1.geometry("400x400")
    lb = tk.Label(root1, text = "dang ky")
    lb.pack()

def new_file():
    print("New File created")

def open_file():
    print("File opened")

def save_file():
    print("File saved")

def cut_text():
    print("Text cut")

def copy_text():
    print("Text copied")

def paste_text():
    print("Text pasted")

def open_url():
    # URL của trang web bạn muốn mở
    webbrowser.open("https://www.google.com")

def open_application():
    # Mở ứng dụng, ví dụ: Notepad trên Windows
    subprocess.run(["notepad.exe"])

def about_app():
    # Tạo cửa sổ phụ (About window)
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x200")
    
    label = tk.Label(about_window, text="Python IDLE Replica\nCreated using Tkinter", font=("Courier", 12))
    label.pack(pady=20)
    
    web_button = tk.Button(about_window, text="google", command=open_url)
    web_button.pack(pady=10)
    application_button = tk.Button(about_window, text="notepad", command=open_application)
    application_button.pack(pady=10)
    
    # Thêm nút đóng cửa sổ phụ
    close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
    close_button.pack(pady=10)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Python IDLE Replica")
root.geometry("600x400")

tk.Button(root, text="Close", command=vd).pack()
# Tạo menu chính
menu_bar = Menu(root)

# Tạo menu File
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Tạo menu Edit
edit_menu = Menu(menu_bar, tearoff=0)

# Tạo menu con "dit_menu" 
dit_menu = Menu(edit_menu, tearoff=0)
dit_menu.add_command(label="Cut", command=cut_text)
dit_menu.add_command(label="Copy", command=copy_text)
dit_menu.add_command(label="Paste", command=paste_text)

sip_menu = Menu(menu_bar, tearoff=0)
sip_menu.add_command(label="Cut", command=cut_text)
sip_menu.add_command(label="Copy", command=copy_text)
sip_menu.add_command(label="Paste", command=paste_text)
# Thêm menu con vào menu Edit
edit_menu.add_cascade(label="dit", menu=dit_menu)
edit_menu.add_cascade(label="sip", menu=sip_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Tạo menu View
view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Zoom In", command=lambda: print("Zoom In"))
view_menu.add_command(label="Zoom Out", command=lambda: print("Zoom Out"))
menu_bar.add_cascade(label="View", menu=view_menu)

# Tạo menu Help
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_app)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Gắn menu vào cửa sổ chính
root.config(menu=menu_bar)

# Thêm Text widget để nhập liệu, tương tự Python IDLE
text_area = tk.Text(root, wrap="word", font=("Courier", 12))
text_area.pack(expand=1, fill="both")

# Bắt đầu vòng lặp giao diện
root.mainloop()
