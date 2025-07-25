#  Hướng dẫn Huấn luyện Chatbot (Seq2Seq)

File này hướng dẫn cách huấn luyện lại mô hình chatbot sử dụng kiến trúc Encoder-Decoder (LSTM) từ đầu bằng tập dữ liệu Cornell Movie Dialogs Corpus.

---

## 1. Tải dữ liệu

* Tải Cornell Movie Dialogs Corpus từ Kaggle:
  🔗 [https://www.kaggle.com/datasets/Cornell-University/movie-dialog-corpus](https://www.kaggle.com/datasets/Cornell-University/movie-dialog-corpus)

* Giải nén file và đặt vào thư mục `data/`:

```
project/
├── data/
│   └── cornell movie-dialogs corpus/
```

Dữ liệu sẽ bao gồm các file như:

```
movie_lines.txt
movie_conversations.txt
```

---

## 2. Cài đặt thư viện

Chạy lệnh sau:

```
pip install -r requirements.txt
```

---

## 3. Chạy file huấn luyện

Giả sử file huấn luyện là `train.py`, bạn chạy lệnh:

```
python train.py
```

Sau khi huấn luyện xong, bạn sẽ thu được các file sau trong thư mục `model/`:

```
model/
├── enc_model.h5
├── dec_model.h5
├── vocab.pkl
└── inv_vocab.pkl
```

---
---

Sau khi huấn luyện, quay lại `README.md` để chạy demo với Flask.
