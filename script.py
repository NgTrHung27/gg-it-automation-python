import os

if os.path.exists("novel.txt"):
    os.remove("novel.txt")
    print("Đã xóa file thành công!")
else:
    print("File không tồn tại, bỏ qua lệnh xóa.")