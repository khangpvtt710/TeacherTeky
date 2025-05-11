import tkinter as tk
from tkinter import OptionMenu, StringVar, messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import Tk, Label
def create_button():
    # Lấy thông tin từ Entry
    button_name = name_var.get()
    if not button_name.strip():
        messagebox.showerror("Lỗi", "Vui lòng nhập tên nút!")
        return
    
    # Tạo Button mới
    new_button = tk.Button(root, text=button_name, command=lambda: button_action(button_name))
    new_button.pack(pady=10)
    
    #Tiêu chí	           pack()	                       grid()	                    place()
    #Mức độ đơn giản	Đơn giản nhất	                Trung bình	                    Khó nhất
    #Kiểm soát vị trí	Hạn chế (tuần tự)	            Linh hoạt theo lưới	            Chính xác tuyệt đối
    #Tự động giãn nở	    Có	                             Có	                            Không
    #Thích hợp cho	    Giao diện đơn giản, ít widget	Bố cục phức tạp, nhiều widget	Giao diện cần tọa độ chính xác
    
    # Xóa nội dung trong Entry
    name_var.set("")

def button_action(name):
    # Hành động khi nhấn nút
    messagebox.showinfo("Thông báo", f"Bạn đã nhấn nút '{name}'!") #f-string

# Tạo giao diện chính
root = tk.Tk()
root.title("Đăng Ký và Tạo Nút")
root.geometry("500x300")

# Khởi tạo StringVar để quản lý dữ liệu Entry
name_var = tk.StringVar()

# Tiêu đề
title_label = tk.Label(root, text="Đăng ký thông tin và tạo nút", font=("Arial", 14))
title_label.pack(pady=10)

# Nhãn và trường nhập
name_label = tk.Label(root, text="Tên nút:")
name_label.pack(pady=10)

name_entry = tk.Entry(root, textvariable=name_var, width=30, show='*')
name_entry.pack(pady=10)

var= StringVar()
list = ['nhat','han','trung','viet']
droplist = OptionMenu(root,var,*list)
var.set('contry')
droplist.config(width=20) # type: ignore
droplist.pack(pady=10) # type: ignore

combo = Combobox(root, font=('Time New Roman', 15))
combo['values']=('nhat','han','trung','viet')
combo.current(3)
combo.pack(pady=5)

# Nút thêm
add_button = tk.Button(root, text="Thêm Nút", command=create_button, bg="blue", fg="white")
add_button.pack(pady=0)

#thêm hình
width, height = 100, 200 #tạo 2 biến size
img = Image.open("khang1.jpg") #mở file hình ảnh
img_resized = img.resize((width, height), Image.Resampling.LANCZOS)  # Chỉnh kích thước
photo = ImageTk.PhotoImage(img_resized)
labe=Label(root,image=photo)
labe.place(x=0,y=0)
# Chạy giao diện
root.mainloop()
