import tkinter as tk
from tkinter import messagebox

def on_submit():
    """Xử lý khi bấm nút Submit."""
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    hobbies = [hobby for hobby, var in hobbies_vars.items() if var.get()]

    if not name or not age or not gender:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    message = f"Tên: {name}\nTuổi: {age}\nGiới tính: {gender}\nSở thích: {', '.join(hobbies) if hobbies else 'Không có'}"
    messagebox.showinfo("Thông tin người dùng", message)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng giao diện đồ họa")
root.geometry("400x400")

# Tiêu đề
title_label = tk.Label(root, text="Nhập thông tin của bạn",fg='blue' ,font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Nhập tên
frame_name = tk.Frame(root)
frame_name.pack(pady=5, padx=5)
tk.Label(frame_name, text="Họ và tên: ").pack(side=tk.LEFT)
entry_name = tk.Entry(frame_name, width=30)
entry_name.pack(side=tk.LEFT)

# Nhập tuổi
frame_age = tk.Frame(root)
frame_age.pack(pady=5)
tk.Label(frame_age, text="Tuổi: ").pack(side=tk.LEFT)
entry_age = tk.Entry(frame_age, width=30)
entry_age.pack(side=tk.LEFT)

# Lựa chọn giới tính
gender_var = tk.StringVar()
gender_label = tk.Label(root, text="Giới tính:")
gender_label.pack(pady=5)

gender_frame = tk.Frame(root)
gender_frame.pack()
tk.Radiobutton(gender_frame, text="Nam", variable=gender_var, value="Nam").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(gender_frame, text="Nữ", variable=gender_var, value="Nữ").pack(side=tk.LEFT, padx=10)

# Chọn sở thích
hobbies_vars = {
    "Thể thao": tk.BooleanVar(),
    "Âm nhạc": tk.BooleanVar(),
    "Đọc sách": tk.BooleanVar(),
    "Du lịch": tk.BooleanVar(),
}
hobbies_label = tk.Label(root, text="Sở thích:")
hobbies_label.pack(pady=5)

for hobby, var in hobbies_vars.items():
    tk.Checkbutton(root, text=hobby, variable=var).pack(anchor="w")

# Nút Submit
submit_button = tk.Button(root, text="Gửi thông tin", command=on_submit)
submit_button.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
