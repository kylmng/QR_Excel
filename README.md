<<<<<<< HEAD
# QR Excel - Ứng Dụng Quét Mã QR và Lưu vào Excel

Ứng dụng web giúp bạn quét mã QR và tự động lưu dữ liệu vào file Excel.

---

## Chọn Cách Cài Đặt

Có **2 cách** để chạy ứng dụng. Chọn cách phù hợp với bạn:

| | Cách 1: Docker | Cách 2: Python trực tiếp |
|---|---|---|
| Phù hợp | Muốn đơn giản, không lo cài Python | Đã có Python sẵn trên máy |
| Cần cài | Docker Desktop | Python 3.9+ |
| Độ phức tạp | Thấp | Trung bình |

---

## Bước Chung — Chuẩn Bị

### 1. Đặt thư mục ứng dụng

Nếu bạn nhận được thư mục `QR_Excel` từ ai đó, hãy đặt nó ở vị trí dễ tìm (ví dụ: Màn hình Desktop).

### 2. Mở Terminal (cửa sổ dòng lệnh)

**Trên Mac:**
1. Bấm tổ hợp phím `Command (⌘) + Space`
2. Gõ `Terminal` rồi bấm Enter

**Trên Windows:**
1. Bấm phím `Windows`
2. Gõ `PowerShell` rồi bấm Enter

### 3. Di chuyển vào thư mục ứng dụng

```
cd Desktop/QR_Excel
```

> Nếu thư mục không nằm trên Desktop, thay `Desktop/QR_Excel` bằng đường dẫn đúng.

---

## Cách 1: Dùng Docker (Khuyến Nghị)

### Bước 1 — Cài Docker Desktop

1. Truy cập: **https://www.docker.com/products/docker-desktop/**
2. Bấm **"Download Docker Desktop"**
3. Chọn phiên bản phù hợp:
   - **Mac (chip Apple M1/M2/M3)** → chọn "Apple Silicon"
   - **Mac (chip Intel)** → chọn "Intel Chip"
   - **Windows** → chọn "Windows"
4. Cài đặt như bình thường
5. Mở Docker Desktop, chờ biểu tượng **chuyển sang màu xanh**

### Bước 2 — Tạo file cấu hình

**Trên Mac:**
```
echo "JWT_SECRET_KEY=khoa-bi-mat-cua-toi" > .env.local
```

**Trên Windows (PowerShell):**
```
"JWT_SECRET_KEY=khoa-bi-mat-cua-toi" | Out-File -FilePath .env.local -Encoding utf8
```

### Bước 3 — Khởi động ứng dụng

```
docker-compose up --build
```

Lần đầu mất khoảng **3–5 phút**. Chờ cho đến khi thấy:

=======
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
>>>>>>> 202c9530b722c3cb8dab35f1b1899b694e83ab58
```
web-1  |  * Running on http://0.0.0.0:5000
```

<<<<<<< HEAD
### Bước 4 — Mở trình duyệt

Truy cập: **http://localhost:5001**

---

## Cách 2: Dùng Python Trực Tiếp (Không Cần Docker)

### Bước 1 — Kiểm tra Python đã cài chưa

```
python --version
```

Nếu thấy số phiên bản (ví dụ `Python 3.11.0`), bạn đã có Python. Nếu báo lỗi, tải Python tại **https://www.python.org/downloads/** rồi cài đặt.

### Bước 2 — Cài các thư viện cần thiết

```
pip install -r requirements.txt
```

### Bước 3 — Tạo thư mục lưu file Excel

**Trên Mac:**
```
mkdir -p uploads
```

**Trên Windows (PowerShell):**
```
New-Item -ItemType Directory -Force -Path uploads
```

### Bước 4 — Khởi động ứng dụng

```
python app.py
```

Khi thấy dòng sau, ứng dụng đã sẵn sàng:

```
 * Running on http://0.0.0.0:5000
```

### Bước 5 — Mở trình duyệt

Truy cập: **http://localhost:5000**

> Lưu ý: Khi dùng Python trực tiếp, địa chỉ là `localhost:5000` (không phải `5001`)

---

## Cách Sử Dụng

| Tính năng | Mô tả |
|-----------|-------|
| Quét mã QR | Dùng camera thiết bị để quét mã QR |
| Lưu vào Excel | Dữ liệu mã QR được tự động thêm vào file `.xlsx` |
| Chọn file | Có thể chọn file Excel khác nhau để lưu dữ liệu |

Tài khoản mặc định để đăng nhập:
- **Tên đăng nhập:** `admin`
- **Mật khẩu:** `password`

---

## Dừng Ứng Dụng

Quay lại Terminal và bấm `Ctrl + C`.

**Nếu dùng Docker**, dọn dẹp thêm bằng lệnh:
```
docker-compose down
```

---

## Khởi Động Lại Lần Sau

**Nếu dùng Docker** (không cần build lại):
```
docker-compose up
```

**Nếu dùng Python trực tiếp:**
```
python app.py
=======
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
>>>>>>> 202c9530b722c3cb8dab35f1b1899b694e83ab58
```

---

<<<<<<< HEAD
## Gặp Lỗi?

**Lỗi: "Cannot connect" hoặc trang web không mở được**
→ Nếu dùng Docker: kiểm tra Docker Desktop đang chạy (biểu tượng màu xanh)
→ Nếu dùng Python: đảm bảo Terminal vẫn đang chạy `python app.py`

**Lỗi: "port is already allocated" (Docker)**
→ Có ứng dụng khác đang dùng cổng 5001. Khởi động lại máy tính rồi thử lại.

**Lỗi: "Address already in use" (Python)**
→ Có ứng dụng khác đang dùng cổng 5000. Khởi động lại máy tính rồi thử lại.

**Lỗi: "file not found" khi lưu dữ liệu**
→ Cần tạo file Excel trước trong thư mục `uploads/`. Liên hệ người hỗ trợ kỹ thuật.

---

## Liên Hệ Hỗ Trợ

Nếu gặp vấn đề không giải quyết được, hãy chụp màn hình lỗi và liên hệ người phụ trách kỹ thuật.

---

*QR Excel — 2026*
=======
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
>>>>>>> 202c9530b722c3cb8dab35f1b1899b694e83ab58
