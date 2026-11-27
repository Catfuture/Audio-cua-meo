
import os

# Tạo thư mục chứa các file
folder = "DanhSach_File"
os.makedirs(folder, exist_ok=True)

# Tạo 100 file txt
for i in range(193, 205):
    filename = f"Chuong_{i}.txt"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write("")

print("Đã tạo thành công 100 file TXT!")
