# =================================================================
# HỌ VÀ TÊN: Bùi Minh Hiếu
# MÃ SINH VIÊN: n25dtcn020
# BÀI TẬP: [Vận dụng cơ bản 1] Sai sót trong API lấy danh sách sinh viên
# =================================================================

from fastapi import FastAPI
from typing import List

# Khởi tạo ứng dụng FastAPI với cấu hình thông tin cơ bản
app = FastAPI(
    title="Hệ thống Quản lý Sinh viên",
    description="API phục vụ việc lấy thông tin và quản lý danh sách sinh viên trong lớp.",
    version="1.0.0"
)

# Cơ sở dữ liệu giả lập (Mock Data) dạng danh sách chuỗi
students_db: List[str] = ["An", "Bình", "Cường"]


# Định nghĩa Endpoint lấy danh sách sinh viên theo chuẩn RESTful API:
# 1. Sử dụng phương thức HTTP GET để lấy dữ liệu.
# 2. Sử dụng danh từ số nhiều `/students` thay vì chứa động từ như `/getStudents`.
# 3. Sử dụng `response_model` để chỉ định kiểu dữ liệu trả về chuẩn hóa.
@app.get(
    "/students", 
    response_model=List[str],
    summary="Lấy toàn bộ danh sách sinh viên",
    description="API này trả về một mảng JSON (JSON Array) chứa danh sách tên của tất cả sinh viên hiện có."
)
def get_students() -> List[str]:
    """
    Xử lý luồng dữ liệu khi Frontend gửi yêu cầu đến endpoint /students.
    Trả về trực tiếp list dữ liệu, FastAPI sẽ tự động serialize sang định dạng JSON hợp lệ.
    """
    return students_db
