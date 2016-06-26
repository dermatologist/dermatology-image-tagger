import os.path
import sys  # We need sys so that we can pass argv to QApplication

from PyQt4 import QtCore, QtGui

from DITagger import model, windows_ui  # This file holds our MainWindow and all design related things


class DitApp(QtGui.QMainWindow, windows_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.FileWidget)
        self.settings = model.SettingsModel()
        self.image = model.ImageModel()
        self.settings.load()
        # This is defined in windows_ui.py file automatically
        # It sets up layout and widgets that are defined
        # self.actionOpen.connect(self.browse_folder()) # When the button is pressed
        # Execute browse_folder function

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        self.stackedWidget.setCurrentWidget(self.FileWidget)
        _fileDialogue = QtGui.QFileDialog()
        _fileDialogue.setFilter("Image Files (*.jpg)")
        _openFile = _fileDialogue.getOpenFileName()
        _pixmap = QtGui.QPixmap(_openFile)
        self.image.fullpath = str(_openFile)  # Covert QString to String
        self.pictureViewLbl.setPixmap(_pixmap)
        # Clear Values
        self.idTxt.clear()
        self.lesionTxt.clear()
        self.diagnosisTxt.clear()
        self.locationTxt.clear()
        self.dateTxt.clear()
        self.commentTxt.clear()

        self.idTxt.setText(self.image.ditid)
        self.lesionTxt.setText(self.image.lesion)
        self.diagnosisTxt.setText(self.image.diagnosis)
        self.locationTxt.setText(self.image.location)
        self.dateTxt.setText(self.image.ditdate)
        self.commentTxt.setText(self.image.ditcomment)

    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        self.stackedWidget.setCurrentWidget(self.FileWidget)
        _pixmap = QtGui.QPixmap(QtCore.QString(self.image.fullpath))
        self.pictureViewLbl.setPixmap(_pixmap)
        self.image.ditid = str(self.idTxt.text())
        self.image.lesion = str(self.lesionTxt.text())
        self.image.diagnosis = str(self.diagnosisTxt.text())
        self.image.location = str(self.locationTxt.text())
        self.image.ditdate = str(self.dateTxt.text())
        self.image.ditcomment = str(self.commentTxt.text())
        self.image.ditsave()

    @QtCore.pyqtSlot()
    def on_actionDefault_triggered(self):
        self.stackedWidget.setCurrentWidget(self.SettingsWidget)

    @QtCore.pyqtSlot()
    def on_actionFind_triggered(self):
        self.stackedWidget.setCurrentWidget(self.SearchWidget)

    @QtCore.pyqtSlot()
    def on_chooseFolderButton_clicked(self):
        _folder = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Folder"))
        self.folderList.addItem(_folder)

    @QtCore.pyqtSlot()
    def on_folderRemoveButton_clicked(self):
        # stackoverflow 23145051
        for _folder in self.folderList.selectedItems():
            self.folderList.takeItem(self.folderList.row(_folder))

    @QtCore.pyqtSlot()
    def on_saveSettingButton_clicked(self):
        _folders = []
        for index in xrange(self.folderList.count()):
            _folders.append(self.folderList.item(index))
        _labels = [i.text() for i in _folders]
        self.settings.add_setting('folders', _labels)
        self.settings.save()

    @QtCore.pyqtSlot()
    def on_loadSettingButton_clicked(self):
        self.settings.load()
        _folders = self.settings.get_setting('folders')
        for _folder in _folders:
            self.folderList.addItem(_folder)

    @QtCore.pyqtSlot()
    def on_searchButton_clicked(self):
        _buffer = []
        for index in xrange(self.folderList.count()):
            _buffer.append(self.folderList.item(index))
        _folderList = [i.text() for i in _buffer]
        for _folder in _folderList:
            for root, dirs, files in os.walk(str(_folder)):
                for filename in files:
                    if filename.lower().endswith(('.jpg', '.jpeg')):
                        self.image.fullpath = os.path.join(root, filename)
                        if self.image.hasIt(str(self.searchTxt.text())):
                            self.searchList.addItem(self.image.fullpath)



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
