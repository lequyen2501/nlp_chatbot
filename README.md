# 🧠 Simple Chatbot with Flask & Seq2Seq

Một chatbot đơn giản sử dụng mô hình Encoder-Decoder (Seq2Seq) huấn luyện từ tập dữ liệu hội thoại phim (Cornell Movie Dialogs Corpus). Triển khai bằng Flask để người dùng có thể tương tác trực tiếp.

---

## 📁 Cấu trúc thư mục

```
project/
├── app.py                   # Ứng dụng Flask
├── model/
│   ├── enc_model.h5         # Encoder LSTM
│   ├── dec_model.h5         # Decoder LSTM
│   ├── vocab.pkl            # Từ điển từ → index
│   └── inv_vocab.pkl        # Từ điển index → từ
├── templates/
│   └── index.html           # Giao diện chatbot
└── requirements.txt         # Danh sách thư viện
```

---

## 🚀 Cách chạy chatbot demo

Chạy các lệnh sau trong terminal:

```
pip install -r requirements.txt
python app.py
```

Sau đó mở trình duyệt và truy cập: [http://127.0.0.1:5000](http://127.0.0.1:5000)

> ✅ Đảm bảo các file `.h5`, `.pkl` nằm trong thư mục `model/` như cấu trúc ở trên.

---

## 📦 Thư viện cần thiết

Trong `requirements.txt`:

```
flask
tensorflow
keras
numpy
```

---

## 📚 Nguồn dữ liệu

* Cornell Movie Dialogs Corpus (tải từ Kaggle):
  🔗 [https://www.kaggle.com/datasets/Cornell-University/movie-dialog-corpus]

---

## 📄 Ghi chú

* Repo **không chứa sẵn mô hình**. Bạn cần tự huấn luyện hoặc sử dụng file `.h5`, `.pkl` từ nguồn khác.
* Nếu muốn huấn luyện lại từ đầu, xem hướng dẫn chi tiết trong file `README_train.md`.
