from flask import Flask, render_template, request
app = Flask(__name__)
import pickle

model = pickle.load(open("model/campus_tree.pkl", 'rb'))

@app.route('/')
def campus():
    return render_template("main.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    fitur = []
    for val in request.form.values():
        fitur.append(int(val)) #[100, 0]

    nilai_sma = "Nilai SMA: " + str(fitur[0])
    jurusan = "Jurusan: " + ["Arts", "Commerce", "Science"][fitur[1]]

    # reshape fitur jadi bentuk 2D, 1 kolom
    fitur = [fitur] #[[100, 0]]

    # bikin prediksi, kita load model kita
    hasil = model.predict(fitur)

    index = hasil[0]
    prediksi = "hasil prediksi: " + ["Tidak Diterima", "Diterima Kerja"][index]

    # return nilai_sma + " " + jurusan + " " + prediksi
    return render_template("main.html", nilai_sma=nilai_sma, jurusan=jurusan, prediksi=prediksi)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'