from PyQt5 import QtCore, QtWidgets, QtGui
from service import SpotiFree


class Window(QtWidgets.QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.messageGroupBox = QtWidgets.QGroupBox("")
        self.adv = False
        self.init_msg = 'Aproveite o silêncio em vez das propagandas :D'
        self.spotifree = SpotiFree(start=False)
        self.createMessageGroupBox()
        self.createActions()
        self.createTrayIcon()
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.messageGroupBox)
        self.setLayout(mainLayout)
        self.trayIcon.show()
        self.setWindowTitle("SpotiFree")
        self.resize(400, 100)
        icon = QtGui.QIcon("icon.png")
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start()

    def tick(self):
        try:
            self.spotifree.verify()
            self.setWindowTitle("SpotiFree " + self.spotifree.get_text())
            self.typeLabel.setText(self.init_msg)
        except:
            self.typeLabel.setText('Spotify não encontrado, porfavor inicie o aplicativo')


    def createMessageGroupBox(self):
        self.typeLabel = QtWidgets.QLabel(self.init_msg)
        self.ok_button = QtWidgets.QPushButton("Ok")
        self.exit_button = QtWidgets.QPushButton("Sair")
        messageLayout = QtWidgets.QGridLayout()
        messageLayout.addWidget(self.typeLabel, 0, 0)
        messageLayout.addWidget(self.exit_button, 1, 4)
        messageLayout.addWidget(self.ok_button, 1, 3)
        self.messageGroupBox.setLayout(messageLayout)
        return

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            QtWidgets.QMessageBox.information(self, "SpotiFree",
                                          "O programa continuará executando. Para sair "
                                          "clique com botão direito no ícone no canto da tela"
                                          " e em seguida clique em <b>Sair</b>.")
            self.hide()
            event.ignore()

    def createActions(self):
        self.minimizeAction = QtWidgets.QAction("M&inimizar", self,
                                            triggered=self.hide)

        self.restoreAction = QtWidgets.QAction("R&estaurar", self,
                                           triggered=self.showNormal)

        self.quitAction = QtWidgets.QAction("&Sair", self,
                                        triggered=QtWidgets.qApp.quit)
                                        
        self.ok_button.clicked.connect(self.hide)
        self.exit_button.clicked.connect(QtWidgets.qApp.quit)
    
    def createTrayIcon(self):
        self.trayIconMenu = QtWidgets.QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QtWidgets.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
    window.show()
    sys.exit(app.exec_())
