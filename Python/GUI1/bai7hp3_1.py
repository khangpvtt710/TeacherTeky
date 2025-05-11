import tkinter as tk

def show_popup(event):
    #Hiển thị Pop-up Menu khi nhấp chuột phải.
    popup_menu.tk_popup(event.x_root, event.y_root)

def open_toplevel():
    #Mở một cửa sổ Toplevel mới.
    new_window = tk.Toplevel(root)
    new_window.title("Toplevel Example")
    new_window.geometry("300x200")
    tk.Label(new_window, text="This is a Toplevel window").pack(pady=20)
    tk.Button(new_window, text="Close", command=new_window.destroy).pack()

def option_1():
    #Hành động khi chọn Option 1 trong Pull-down Menu.
    print("Option 1 Selected")

def option_2():
    #Hành động khi chọn Option 2 trong Pull-down Menu.
    print("Option 2 Selected")

def khang():
    print("khang")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Combined Example")
root.geometry("400x300")

menu = tk.Menu(root)
# Tạo thanh Pull-down Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Option 1", command=option_1)
file_menu.add_command(label="Option 2", command=option_2)
file_menu.add_command(label="khang",command=khang)
file_menu.add_separator()
file_menu.add_command(label="Open Toplevel", command=open_toplevel)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Tạo Pop-up Menu
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Pop-up Option 1", command=lambda: print("Pop-up Option 1 Selected"))
popup_menu.add_command(label="Pop-up Option 2", command=lambda: print("Pop-up Option 2 Selected"))
popup_menu.add_separator()
popup_menu.add_command(label="Exit", command=root.quit)

edit_menu=tk.Menu(root, tearoff=0)
edit_menu.add_command(label='khang2')
menu_bar.add_cascade(label="File2", menu=edit_menu)

# Gắn sự kiện chuột phải để hiển thị Pop-up Menu
root.bind("<Button-3>", show_popup)



# Nội dung giao diện chính
tk.Label(root, text="Right-click for Pop-up Menu\nUse the top menu for Pull-down options").pack(pady=50)

# Bắt đầu vòng lặp ứng dụng
root.mainloop()