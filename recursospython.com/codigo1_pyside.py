from urllib.request import urlopen

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtWidgets import QProgressBar


class Downloader(QThread):

    # Señal para que la ventana establezca el valor máximo
    # de la barra de progreso.
    setTotalProgress = Signal(int)
    # Señal para aumentar el progreso.
    setCurrentProgress = Signal(int)
    # Señal para indicar que el archivo se descargó correctamente.
    succeeded = Signal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def run(self):
        url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
        filename = "python-3.7.2.exe"
        readBytes = 0
        chunkSize = 1024
        # Abrir la dirección de URL.
        with urlopen(url) as r:
            # Avisar a la ventana cuántos bytes serán descargados.
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(filename, "ab") as f:
                while True:
                    # Leer una porción del archivo que estamos descargando.
                    chunk = r.read(chunkSize)
                    # Si el resultado es `None` quiere decir que todavía
                    # no se han descargado los datos. Simplemente
                    # seguimos esperando.
                    if chunk is None:
                        continue
                    # Si el resultado es una instancia de `bytes` vacía
                    # quiere decir que el archivo está completo.
                    elif chunk == b"":
                        break
                    # Escribir la porción descargada en el archivo local.
                    f.write(chunk)
                    readBytes += chunkSize
                    # Avisar a la ventana la cantidad de bytes recibidos.
                    self.setCurrentProgress.emit(readBytes)
        # Si esta línea llega a ejecutarse es porque no ocurrió ninguna
        # excepción en el código anterior.
        self.succeeded.emit()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Descarga con progreso en Qt (PySide)")
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
        # Ejecutar la descarga en un nuevo hilo.
        self.downloader = Downloader(
            "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe",
            "python-3.7.2.exe"
        )
        # Conectar las señales que indican el progreso de la descarga
        # con los métodos correspondientes de la barra de progreso.
        self.downloader.setTotalProgress.connect(self.progressBar.setMaximum)
        self.downloader.setCurrentProgress.connect(self.progressBar.setValue)
        # Qt invocará el método `succeeded` cuando el archivo se haya
        # descargado correctamente y `downloadFinished()` cuando el hilo 
        # haya terminado.
        self.downloader.succeeded.connect(self.downloadSucceeded)
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()
    
    def downloadSucceeded(self):
        # Establecer el progreso en 100%.
        self.progressBar.setValue(self.progressBar.maximum())
        self.label.setText("¡El archivo se ha descargado!")
    
    def downloadFinished(self):
        # Restablecer el botón.
        self.button.setEnabled(True)
        # Eliminar el hilo una vez que fue utilizado.
        del self.downloader


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()