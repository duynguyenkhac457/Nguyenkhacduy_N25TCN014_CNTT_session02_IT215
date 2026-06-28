# =================================================================
# HỌ VÀ TÊN: Bùi Minh Hiếu
# MÃ SINH VIÊN: n25dtcn020
# BÀI TẬP: [Vận dụng chuyên sâu] Xây dựng API lấy danh sách sinh viên đang học
# =================================================================

from fastapi import FastAPI

app = FastAPI()

# Dữ liệu danh sách sinh viên ban đầu
students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Bình", "status": "inactive"},
    {"id": 3, "name": "Cường", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"},
]

@app.get("/students/active")
def get_active_students():
    # Bước 1 & 2: Lọc danh sách sinh viên đang học (status == "active")
    active_students = []
    for student in students:
        if student.get("status") == "active":
            active_students.append(student)
            
    # Mẹo: Có thể viết gọn lại bằng List Comprehension như sau:
    # active_students = [student for student in students if student.get("status") == "active"]

    # Bước 3 & 4: Kiểm tra và trả về kết quả theo đúng định dạng
    if len(active_students) > 0:
        return {
            "message": "Danh sách sinh viên đang học",
            "data": active_students
        }
    else:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
