# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/beapen/PycharmProjects/DITagger/DITagger/windows.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(643, 489)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 441))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.FileWidget = QtGui.QWidget()
        self.FileWidget.setObjectName(_fromUtf8("FileWidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.FileWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 641, 221))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pictureViewLbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.pictureViewLbl.setText(_fromUtf8(""))
        self.pictureViewLbl.setObjectName(_fromUtf8("pictureViewLbl"))
        self.verticalLayout_2.addWidget(self.pictureViewLbl)
        self.formLayoutWidget = QtGui.QWidget(self.FileWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 220, 641, 245))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.idTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.idTxt.setObjectName(_fromUtf8("idTxt"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.idTxt)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lesionTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.lesionTxt.setObjectName(_fromUtf8("lesionTxt"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lesionTxt)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.diagnosisTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.diagnosisTxt.setObjectName(_fromUtf8("diagnosisTxt"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.diagnosisTxt)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.locationTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.locationTxt.setObjectName(_fromUtf8("locationTxt"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.locationTxt)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.dateEdit = QtGui.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateEdit)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.commentTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.commentTxt.setObjectName(_fromUtf8("commentTxt"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.commentTxt)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.label_7)
        self.stackedWidget.addWidget(self.FileWidget)
        self.SearchWidget = QtGui.QWidget()
        self.SearchWidget.setObjectName(_fromUtf8("SearchWidget"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.SearchWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 381, 411))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.searchTxt = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.searchTxt.setObjectName(_fromUtf8("searchTxt"))
        self.verticalLayout_4.addWidget(self.searchTxt)
        self.searchButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.verticalLayout_4.addWidget(self.searchButton)
        self.searchTable = QtGui.QTableView(self.verticalLayoutWidget_3)
        self.searchTable.setObjectName(_fromUtf8("searchTable"))
        self.searchTable.horizontalHeader().setCascadingSectionResizes(True)
        self.searchTable.verticalHeader().setVisible(False)
        self.searchTable.verticalHeader().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.searchTable)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.SearchWidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(380, 0, 251, 411))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.pictureSearchView = QtGui.QGraphicsView(self.verticalLayoutWidget_4)
        self.pictureSearchView.setObjectName(_fromUtf8("pictureSearchView"))
        self.verticalLayout_5.addWidget(self.pictureSearchView)
        self.searchTable2 = QtGui.QTableWidget(self.verticalLayoutWidget_4)
        self.searchTable2.setObjectName(_fromUtf8("searchTable2"))
        self.searchTable2.setColumnCount(0)
        self.searchTable2.setRowCount(0)
        self.verticalLayout_5.addWidget(self.searchTable2)
        self.searchProgressBar = QtGui.QProgressBar(self.SearchWidget)
        self.searchProgressBar.setGeometry(QtCore.QRect(0, 410, 118, 23))
        self.searchProgressBar.setProperty("value", 24)
        self.searchProgressBar.setObjectName(_fromUtf8("searchProgressBar"))
        self.stackedWidget.addWidget(self.SearchWidget)
        self.SettingsWidget = QtGui.QWidget()
        self.SettingsWidget.setObjectName(_fromUtf8("SettingsWidget"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.SettingsWidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(-1, -1, 641, 441))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chooseFolderButton = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.chooseFolderButton.setObjectName(_fromUtf8("chooseFolderButton"))
        self.verticalLayout_3.addWidget(self.chooseFolderButton)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget_5)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_3.addWidget(self.listWidget)
        self.loadSettingButton = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.loadSettingButton.setObjectName(_fromUtf8("loadSettingButton"))
        self.verticalLayout_3.addWidget(self.loadSettingButton)
        self.saveSettingButton = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.saveSettingButton.setObjectName(_fromUtf8("saveSettingButton"))
        self.verticalLayout_3.addWidget(self.saveSettingButton)
        self.stackedWidget.addWidget(self.SettingsWidget)
        self.helpWidget = QtGui.QWidget()
        self.helpWidget.setObjectName(_fromUtf8("helpWidget"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.helpWidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(150, 60, 361, 261))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.helpNameLbl = QtGui.QLabel(self.formLayoutWidget_2)
        self.helpNameLbl.setObjectName(_fromUtf8("helpNameLbl"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.helpNameLbl)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.helpAuthorLbl = QtGui.QLabel(self.formLayoutWidget_2)
        self.helpAuthorLbl.setObjectName(_fromUtf8("helpAuthorLbl"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.helpAuthorLbl)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.helpLicenseLbl = QtGui.QLabel(self.formLayoutWidget_2)
        self.helpLicenseLbl.setObjectName(_fromUtf8("helpLicenseLbl"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.helpLicenseLbl)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.helpVersionLbl = QtGui.QLabel(self.formLayoutWidget_2)
        self.helpVersionLbl.setObjectName(_fromUtf8("helpVersionLbl"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.helpVersionLbl)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_11)
        self.helpUpdateLbl = QtGui.QLabel(self.formLayoutWidget_2)
        self.helpUpdateLbl.setObjectName(_fromUtf8("helpUpdateLbl"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.helpUpdateLbl)
        self.label_12 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_12)
        self.stackedWidget.addWidget(self.helpWidget)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setObjectName(_fromUtf8("menuSearch"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionRestore = QtGui.QAction(MainWindow)
        self.actionRestore.setObjectName(_fromUtf8("actionRestore"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionDefault = QtGui.QAction(MainWindow)
        self.actionDefault.setObjectName(_fromUtf8("actionDefault"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCheck_for_Updates = QtGui.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(_fromUtf8("actionCheck_for_Updates"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionRestore)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSearch.addAction(self.actionFind)
        self.menuSettings.addAction(self.actionDefault)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dermatology Image Tagger", None))
        self.label.setText(_translate("MainWindow", "ID", None))
        self.label_2.setText(_translate("MainWindow", "Lesion", None))
        self.label_3.setText(_translate("MainWindow", "Diagnosis", None))
        self.label_4.setText(_translate("MainWindow", "Location", None))
        self.label_5.setText(_translate("MainWindow", "Date", None))
        self.label_6.setText(_translate("MainWindow", "Comment", None))
        self.label_7.setText(
            _translate("MainWindow", "By Dermatologists Sans Borders http://dermatologist.co.in", None))
        self.searchTxt.setPlaceholderText(_translate("MainWindow", "Search Term", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.chooseFolderButton.setText(_translate("MainWindow", "Choose Folder to Add to Search Path", None))
        self.loadSettingButton.setText(_translate("MainWindow", "Load Setting", None))
        self.saveSettingButton.setText(_translate("MainWindow", "Save Settings", None))
        self.helpNameLbl.setText(_translate("MainWindow", "DIT", None))
        self.label_8.setText(_translate("MainWindow", "by", None))
        self.helpAuthorLbl.setText(_translate("MainWindow", "Bell Eapen", None))
        self.label_10.setText(_translate("MainWindow", "License", None))
        self.helpLicenseLbl.setText(_translate("MainWindow", "LGPL", None))
        self.label_9.setText(_translate("MainWindow", "Version", None))
        self.helpVersionLbl.setText(_translate("MainWindow", "0.5.0", None))
        self.label_11.setText(_translate("MainWindow", "Current Version:", None))
        self.helpUpdateLbl.setText(_translate("MainWindow", "Check for Updates", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSearch.setTitle(_translate("MainWindow", "Search", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionRestore.setText(_translate("MainWindow", "Restore", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionFind.setText(_translate("MainWindow", "Find", None))
        self.actionDefault.setText(_translate("MainWindow", "Default", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates", None))
