import sys  # We need sys so that we can pass argv to QApplication

from PyQt4 import QtCore, QtGui

from DITagger import mainWindow_ui  # This file holds our MainWindow and all design related things


# it also keeps events etc that we defined in Qt Designer


class ExampleApp(QtGui.QMainWindow, mainWindow_ui.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        # self.actionOpen.connect(self.browse_folder()) # When the button is pressed
        # Execute browse_folder function

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        print("Open")


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
