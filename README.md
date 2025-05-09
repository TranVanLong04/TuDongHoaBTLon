# Tra Cứu Vi Phạm Giao Thông Tự Động
Sử dụng Selenium để tự động hóa việc kiểm tra vi phạm ở web https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.htm
I. Cấu Hình
- Trình biên dịch Python(PyCharm, VsCode, ...)
- Trình duyệt Chrome
- Đường dẫn Tesseract-OCR: C:\Program Files\Tesseract-OCR\tesseract.exe (Thay dổi theo vị trí lưu của người )
- Đường dẫn lưu captcha:  D:\TDHQT\BaiTap\BaiTapLon\captcha.png (Thay dổi theo vị trí lưu của người )

II. Cài đặt phụ thuộc
Chạy lệnh sau trong terminal (Command Prompt / PowerShell) để cài đặt:
- pip install selenium opencv-python pytesseract
- Hoặc tải trực tiếp tại: https://github.com/tesseract-ocr/tesseract

III. Chạy thủ công
Bước 1: Mở terminal tại thư mục chứa dự án
Bước 2: Chạy lệnh python TraCuuViPham.py để thực thi
