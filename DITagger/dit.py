import sys  # We need sys so that we can pass argv to QApplication

from PyQt4 import QtCore, QtGui

from DITagger import model, windows_ui  # This file holds our MainWindow and all design related things


# it also keeps events etc that we defined in Qt Designer


class DitApp(QtGui.QMainWindow, windows_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.FileWidget.show()
        self.settings = model.SettingsModel()
        self.image = model.ImageModel()
        self.settings.load()
        # This is defined in windows_ui.py file automatically
        # It sets up layout and widgets that are defined
        # self.actionOpen.connect(self.browse_folder()) # When the button is pressed
        # Execute browse_folder function

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        _fileDialogue = QtGui.QFileDialog()
        _fileDialogue.setFilter("Image Files (*.jpg)")
        _openFile = _fileDialogue.getOpenFileName()
        _pixmap = QtGui.QPixmap(_openFile)
        self.image.fullpath = str(_openFile)  # Covert QString to String
        self.pictureViewLbl.setPixmap(_pixmap)
        self.idTxt.setText(self.image.ditid)
        self.lesionTxt.setText(self.image.lesion)
        self.diagnosisTxt.setText(self.image.diagnosis)
        self.locationTxt.setText(self.image.location)
        self.commentTxt.setText(self.image.ditcomment)

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        sys.exit(0)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = DitApp()  # We set the form to be our DitApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
