import os
import csv # Thêm thư viện csv

# if os.path.exists("novel.txt"):
#     os.remove("novel.txt")
#     print("Đã xóa file thành công!")
# else:
#     print("File không tồn tại, bỏ qua lệnh xóa.")

# with open("csv_file.txt") as f:
#     csv_f = csv.reader(f)
#     for row in csv_f:
#         name, phone, role = row
#         print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))


# # PHẦN 1: MẪU TỰ ĐỘNG TẠO FILE DỮ LIỆU ĐẦU VÀO SOUTWARE.CSV
# software_data = """name,version,status,users
# MailTree,5.34,production,324
# CalDoor,1.25.1,beta,22
# Chatty Chicken,0.34,alpha,4"""

# with open("software.csv", "w", encoding="utf-8") as f:
#     f.write(software_data.strip())

# # PHẦN 2: ỨNG DỤNG CSV.DICTREADER ĐỂ ĐỌC FILE VÀ IN KẾT QUẢ
# print("--- KẾT QUẢ ĐỌC FILE SOFTWARE.CSV ---")
# # Mở file dữ liệu ở chế độ đọc mặc định
# with open('software.csv', 'r', encoding='utf-8') as software:
#     # Khởi tạo bộ đọc Dictionary, tự động bốc hàng 1 làm Key
#     reader = csv.DictReader(software)

#     # Duyệt qua từng hàng dữ liệu (mỗi hàng lúc này là một Dictionary)
#     for row in reader:
#         # Truy cập trực tiếp giá trị bằng tên cột làm Key thay vì dùng index số
#         print("{} has {} users".format(row["name"], row["users"]))

# # PHẦN 3: ỨNG DỤNG CSV.DICTWRITER ĐỂ TẠO FILE DỮ LIỆU MỚI
# # Chuẩn bị danh sách dữ liệu mẫu dạng List of Dictionaries
# users = [
#     {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
#     {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
#     {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
# ]

# # Khai báo danh sách các tên cột bắt buộc theo đúng cấu trúc dữ liệu
# keys = ["name", "username", "department"]

# # Mở file ghi mới 'by_department.csv', cấu hình newline='' để tránh lỗi dòng trống trên Windows
# with open('by_department.csv', 'w', newline='', encoding='utf-8') as by_department:
#     # Khởi tạo bộ ghi Dictionary và truyền cấu trúc cột vào tham số fieldnames
#     writer = csv.DictWriter(by_department, fieldnames=keys)

#     # Lệnh ghi hàng tiêu đề (Header row) đầu tiên dựa vào biến keys
#     writer.writeheader()

#     # Ghi hàng loạt toàn bộ danh sách các bản ghi từ cấu trúc mảng Dictionary xuống file
#     writer.writerows(users)

# print("\n--- KẾT QUẢ GHI FILE BY_DEPARTMENT.CSV THÀNH CÔNG ---")
# with open('by_department.csv', 'r', encoding='utf-8') as f:
#     print(f.read())

# import csv

# # Bước 1: Tự động khởi tạo file dữ liệu mẫu 'software.csv' để làm dữ liệu đầu vào
# raw_data = """name,version,status,users
# MailTree,5.34,production,324
# CalDoor,1.25.1,beta,22
# Chatty Chicken,0.34,alpha,4"""

# with open("software.csv", "w", encoding="utf-8") as f:
#     f.write(raw_data.strip())

# # Bước 2: ỨNG DỤNG DICTREADER ĐỂ ĐỌC FILE BẰNG TÊN CỘT
# print("--- KẾT QUẢ ĐỌC FILE DÙNG DICTREADER ---")
# with open('software.csv', 'r', encoding='utf-8') as software:
#     reader = csv.DictReader(software)
#     for row in reader:
#         # Truy cập dữ liệu trực tiếp bằng tên cột, không sợ lệch chỉ số index số
#         print("{} has {} users".format(row["name"], row["users"]))

# # Bước 3: ỨNG DỤNG DICTWRITER ĐỂ TẠO FILE TỪ DANH SÁCH DICTIONARY
# # Chuẩn bị mảng dữ liệu cấu trúc dạng List of Dictionaries
# users = [
#     {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
#     {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
#     {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
# ]

# # Xác định danh sách các cột bắt buộc sẽ xuất hiện trong file CSV mới
# keys = ["name", "username", "department"]

# # Mở file ghi mới, cấu hình newline='' để chống lỗi sinh dòng trống thừa khi chạy trên Windows
# with open('by_department.csv', 'w', newline='', encoding='utf-8') as by_department:
#     # Khởi tạo DictWriter và cấu hình móng các cột qua tham số fieldnames
#     writer = csv.DictWriter(by_department, fieldnames=keys)

#     # Lệnh ghi dòng tiêu đề cột (Header row) đầu tiên dựa vào biến keys
#     writer.writeheader()

#     # Dịch toàn bộ mảng dữ liệu Dictionary thành text và đẩy hàng loạt xuống ổ cứng
#     writer.writerows(users)

# print("\n--- KẾT QUẢ KIỂM TRA FILE BY_DEPARTMENT.CSV VỪA GHI ---")
# with open('by_department.csv', 'r', encoding='utf-8') as f:
#     print(f.read())

import csv

# PHẦN 1: TẠO FILE CSV DÙNG DẤU CHẤM PHẨY RE-FORMAT (BIẾN THỂ DIALECT)
# Giả lập file CSV xuất ra từ một hệ thống sử dụng dấu ';' thay vì dấu ','
# custom_csv_data = """Name;Department;Salary
# Aisha Khan;Engineering;80000
# Jules Lee;Marketing;67000
# Queenie Corbit;Human Resources;90000"""

# with open("custom_employees.csv", "w", encoding="utf-8") as f:
#     f.write(custom_csv_data.strip())

# # PHẦN 2: ĐỌC FILE VỚI CẤU HÌNH DELIMITER TÙY BIẾN VÀ LỆNH NEXT()
# print("--- CHẠY SCRIPT.PY: ĐỌC CSV TÙY BIẾN ---")

# with open("custom_employees.csv", "r", encoding="utf-8") as f:
#     # Khai báo bộ đọc kèm cấu hình delimiter=';' để Python không bị nhận diện sai cột
#     reader = csv.reader(f, delimiter=';')

#     # Sử dụng hàm next() để hớt dòng đầu tiên (Header row) ra ngoài
#     header = next(reader)
#     print("Dòng tiêu đề bóc tách riêng: {}".format(header))
#     print("-" * 40)

#     # Vòng lặp for lúc này chỉ duyệt qua các dòng dữ liệu thô, không bị dính dòng tiêu đề
#     for row in reader:
#         name, department, salary = row
#         print("Nhân viên: {} | Phòng: {} | Lương: {}".format(name, department, salary))