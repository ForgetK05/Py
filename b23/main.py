import cv2
import sys

# Đường dẫn đến tệp Haar Cascade.
# Đảm bảo tệp này nằm cùng thư mục với script hoặc sử dụng đường dẫn tuyệt đối.
CASCADE_PATH = 'haarcascade_frontalface_default.xml'

# Khởi tạo bộ phân loại (classifier)
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

if face_cascade.empty():
    print(f"Lỗi: Không thể tải tệp Haar Cascade tại {CASCADE_PATH}")
    sys.exit(1)

# Mở camera (chỉ mục 0 thường là camera mặc định)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Lỗi: Không thể mở camera.")
    sys.exit(1)

print("Đang mở camera... Nhấn 'q' để thoát.")

while True:
    # 1. Đọc từng khung hình (frame) từ camera
    ret, frame = cap.read()

    if not ret:
        print("Không thể nhận được frame. Thoát...")
        break

    # 2. Chuyển đổi sang ảnh xám (grayscale) để tăng tốc độ xử lý
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3. Nhận diện khuôn mặt
    # detectMultiScale trả về một danh sách các hình chữ nhật (x, y, w, h)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # Tỷ lệ giảm kích thước ảnh ở mỗi lần quét
        minNeighbors=5,  # Số lượng lân cận cần thiết để chấp nhận nhận diện
        minSize=(30, 30),  # Kích thước đối tượng tối thiểu (30x30 pixels)
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 4. Vẽ hình chữ nhật xung quanh các khuôn mặt
    for (x, y, w, h) in faces:
        # (x, y) là góc trên bên trái, (w, h) là chiều rộng và chiều cao
        # (0, 255, 0) là màu xanh lá cây (BGR), 2 là độ dày đường viền
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Khuon Mat', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # 5. Hiển thị khung hình đã xử lý
    cv2.imshow('Face Detection (Nhan dien khuon mat)', frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dọn dẹp
cap.release()  # Giải phóng camera
cv2.destroyAllWindows()  # Đóng tất cả cửa sổ OpenCV