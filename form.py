# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(668, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(668, 448))
        MainWindow.setMaximumSize(QtCore.QSize(668, 448))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.sendingMessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.sendingMessageLabel.setGeometry(QtCore.QRect(130, 30, 47, 13))
        self.sendingMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sendingMessageLabel.setObjectName("sendingMessageLabel")
        self.sign2LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sign2LineEdit.setGeometry(QtCore.QRect(360, 150, 281, 20))
        self.sign2LineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.sign2LineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sign2LineEdit.setReadOnly(True)
        self.sign2LineEdit.setObjectName("sign2LineEdit")
        self.answerLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.answerLineEdit.setEnabled(False)
        self.answerLineEdit.setGeometry(QtCore.QRect(430, 370, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.answerLineEdit.setFont(font)
        self.answerLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.answerLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLineEdit.setReadOnly(True)
        self.answerLineEdit.setObjectName("answerLineEdit")
        self.resultLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resultLineEdit.setGeometry(QtCore.QRect(360, 340, 281, 20))
        self.resultLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resultLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.resultLineEdit.setText("")
        self.resultLineEdit.setReadOnly(True)
        self.resultLineEdit.setObjectName("resultLineEdit")
        self.dLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dLineEdit.setGeometry(QtCore.QRect(20, 310, 281, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dLineEdit.sizePolicy().hasHeightForWidth())
        self.dLineEdit.setSizePolicy(sizePolicy)
        self.dLineEdit.setMouseTracking(False)
        self.dLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dLineEdit.setReadOnly(True)
        self.dLineEdit.setObjectName("dLineEdit")
        self.checkButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkButton.setEnabled(False)
        self.checkButton.setGeometry(QtCore.QRect(450, 250, 75, 23))
        self.checkButton.setObjectName("checkButton")
        self.privKeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.privKeyLabel.setGeometry(QtCore.QRect(130, 290, 61, 16))
        self.privKeyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.privKeyLabel.setObjectName("privKeyLabel")
        self.nLabel = QtWidgets.QLabel(self.centralwidget)
        self.nLabel.setGeometry(QtCore.QRect(10, 230, 16, 16))
        self.nLabel.setObjectName("nLabel")
        self.senderLabel = QtWidgets.QLabel(self.centralwidget)
        self.senderLabel.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.senderLabel.setObjectName("senderLabel")
        self.nLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nLineEdit.setGeometry(QtCore.QRect(20, 230, 281, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nLineEdit.sizePolicy().hasHeightForWidth())
        self.nLineEdit.setSizePolicy(sizePolicy)
        self.nLineEdit.setMouseTracking(False)
        self.nLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.nLineEdit.setReadOnly(True)
        self.nLineEdit.setObjectName("nLineEdit")
        self.sentMessageTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.sentMessageTextEdit.setGeometry(QtCore.QRect(360, 50, 281, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sentMessageTextEdit.sizePolicy().hasHeightForWidth())
        self.sentMessageTextEdit.setSizePolicy(sizePolicy)
        self.sentMessageTextEdit.setMouseTracking(False)
        self.sentMessageTextEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.sentMessageTextEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sentMessageTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.sentMessageTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sentMessageTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sentMessageTextEdit.setTabChangesFocus(True)
        self.sentMessageTextEdit.setUndoRedoEnabled(False)
        self.sentMessageTextEdit.setReadOnly(False)
        self.sentMessageTextEdit.setObjectName("sentMessageTextEdit")
        self.dLabel = QtWidgets.QLabel(self.centralwidget)
        self.dLabel.setGeometry(QtCore.QRect(10, 310, 16, 16))
        self.dLabel.setObjectName("dLabel")
        self.eLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.eLabel_2.setGeometry(QtCore.QRect(350, 190, 16, 16))
        self.eLabel_2.setObjectName("eLabel_2")
        self.opKeyLable_2 = QtWidgets.QLabel(self.centralwidget)
        self.opKeyLable_2.setGeometry(QtCore.QRect(460, 170, 51, 16))
        self.opKeyLable_2.setAlignment(QtCore.Qt.AlignCenter)
        self.opKeyLable_2.setObjectName("opKeyLable_2")
        self.signLabel = QtWidgets.QLabel(self.centralwidget)
        self.signLabel.setGeometry(QtCore.QRect(140, 250, 21, 16))
        self.signLabel.setObjectName("signLabel")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(470, 320, 41, 20))
        self.resultLabel.setObjectName("resultLabel")
        self.signLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.signLineEdit.setGeometry(QtCore.QRect(20, 270, 281, 20))
        self.signLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.signLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.signLineEdit.setReadOnly(True)
        self.signLineEdit.setObjectName("signLineEdit")
        self.hashLabel = QtWidgets.QLabel(self.centralwidget)
        self.hashLabel.setGeometry(QtCore.QRect(450, 280, 71, 20))
        self.hashLabel.setObjectName("hashLabel")
        self.eLineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.eLineEdit2.setGeometry(QtCore.QRect(360, 190, 281, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eLineEdit2.sizePolicy().hasHeightForWidth())
        self.eLineEdit2.setSizePolicy(sizePolicy)
        self.eLineEdit2.setMouseTracking(False)
        self.eLineEdit2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.eLineEdit2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.eLineEdit2.setReadOnly(True)
        self.eLineEdit2.setObjectName("eLineEdit2")
        self.sendingMessageTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.sendingMessageTextEdit.setGeometry(QtCore.QRect(20, 50, 281, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendingMessageTextEdit.sizePolicy().hasHeightForWidth())
        self.sendingMessageTextEdit.setSizePolicy(sizePolicy)
        self.sendingMessageTextEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sendingMessageTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sendingMessageTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sendingMessageTextEdit.setTabChangesFocus(True)
        self.sendingMessageTextEdit.setUndoRedoEnabled(False)
        self.sendingMessageTextEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.sendingMessageTextEdit.setObjectName("sendingMessageTextEdit")
        self.sentMessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.sentMessageLabel.setGeometry(QtCore.QRect(460, 30, 47, 13))
        self.sentMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sentMessageLabel.setObjectName("sentMessageLabel")
        self.eLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.eLineEdit.setGeometry(QtCore.QRect(20, 200, 281, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eLineEdit.sizePolicy().hasHeightForWidth())
        self.eLineEdit.setSizePolicy(sizePolicy)
        self.eLineEdit.setMouseTracking(False)
        self.eLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.eLineEdit.setReadOnly(True)
        self.eLineEdit.setObjectName("eLineEdit")
        self.opKeyLable = QtWidgets.QLabel(self.centralwidget)
        self.opKeyLable.setGeometry(QtCore.QRect(130, 180, 51, 16))
        self.opKeyLable.setAlignment(QtCore.Qt.AlignCenter)
        self.opKeyLable.setObjectName("opKeyLable")
        self.hashLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.hashLineEdit.setGeometry(QtCore.QRect(360, 300, 281, 20))
        self.hashLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hashLineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.hashLineEdit.setReadOnly(True)
        self.hashLineEdit.setObjectName("hashLineEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setEnabled(False)
        self.sendButton.setGeometry(QtCore.QRect(120, 340, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setCheckable(False)
        self.sendButton.setFlat(False)
        self.sendButton.setObjectName("sendButton")
        self.eLabel = QtWidgets.QLabel(self.centralwidget)
        self.eLabel.setGeometry(QtCore.QRect(10, 200, 16, 16))
        self.eLabel.setObjectName("eLabel")
        self.sign2Label = QtWidgets.QLabel(self.centralwidget)
        self.sign2Label.setGeometry(QtCore.QRect(470, 130, 21, 20))
        self.sign2Label.setObjectName("sign2Label")
        self.nLineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.nLineEdit2.setGeometry(QtCore.QRect(360, 220, 281, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nLineEdit2.sizePolicy().hasHeightForWidth())
        self.nLineEdit2.setSizePolicy(sizePolicy)
        self.nLineEdit2.setMouseTracking(False)
        self.nLineEdit2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nLineEdit2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.nLineEdit2.setReadOnly(True)
        self.nLineEdit2.setObjectName("nLineEdit2")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setEnabled(False)
        self.generateButton.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.generateButton.setCheckable(False)
        self.generateButton.setChecked(False)
        self.generateButton.setObjectName("generateButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 10, 20, 391))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.recipientLabel = QtWidgets.QLabel(self.centralwidget)
        self.recipientLabel.setGeometry(QtCore.QRect(460, 10, 47, 13))
        self.recipientLabel.setObjectName("recipientLabel")
        self.nLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.nLabel_2.setGeometry(QtCore.QRect(350, 220, 16, 16))
        self.nLabel_2.setObjectName("nLabel_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA ЭЦП"))
        self.sendingMessageLabel.setText(_translate("MainWindow", "Message"))
        self.checkButton.setText(_translate("MainWindow", "Check"))
        self.privKeyLabel.setText(_translate("MainWindow", "Private key"))
        self.nLabel.setText(_translate("MainWindow", "n"))
        self.senderLabel.setText(_translate("MainWindow", "Sender"))
        self.dLabel.setText(_translate("MainWindow", "d"))
        self.eLabel_2.setText(_translate("MainWindow", "e"))
        self.opKeyLable_2.setText(_translate("MainWindow", "Open  key"))
        self.signLabel.setText(_translate("MainWindow", "Sign"))
        self.resultLabel.setText(_translate("MainWindow", "Result"))
        self.hashLabel.setText(_translate("MainWindow", "Message Hash"))
        self.sentMessageLabel.setText(_translate("MainWindow", "Message"))
        self.opKeyLable.setText(_translate("MainWindow", "Open  key"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.eLabel.setText(_translate("MainWindow", "e"))
        self.sign2Label.setText(_translate("MainWindow", "Sign"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.recipientLabel.setText(_translate("MainWindow", "Recipient"))
        self.nLabel_2.setText(_translate("MainWindow", "n"))