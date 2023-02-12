from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtWidgets import QProgressBar

from twisted.internet.defer import inlineCallbacks


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Descarga con progreso en PyQt")
        self.resize(400, 300)
        self.label = QLabel("Presione el botón para iniciar la descarga.",
            self)
        self.label.setGeometry(20, 20, 200, 25)
        self.button = QPushButton("Iniciar descarga", self)
        self.button.move(20, 60)
        self.button.pressed.connect(self.initDownload)
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(20, 115, 300, 25)
    
    def initDownload(self):
        self.label.setText("Descargando archivo...")
        # Deshabilitar el botón mientras se descarga el archivo.
        self.button.setEnabled(False)
        url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
        # El método `requestSucceeded()` será invocado cuando la conexión
        # con la dirección de URL se haya establecido correctamente.
        treq.get(url).addCallback(self.requestSucceeded)
    
    def collector(self, chunk):
        """
        Esta función es invocada por Twisted cada vez que se recibe
        un pedazo (`chunk`) del archivo que estamos descargando.
        """
        self.progressBar.setValue(self.progressBar.value() + len(chunk))
        self.f.write(chunk)

    def requestSucceeded(self, response):
        # Obtener el tamaño del archivo que vamos a descargar y establecerlo
        # como el máximo de la barra de progreso.
        self.progressBar.setMaximum(response.length)
        # Abrimos el archivo en modo "ab" para ir escribiendo por partes.
        self.f = open("python-3.7.2.exe", "ab")
        # Iniciamos la descarga, indicando que `downloadSucceeded` debe
        # invocarse si la descarga resulta exitosa, y `downloadFinished`
        # indistintamente si resulta exitosa o fallida.
        treq.collect(response, self.collector).addCallback(
            self.downloadSucceeded
        ).addBoth(
            self.downloadFinished
        )
    
    def downloadSucceeded(self, result):
        self.progressBar.setValue(self.progressBar.maximum())
        self.label.setText("¡El archivo se ha descargado!")
    
    def downloadFinished(self, result):
        self.f.close()
        # Restablecer el botón.
        self.button.setEnabled(True)
    
    def closeEvent(self, event):
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication([])
    import qt5reactor
    qt5reactor.install()
    window = MainWindow()
    window.show()
    from twisted.internet import reactor
    import treq
    import os
    import certifi
    # Necesario para conexiones vía HTTPS.
    os.environ["SSL_CERT_FILE"] = certifi.where()
    reactor.run()