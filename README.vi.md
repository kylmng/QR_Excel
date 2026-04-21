# QR Excel - Ứng Dụng Quét Mã QR và Xuất Dữ Liệu vào Excel

## Mô Tả
Ứng dụng di động Android cho phép:
- Quét mã QR
- Gửi dữ liệu dạng văn bản đến máy chủ
- Lưu dữ liệu vào tệp Excel trên máy chủ
- Chọn tệp Excel khác nhau để lưu dữ liệu

## Kiến Trúc
- **Frontend**: Ứng dụng Android (Java)
- **Backend**: Flask (Python) + openpyxl
- **Database**: Tệp Excel (.xlsx)
- **Deployment**: Docker Compose + Microsoft Azure

## Yêu Cầu
- Docker & Docker Compose
- Python 3.11+
- Android Studio (cho phát triển ứng dụng di động)

## Cài Đặt

### 1. Khởi động máy chủ backend

```bash
cd /Users/kylmng/Documents/Coding\ Projects/QR_Excel
docker-compose up --build
```

Máy chủ sẽ chạy tại `http://localhost:5001`

### 2. Cài đặt các gói Python (nếu không dùng Docker)

```bash
pip install -r requirements.txt
python app.py
```

## API Endpoints

### POST /login
Đăng nhập và nhận token JWT
```bash
curl -X POST http://localhost:5001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'
```

### GET /files
Lấy danh sách tệp Excel
```bash
curl http://localhost:5001/files
```

### POST /append
Thêm dữ liệu mã QR vào tệp Excel
```bash
curl -X POST http://localhost:5001/append \
  -H "Content-Type: application/json" \
  -d '{"filename":"test.xlsx","qr_data":"dữ liệu từ mã QR"}'
```

## Cấu Trúc Thư Mục

```
QR_Excel/
├── app.py                 # Ứng dụng Flask chính
├── requirements.txt       # Các phụ thuộc Python
├── Dockerfile            # Dockerfile
├── docker-compose.yml    # Docker Compose config
├── .dockerignore          # Các tệp bỏ qua trong Docker
├── uploads/              # Thư mục lưu tệp Excel
└── README.vi.md          # Tài liệu này
```

## Các Tính Năng

✅ Quét mã QR trên thiết bị Android
✅ Xác thực người dùng (JWT)
✅ Lưu dữ liệu vào Excel
✅ Chọn tệp Excel
✅ API RESTful

## Phát Triển Tiếp Theo

- [ ] Xây dựng ứng dụng Android
- [ ] Thêm xác thực JWT đầy đủ
- [ ] Triển khai trên Azure
- [ ] Hỗ trợ nhiều sheet trong Excel
- [ ] Thêm giao diện web

## Lỗi Thường Gặp

### "file is not a zip file"
Tệp Excel không hợp lệ. Tạo tệp mới:
```python
from openpyxl import Workbook
wb = Workbook()
wb.save("uploads/test.xlsx")
```

### Dữ liệu bị thêm hai lần
Kiểm tra lệnh curl có URL trùng lặp ở cuối hay không.

## Giấy Phép
MIT

## Liên Hệ
Dự án QR to Excel - 2026
```

**SETUP.vi.md** (Hướng Dẫn Cài Đặt Chi Tiết):
```markdown
# Hướng Dẫn Cài Đặt Chi Tiết

## Bước 1: Chuẩn Bị Môi Trường

### Yêu Cầu Hệ Thống
- macOS hoặc Linux (hoặc Windows với WSL2)
- Docker Desktop cài đặt
- Terminal/Shell

### Kiểm Tra Docker
```bash
docker --version
docker-compose --version
```

## Bước 2: Tải Xuống Dự Án

```bash
cd ~/Documents/Coding\ Projects/QR_Excel
ls -la
```

## Bước 3: Tạo Tệp Cấu Hình

Tạo .env.local:
```
JWT_SECRET_KEY=your-secret-key-here
```

## Bước 4: Tạo Thư Mục uploads

```bash
mkdir -p uploads
```

## Bước 5: Tạo Tệp Excel Mẫu

Tạo tệp `create_test_excel.py`:
```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = 'QR Data'
ws['B1'] = 'Timestamp'
wb.save('uploads/test.xlsx')
print("Tệp test.xlsx đã được tạo!")
```

Chạy:
```bash
python create_sample.py
```

## Bước 6: Khởi Động Ứng Dụng

```bash
docker-compose up --build
```

Chờ cho đến khi thấy:
```
web-1  |  * Running on http://0.0.0.0:5000
```

## Bước 7: Kiểm Tra API

Mở terminal mới và chạy:
```bash
curl -X POST http://localhost:5001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'
```

Bạn sẽ nhận được token JWT.

## Bước 8: Dừng Ứng Dụng

```bash
docker-compose down
```

## Mẹo

- Để xem logs: `docker-compose logs -f`
- Để rebuild: `docker-compose up --build`
- Để xóa container: `docker-compose down -v`
```

**API.vi.md** (Tài Liệu API):
```markdown
# Tài Liệu API

## Authentication (Xác Thực)

### POST /login
**Mô Tả**: Đăng nhập và nhận token JWT

**Request**:
```json
{
  "username": "admin",
  "password": "password"
}
```

**Response** (200):
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response** (401):
```json
{
  "error": "Invalid credentials"
}
```

---

## Excel Management (Quản Lý Excel)

### GET /files
**Mô Tả**: Lấy danh sách tất cả tệp Excel

**Header**:
```
Authorization: Bearer <token>
```

**Response** (200):
```json
{
  "files": ["test.xlsx", "data.xlsx"]
}
```

---

### POST /append
**Mô Tả**: Thêm dữ liệu vào tệp Excel

**Header**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request**:
```json
{
  "filename": "test.xlsx",
  "qr_data": "dữ liệu từ mã QR"
}
```

**Response** (200):
```json
{
  "message": "Data appended successfully"
}
```

**Response** (400):
```json
{
  "error": "Filename and qr_data required"
}
```

**Response** (404):
```json
{
  "error": "File not found"
}
```

---

## Ví Dụ Sử Dụng

### 1. Đăng Nhập
```bash
TOKEN=$(curl -s -X POST http://localhost:5001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}' \
  | jq -r '.access_token')

echo $TOKEN
```

### 2. Lấy Danh Sách Tệp
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5001/files
```

### 3. Thêm Dữ Liệu
```bash
curl -X POST http://localhost:5001/append \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"filename":"test.xlsx","qr_data":"ABC123"}'
```

---

## Lỗi Phổ Biến

| Lỗi | Nguyên Nhân | Giải Pháp |
|-----|-----------|----------|
| "Invalid credentials" | Sai tên đăng nhập hoặc mật khẩu | Sử dụng admin/password |
| "File not found" | Tệp Excel không tồn tại | Tạo tệp trong thư mục uploads |
| "Filename and qr_data required" | Thiếu trường trong request | Thêm cả filename và qr_data |
| "Connection refused" | Máy chủ không chạy | Chạy `docker-compose up` |
```