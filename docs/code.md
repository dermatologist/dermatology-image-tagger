from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.btnBrowse.clicked.connect(self.browse_folder)  # When the button is pressed
                                                            # Execute browse_folder function

    def browse_folder(self):
        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function


Just add all your widgets into the layout and use QWidget::hide(), QWidget::show() when needed.



if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mw_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    img_widget = ImageWidget(MainWindow)

    sys.exit(app.exec_())

class ImageWidget(QtGui.QWidget):
    def __init__(self, parent, variables):
        # self.ui = ui
        # self.variables = variables
        if not isinstance(parent, QtGui.QMainWindow):
            raise TypeError('parent must be a QMainWindow')
        super(ImageWidget, self).__init__()

        self._parentWidget = parent

        imglabel = self.ui.findChild(QtGui.QLabel, "imglabel")


http://gis.stackexchange.com/questions/32263/how-to-reference-to-my-in-qt-designer-created-buttons-in-python

