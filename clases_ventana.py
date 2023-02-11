from pygame import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from time import sleep
from PyQt5.QtCore import QEvent, QPoint, QEventLoop, QTimer
from random import randint
from mensajes import lista_mensajes
class VentanaRandom(QWidget):
    def __init__(self):
        super(VentanaRandom, self).__init__()
        self.empezar = 7
        self.contador = 0
        self.ancho = self.width()
        self.alto = self.height()
        loadUi("interfaces\\ventanaramdon17.ui",self)
        self.btnEmpezar.clicked.connect(self.IncrementarValor)
        self.btnEmpezar.installEventFilter(self)
    def IncrementarValor(self):
        if (self.contador >= 0 and self.contador <= 6) or (self.contador >= 21 and self.contador < 33):
            mensaje = lista_mensajes[self.contador]
            self.lblMensaje.setText(mensaje)
            self.contador =  self.contador + 1
        if self.contador == self.empezar:
            x = randint(0+100,self.ancho-100)
            y = randint(0+100,self.alto-100)
            newpoint = QPoint(x,y)
            self.btnEmpezar.move(newpoint)
            mensaje = lista_mensajes[self.contador]
            self.lblMensaje.setText(mensaje)
            self.contador =  self.contador + 1
        if self.contador == 33:
            self.setStyleSheet('background-color:red')
            estilo = """
                    QPushButton {
                        box-shadow: 0px 10px 14px -7px #276873;
                        background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);
                        background-color:#000000;
                        border-radius:8px;
                        display:inline-block;
                        cursor:pointer;
                        color:#ffffff;
                        font-family:Arial;
                        font-size:20px;
                        font-weight:bold;
                        padding:13px 32px;
                        text-decoration:none;
                        text-shadow:0px 1px 0px #3d768a;
                    }
                    QPushButton:hover {
                        background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);
                        background-color:darkred;
                    }
                    """
            self.btnEmpezar.setStyleSheet(estilo)
        if self.contador >= 33:
            try:
                mensaje = lista_mensajes[self.contador]
            except:
                mensaje = ''
                self.close()
            
            self.lblMensaje.setText(mensaje.upper())
            estilo_mensaje = """
                                color:#FFFFFF;
                                font-family:Arial;
                                font-size:20px;
                                font-weight:bold;
                            """

            self.lblMensaje.setStyleSheet(estilo_mensaje)
            self.contador =  self.contador + 1
        # self.contador = self.contador + 1
        # print(self.contador)
        # try:
        #     texto = lista_mensajes[self.contador]
        # except:
        #     self.contador = 0
        #     self.close()
        # self.lblMensaje.setText(texto)
        # if self.contador == 28:
        #     texto_2 = "para"
        #     self.lbl2Mensaje.setText(texto_2)
        # else:
        #     self.lbl2Mensaje.setText("")
        # if self.contador == 30:
        #     texto_3 = "PARA"
        #     self.lbl3Mensaje.setText(texto_3)
        #   boton xdss
         
    def eventFilter(self,object,event):
        if event.type() == QEvent.Enter:
            if self.contador >= self.empezar and self.contador <= 19:
                x = randint(0+100,self.ancho-100)
                y = randint(0+100,self.alto-100)
                newpoint = QPoint(x,y)
                self.btnEmpezar.move(newpoint)
                mensaje = lista_mensajes[self.contador]
                self.lblMensaje.setText(mensaje)
                self.contador =  self.contador + 1
            if self.contador == 20:
                x = 410
                y = 270
                newpoint = QPoint(x,y)
                self.btnEmpezar.move(newpoint)
                mensaje = lista_mensajes[self.contador]
                self.lblMensaje.setText(mensaje)
                self.contador =  self.contador + 1
        return False #410 270
