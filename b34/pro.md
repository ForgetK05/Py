### Đề bài: Xây dựng ứng dụng quản lý thư viện sách đơn giản với SQLModel

**Mô tả bài tập:**  
Sử dụng thư viện SQLModel (dựa trên SQLAlchemy và Pydantic) để xây dựng một ứng dụng quản lý cơ bản cho thư viện sách. Ứng dụng cần lưu trữ thông tin về sách và tác giả, đồng thời hỗ trợ các thao tác CRUD (Create, Read, Update, Delete) đơn giản. Database sử dụng SQLite với file `library.db`.

**Yêu cầu chi tiết:**

1. **Định nghĩa các mô hình (Models):**  
   - Tạo mô hình `Author` với các trường:  
     - `id`: Integer, primary key, tự động tăng.  
     - `name`: String, không null, độ dài tối đa 100 ký tự.  
     - `birth_year`: Optional Integer (năm sinh, có thể null).  
   - Tạo mô hình `Book` với các trường:  
     - `id`: Integer, primary key, tự động tăng.  
     - `title`: String, không null, độ dài tối đa 200 ký tự.  
     - `isbn`: String, unique, độ dài chính xác 13 ký tự (sử dụng validator để kiểm tra).  
     - `publish_year`: Integer, không null.  
     - `author_id`: Integer, foreign key tham chiếu đến `Author.id`.  
   - Thiết lập mối quan hệ: Một `Author` có thể có nhiều `Book` (one-to-many). Sử dụng `relationship` để truy vấn ngược (ví dụ: từ Book lấy Author).

2. **Thiết lập kết nối database:**  
   - Tạo SQLAlchemy engine kết nối với SQLite file `library.db`.  
   - Sử dụng `create_all()` để tạo các bảng trong database.

3. **Thao tác dữ liệu (CRUD):**  
   - **Create:** Viết hàm `add_author_and_books()` để thêm ít nhất 2 tác giả và 4 sách tương ứng (mỗi tác giả có ít nhất 2 sách). Dữ liệu mẫu:  
     - Tác giả 1: Name="Nguyễn Nhật Ánh", Birth_year=1954.  
     - Sách 1: Title="Cho tôi xin một vé đi tuổi thơ", ISBN="9786041134567", Publish_year=2015, Author_id=1.  
     - (Thêm các dữ liệu khác tương tự).  
   - **Read:** Viết hàm `get_books_by_author(author_name: str)` để truy vấn và trả về danh sách tất cả sách của một tác giả cụ thể (sử dụng join hoặc relationship).  
   - **Update:** Viết hàm `update_book_isbn(book_title: str, new_isbn: str)` để cập nhật ISBN của một sách dựa trên title.  
   - **Delete:** Viết hàm `delete_old_books(year: int)` để xóa tất cả sách xuất bản trước năm `year` (ví dụ: trước 2000).

4. **Xử lý lỗi và validation:**  
   - Sử dụng Pydantic validators để đảm bảo ISBN đúng định dạng (13 chữ số, chỉ số và dấu gạch ngang).  
   - Xử lý trường hợp không tìm thấy dữ liệu (ví dụ: raise exception nếu tác giả không tồn tại).

5. **Chạy và kiểm tra:**  
   - Trong hàm `main()`, gọi các hàm trên để thực hiện: Thêm dữ liệu → Truy vấn sách của một tác giả → Cập nhật một sách → Xóa sách cũ → In kết quả truy vấn cuối cùng ra màn hình (danh sách sách còn lại).

**Hướng dẫn nộp bài:**  
- Viết code hoàn chỉnh trong một file Python (ví dụ: `library_app.py`).  
- Không sử dụng thêm thư viện ngoài SQLModel, SQLAlchemy, và Pydantic (đã được import từ SQLModel).  
- Chạy code và kiểm tra database được tạo đúng (có thể dùng công cụ như DB Browser for SQLite để xem).  
- Bài làm cần sạch sẽ, có comment giải thích các phần chính.

**Thời gian gợi ý:** 2-3 giờ.  
**Điểm số:** 10 điểm (2 điểm/model, 2 điểm/CRUD, 2 điểm/validation, 2 điểm/main, 2 điểm/chạy đúng).  
