# =================================================================
# HỌ VÀ TÊN: Bùi Minh Hiếu
# MÃ SINH VIÊN: n25dtcn020
# BÀI TẬP: [Vận dụng cơ bản 2] Sai sót khi lấy thông tin sinh viên theo ID
# =================================================================

from fastapi import FastAPI

app = FastAPI()

# Dữ liệu danh sách sinh viên
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Bình"},
    {"id": 3, "name": "Cường"},
]

# Sửa 1: Đổi endpoint thành /students (danh từ số nhiều)
@app.get("/students")
# Sửa 2: Đổi tên hàm thành get_students cho đúng ngữ nghĩa
def get_students():
    # Sửa 3: Trả về toàn bộ danh sách (mảng) thay vì chỉ phần tử students[0]
    return students
