# README - Demo Chatbot Flask (Seq2Seq)

Đây là hướng dẫn sử dụng Flask để chạy thử chatbot đã được huấn luyện bằng mô hình Encoder-Decoder (LSTM).

---

## 1. Cấu trúc thư mục dự án

```
project/
├── app.py
├── model/
│   ├── enc_model.h5
│   ├── dec_model.h5
│   ├── vocab.pkl
│   └── inv_vocab.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 2. Cài đặt môi trường

Tạo môi trường ảo và cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

---

## 3. Chạy Flask App

Chạy ứng dụng Flask:

```bash
python app.py
```

Ứng dụng sẽ chạy ở địa chỉ mặc định:

```
http://127.0.0.1:5000/
```

Bạn có thể trò chuyện với chatbot qua giao diện web.

---

## 4. Lưu ý

* Thư mục `model/` phải chứa đầy đủ 4 file: `enc_model.h5`, `dec_model.h5`, `vocab.pkl`, `inv_vocab.pkl`
* Nếu bạn chưa có các file này, hãy xem file `README_train.md` để huấn luyện lại mô hình.
* Flask chỉ chạy local, không deploy công khai (trừ khi cấu hình thêm).

---

## 5. Tham khảo

* Mô hình: Encoder-Decoder (LSTM)
* Dữ liệu huấn luyện: Cornell Movie Dialogs Corpus
