import tkinter as tk
from tkinter import messagebox

def create_button():
    # Lấy thông tin từ Entry
    button_name = name_var.get()
    if not button_name.strip():
        messagebox.showerror("Lỗi", "Vui lòng nhập tên nút!")
        return

    # Tạo Button mới
    new_button = tk.Button(root, text=button_name, command=lambda: button_action(button_name))
    new_button.pack(pady=5)

    # Xóa nội dung trong Entry
    name_var.set("")

def button_action(name):
    # Hành động khi nhấn nút
    messagebox.showinfo("Thông báo", f"Bạn đã nhấn nút '{name}'!")

def display_selection():
    # Hiển thị lựa chọn RadioButton
    selected_gender = gender_var.get()
    terms_accepted = "đã" if terms_var.get() else "chưa"
    messagebox.showinfo("Thông tin", f"Giới tính: {selected_gender}\nĐiều khoản: {terms_accepted} đồng ý")

# Tạo giao diện chính
root = tk.Tk()
root.title("Tạo Nút và Tương Tác")
root.geometry("400x400")

# Khởi tạo StringVar để quản lý dữ liệu
name_var = tk.StringVar()
gender_var = tk.StringVar(value="Chưa chọn")
terms_var = tk.BooleanVar(value=False)

# Tiêu đề
title_label = tk.Label(root, text="Đăng ký thông tin và tạo nút", font=("Arial", 14,"bold"))
title_label.pack(pady=10)

# Nhãn và trường nhập
name_label = tk.Label(root, text="Tên nút:")
name_label.pack(pady=5)

name_entry = tk.Entry(root, textvariable=name_var, width=30)
name_entry.pack(pady=5)

# Nút thêm
add_button = tk.Button(root, text="Thêm Nút", command=create_button, bg="blue", fg="white")
add_button.pack(pady=10)

# RadioButton để chọn giới tính
gender_label = tk.Label(root, text="Giới tính:")
gender_label.pack(pady=5)

male_rb = tk.Radiobutton(root, text="Nam", variable=gender_var, value="Nam")
male_rb.pack()

female_rb = tk.Radiobutton(root, text="Nữ", variable=gender_var, value="Nữ")
female_rb.pack()

# Checkbox để đồng ý điều khoản
terms_cb = tk.Checkbutton(root, text="Đồng ý với điều khoản", variable=terms_var)
terms_cb.pack(pady=10)

lab = tk.Label(root,text="-----**ooo___ooo**-----")
lab.pack(pady=10)
# Nút hiển thị lựa chọn
submit_button = tk.Button(root, text="Hiển thị lựa chọn", command=display_selection, bg="green", fg="white")
submit_button.pack(pady=10)

# Chạy giao diện
root.mainloop()
