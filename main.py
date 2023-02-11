import sys
from PyQt5.QtWidgets import QApplication
from clases_ventana import VentanaRandom

app = QApplication(sys.argv)

# ----- odio los comentarios :,v
ventanaRandom = VentanaRandom()
ventanaRandom.show()


sys.exit(app.exec_())