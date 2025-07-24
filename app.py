from flask import Flask, request, jsonify, render_template
from keras.models import load_model, Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, TimeDistributed, Input
import numpy as np
import pickle
import re

app = Flask(__name__)

# ==== Load mô hình đã huấn luyện ====
enc_model = load_model('model/enc_model.h5')
dec_model = load_model('model/dec_model.h5')

# ==== Load vocab và inv_vocab ====
with open('model/vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)

with open('model/inv_vocab.pkl', 'rb') as f:
    inv_vocab = pickle.load(f)

# ==== Hàm làm sạch văn bản ====
def clean_text(txt):
    txt = txt.lower()
    txt = re.sub(r"i'm", "i am", txt)
    txt = re.sub(r"he's", "he is", txt)
    txt = re.sub(r"she's", "she is", txt)
    txt = re.sub(r"that's", "that is", txt)
    txt = re.sub(r"what's", "what is", txt)
    txt = re.sub(r"where's", "where is", txt)
    txt = re.sub(r"\'ll", " will", txt)
    txt = re.sub(r"\'ve", " have", txt)
    txt = re.sub(r"\'re", " are", txt)
    txt = re.sub(r"\'d", " would", txt)
    txt = re.sub(r"won't", "will not", txt)
    txt = re.sub(r"can't", "can not", txt)
    txt = re.sub(r"[^\w\s]", "", txt)
    return txt

# ==== Giả lập dense layer như trong demo nếu có ====
# Giả sử vocab có kích thước V
V = len(vocab)
dense = TimeDistributed(Dense(V, activation='softmax'))

# ==== Trang chính ====
@app.route('/')
def home():
    return render_template('index.html')

# ==== API xử lý chat ====
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    message = clean_text(message)

    # Tiền xử lý câu đầu vào
    tokens = [vocab.get(w, vocab['<OUT>']) for w in message.split()]
    tokens = pad_sequences([tokens], maxlen=13, padding='post')

    # Lấy trạng thái từ encoder
    states = enc_model.predict(tokens, verbose=0)

    # Khởi tạo input đầu tiên cho decoder là <SOS>
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = vocab['<SOS>']

    stop_condition = False
    decoded_sentence = ''

    while not stop_condition:
        # Dự đoán bước kế tiếp
        output_tokens, h, c = dec_model.predict([target_seq] + states, verbose=0)

        # Nếu cần dense layer giống demo
        decoder_output = dense(output_tokens)
        sampled_token_index = np.argmax(decoder_output[0, -1, :])

        # Lấy từ tương ứng
        sampled_word = inv_vocab.get(sampled_token_index, '<UNK>')

        # Kiểm tra điều kiện dừng
        if sampled_word == '<EOS>' or len(decoded_sentence.split()) > 13:
            stop_condition = True
        elif sampled_word not in ['<SOS>', '<OUT>', '<UNK>']:
            decoded_sentence += ' ' + sampled_word

        # Chuẩn bị input cho bước kế tiếp
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index
        states = [h, c]

    return jsonify({'response': decoded_sentence.strip()})

# ==== Chạy Flask app ====
if __name__ == '__main__':
    app.run(debug=True)

