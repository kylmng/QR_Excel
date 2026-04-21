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

```
web-1  |  * Running on http://0.0.0.0:5000
```

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
```

---

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
