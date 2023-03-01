from PyQt5.QtWidgets import *
from vucut_kitle_Qt import Ui_MainWindow

class vucut_kitle_hesaplama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vucut_kitle=Ui_MainWindow()
        self.vucut_kitle.setupUi(self)

        self.vucut_kitle.pushButton_temizle.clicked.connect(self.temizle)
        self.vucut_kitle.pushButton_hesapla.clicked.connect(self.hesapla)
        self.show()
    
    def temizle(self):
        self.vucut_kitle.lineEdit_boy.clear()
        self.vucut_kitle.lineEdit_kilo.clear()

        self.vucut_kitle.label_bilgilendirme.setText("Bilgilendirme...")
    def hesapla(self):
        if self.vucut_kitle.lineEdit_boy.text()=="" or self.vucut_kitle.lineEdit_kilo.text()=="":
            self.vucut_kitle.label_bilgilendirme.setText("Lütfen kilonuzu ve boyunuzu giriniz")
        else:

            kilo=float(self.vucut_kitle.lineEdit_kilo.text())
            boy=self.vucut_kitle.lineEdit_boy.text()
            boy=boy[:1]+"."+boy[1:]
            boy=float(boy)

            sonuc=kilo/(boy**2)
            sonuc=round(sonuc,3)

            if sonuc<=18.5:
                bilgilendirme="     V.K.İ. == {}\n\nSağlığınız için kilo almalısınız...".format(sonuc)
                self.vucut_kitle.label_bilgilendirme.setText(bilgilendirme)
            elif 24.9>sonuc>18.5:
                bilgilendirme="     V.K.İ. == {}\n\nSağlığınız için kilonuzu sabşt tutmalısınız...".format(sonuc)
                self.vucut_kitle.label_bilgilendirme.setText(bilgilendirme)
            elif 29.9>sonuc>=25:
                bilgilendirme="     V.K.İ. == {}\n\nSağlığınız için kilo vermelisiniz...".format(sonuc)
                self.vucut_kitle.label_bilgilendirme.setText(bilgilendirme)
            else:
                bilgilendirme="     V.K.İ. == {}\n\nSağlığınız için ACİL kilo vermelisiniz...".format(sonuc)
                self.vucut_kitle.label_bilgilendirme.setText(bilgilendirme)