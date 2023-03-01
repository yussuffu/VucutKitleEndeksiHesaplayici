from PyQt5.QtWidgets import QApplication
from vucut_kitle_python import vucut_kitle_hesaplama


app=QApplication([])
pencere=vucut_kitle_hesaplama()
pencere.show()
app.exec_()

