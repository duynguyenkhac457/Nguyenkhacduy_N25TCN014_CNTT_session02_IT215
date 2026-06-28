# =================================================================
# HỌ VÀ TÊN: Bùi Minh Hiếu
# MÃ SINH VIÊN: n25dtcn020
# BÀI TẬP: Xây dựng API lấy danh sách sách sắp hết hàng
# =================================================================

from fastapi import FastAPI

app = FastAPI()

# Cấu trúc dữ liệu mock data, bao gồm cả các bẫy dữ liệu
books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20},
    {"id": 6, "title": "Java Basic"},  # Bẫy 1: Thiếu trường quantity
    {"id": 7, "title": "Spring Boot", "quantity": -2} # Bẫy 2: Quantity âm
]

@app.get("/books/low-stock")
def get_low_stock_books():
    low_stock_books = []
    
    for book in books:
        # Xử lý bẫy 1: Bỏ qua nếu không có trường quantity
        if "quantity" not in book:
            continue
            
        qty = book["quantity"]
        
        # Xử lý bẫy 2: Bỏ qua nếu dữ liệu không hợp lệ (số lượng âm)
        if qty < 0:
            continue
            
        # Xử lý nghiệp vụ chính: Kiểm tra sách sắp hết hàng
        if qty <= 5:
            low_stock_books.append(book)
            
    # Kiểm tra và trả về response tương ứng
    if len(low_stock_books) == 0:
        return {
            "message": "Không có sách nào sắp hết hàng",
            "data": []
        }
        
    return {
        "message": "Danh sách sách sắp hết hàng",
        "data": low_stock_books
    }
