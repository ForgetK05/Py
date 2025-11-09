import google.generativeai as genai
import os

# --- CẤU HÌNH API KEY (Cách an toàn) ---
#
# 1. Mở terminal/PowerShell (nơi có .venv)
# 2. Chạy lệnh (chỉ cần chạy 1 lần cho mỗi phiên terminal):
#    (Trên PowerShell): $env:GOOGLE_API_KEY="DÁN_KEY_MỚI_VÀ_BÍ_MẬT_CỦA_BẠN_VÀO_ĐÂY"
#    (Trên CMD):       set GOOGLE_API_KEY=DÁN_KEY_MỚI_VÀ_BÍ_MẬT_CỦA_BẠN_VÀO_ĐÂY
#
# ----------------------------------------
api_key = "KEY_CỦA_BẠN_ĐÂY"  # Thay thế tạm thời để tránh lỗi trong IDE

if not api_key:
    print("LỖI: Không tìm thấy biến môi trường 'GOOGLE_API_KEY'.")
    print("Vui lòng chạy lệnh '$env:GOOGLE_API_KEY=...' trong terminal trước.")
    exit()  # Thoát nếu không có key

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Lỗi cấu hình API Key: {e}")
    exit()

# --- KHỞI TẠO MODEL ---
try:
    # Chúng ta đã xác nhận 'gemini-pro' hoạt động tốt
    model = genai.GenerativeModel("gemini-2.5-flash")
    print(">>> Gia sư AI đã sẵn sàng! (gõ 'exit' hoặc 'quit' để thoát).")

except Exception as e:
    print(f"Lỗi khi tải model: {e}")
    exit()


# --- HÀM CHAT ---
def chat_with_ai(prompt: str):
    """Gửi prompt đến AI và trả về phản hồi."""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"\n[Lỗi API khi đang chat]: {e}\n")
        return "Xin lỗi, tôi gặp sự cố khi đang xử lý..."


# --- VÒNG LẶP CHAT CHÍNH ---
if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("AI: Tạm biệt! Hẹn gặp lại.")
            break

        ai_response = chat_with_ai(user_input)
        print(f"AI: {ai_response}")