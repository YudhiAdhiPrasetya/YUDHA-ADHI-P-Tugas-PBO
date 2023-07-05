from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QVBoxLayout, QCheckBox
from PyQt5.QtGui import QFont, QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Mengatur judul window
        self.setWindowTitle('PEMBELIAN PULSA')

        # Membuat QLine Edit berupa nomor telepon dan nominal harga pulsa
        self.nomor_telepon = QLineEdit()
        self.nominal_harga = QLineEdit()

        # Membuat Qlabel untuk menampilkan input dan hasilnya
        self.label1 = QLabel("PEMBELIAN PULSA")
        self.label2 = QLabel("Masukkan Nomor Telepon")
        self.label3 = QLabel("Masukkan Nominal Pulsa")
        self.label4 = QLabel("Pilih Jenis Nomor Operator")
        self.harga_label = QLabel("Harga Yang Harus Dibayarkan ")
        self.hasil_label = QLabel()
        self.label5 = QLabel("Pilih Metode Pembayaran")
        self.harga2_label2 = QLabel()
        self.hasil2_label2 = QLabel()

        # Mengatur gaya dan warna teks pada label
        self.label1.setFont(QFont('Arial', 16))
        self.label1.setStyleSheet("color: blue")
        self.label2.setStyleSheet("color: #000000")
        self.label3.setStyleSheet("color: #000000")
        self.label4.setStyleSheet("color: #000000")
        self.harga_label.setStyleSheet("color: #000000")
        self.label5.setStyleSheet("color: #000000")
        self.harga2_label2.setStyleSheet("color: #000000")

        # Mengatur warna latar belakang pada label
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("#F5F5F5"))
        self.label1.setAutoFillBackground(True)
        self.label1.setPalette(palette)

        # Membuat perhitungan QpushButton widget pertama
        self.telkomsel_button = QPushButton('TELKOMSEL')
        self.smartfren_button = QPushButton('SMARTFREN')
        self.indosat_button = QPushButton('INDOSAT')
        self.xl_button = QPushButton('XL')

        # Mengatur warna latar belakang pada tombol
        self.telkomsel_button.setStyleSheet("background-color: #1E90FF")
        self.smartfren_button.setStyleSheet("background-color: #1E90FF")
        self.indosat_button.setStyleSheet("background-color: #1E90FF")
        self.xl_button.setStyleSheet("background-color: #1E90FF")

        # Membuat QpushButton widget kedua
        self.bri_checkBox = QCheckBox('BRI MOBILE')
        self.bni_checkBox = QCheckBox('BNI MOBILE BANKING')
        self.ovo_checkBox = QCheckBox('OVO')
        self.dana_checkBox = QCheckBox('DANA')
        self.alfamart_checkBox = QCheckBox('ALFAMART')
        self.indomaret_checkBox = QCheckBox('INDOMARET')

        # Mengatur gaya teks pada checkbox
        self.bri_checkBox.setStyleSheet("color: #000000")
        self.bni_checkBox.setStyleSheet("color: #000000")
        self.ovo_checkBox.setStyleSheet("color: #000000")
        self.dana_checkBox.setStyleSheet("color: #000000")
        self.alfamart_checkBox.setStyleSheet("color: #000000")
        self.indomaret_checkBox.setStyleSheet("color: #000000")

        # Connect signal button jenis nomor operator
        self.telkomsel_button.clicked.connect(self.telkomsel_operator)
        self.smartfren_button.clicked.connect(self.smartfren_operator)
        self.indosat_button.clicked.connect(self.indosat_operator)
        self.xl_button.clicked.connect(self.xl_operator)

        # Connect signal metode pembayaran
        

        # Membuat add QVBoxLayout dan add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.nomor_telepon)
        layout.addWidget(self.label3)
        layout.addWidget(self.nominal_harga)
        layout.addWidget(self.label4)
        layout.addWidget(self.telkomsel_button)
        layout.addWidget(self.smartfren_button)
        layout.addWidget(self.indosat_button)
        layout.addWidget(self.xl_button)
        layout.addWidget(self.harga_label)
        layout.addWidget(self.hasil_label)
        layout.addWidget(self.label5)
        layout.addWidget(self.bri_checkBox)
        layout.addWidget(self.bni_checkBox)
        layout.addWidget(self.ovo_checkBox)
        layout.addWidget(self.dana_checkBox)
        layout.addWidget(self.alfamart_checkBox)
        layout.addWidget(self.indomaret_checkBox)
        self.konfirmasi_button = QPushButton('Konfirmasi')
        self.konfirmasi_button.clicked.connect(self.tampilkan_hasil)
        layout.addWidget(self.konfirmasi_button)
        layout.addWidget(self.harga2_label2)
        layout.addWidget(self.hasil2_label2)

        # Membuat widget dan mengatur layout pada program
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Membuat perhitungan harga setiap jenis nomor operator
    # Menentukan harga jenis nomor operator TELKOMSEL
    def telkomsel_operator(self):
        hasil = float(self.nominal_harga.text()) + 4000
        self.hasil_label.setText(str(hasil))

    # Menentukan harga jenis nomor operator SMARTFREN
    def smartfren_operator(self):
        hasil = float(self.nominal_harga.text()) + 3500
        self.hasil_label.setText(str(hasil))

    # Menentukan harga jenis nomor operator INDOSAT
    def indosat_operator(self):
        hasil = float(self.nominal_harga.text()) + 3000
        self.hasil_label.setText(str(hasil))

    # Menentukan harga jenis nomor operator XL
    def xl_operator(self):
        hasil = float(self.nominal_harga.text()) + 2000
        self.hasil_label.setText(str(hasil))

    # Membuat Metode Pembayaran
    # Membuat metode pembayaran dengan BRI MOBILE
    
    def tampilkan_hasil(self):
        nomor_telepon = self.nomor_telepon.text()
        nominal_harga = self.nominal_harga.text()
        operator = ''
        if self.telkomsel_button.isChecked():
            operator = "TELKOMSEL"
        elif self.smartfren_button.isChecked():
            operator = "SMARTFREN"
        elif self.indosat_button.isChecked():
            operator = "INDOSAT"
        elif self.xl_button.isChecked():
            operator = "XL"
        metode_pembayaran = []
        if self.bri_checkBox.isChecked():
            metode_pembayaran.append("BRI MOBILE")
        if self.bni_checkBox.isChecked():
            metode_pembayaran.append("BNI MOBILE BANKING")
        if self.ovo_checkBox.isChecked():
            metode_pembayaran.append("OVO")
        if self.dana_checkBox.isChecked():
            metode_pembayaran.append("DANA")
        if self.alfamart_checkBox.isChecked():
            metode_pembayaran.append("ALFAMART")
        if self.indomaret_checkBox.isChecked():
            metode_pembayaran.append("INDOMARET")
        
        konfirmasi_data = f"Data yang Anda masukkan:\n\nNomor Telepon: {nomor_telepon}\nNominal Harga Pulsa: {nominal_harga}\nMetode Pembayaran: {', '.join(metode_pembayaran)}"
        hasil_pembayaran = float(self.hasil_label.text())
        hasil2 = f"Selamat! Pulsa Anda telah terkirim dan telah melakukan pembayaran sebesar {hasil_pembayaran} melalui {', '.join(metode_pembayaran)}"
    
        # Menampilkan hasil pada tab selanjutnya (membuat window baru)
        self.new_window = QMainWindow()
        self.new_window.setWindowTitle('Hasil Pembelian Pulsa')
    
        layout = QVBoxLayout()
        layout.addWidget(QLabel(konfirmasi_data))
        layout.addWidget(QLabel(hasil2))
    
        container = QWidget()
        container.setLayout(layout)
        self.new_window.setCentralWidget(container)
        self.new_window.show()


# Menampilkan hasil
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()