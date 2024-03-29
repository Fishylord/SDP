
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView, QPushButton, QMessageBox

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1080, 720))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1080, 720))
        self.stackedWidget.setStyleSheet("background-color: grey")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Login_Page = QtWidgets.QWidget()
        self.Login_Page.setMaximumSize(QtCore.QSize(1080, 16777215))
        self.Login_Page.setStyleSheet("")
        self.Login_Page.setObjectName("Login_Page")
        self.gridLayout = QtWidgets.QGridLayout(self.Login_Page)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.Login_Page)
        self.frame_2.setStyleSheet("background: grey")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget_3.setGeometry(QtCore.QRect(410, 170, 232, 432))
        self.stackedWidget_3.setStyleSheet("*{\n"
"    color: #fff;\n"
"    background-color: rgb(9,27,68);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#Widget{\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(9,10,37);\n"
"    padding: 5px 3px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(9, 10, 37);\n"
"    padding: 10px 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setStyleSheet("")
        self.page_7.setObjectName("page_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.page_7)
        self.label_10.setMinimumSize(QtCore.QSize(30, 40))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Icons/user.svg"))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_16 = QtWidgets.QFrame(self.page_7)
        self.frame_16.setStyleSheet("")
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_9.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_9.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_9.addWidget(self.lineEdit_6)
        self.verticalLayout_8.addWidget(self.frame_16)
        self.pushButton_11 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_8.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_8.addWidget(self.pushButton_12)
        self.label_12 = QtWidgets.QLabel(self.page_7)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setStyleSheet("Qwidget {\n"
"    background-color: rgb(9,27,68);\n"
"    border-radius: 20px;\n"
"}")
        self.page_8.setObjectName("page_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.page_8)
        self.label_13.setMinimumSize(QtCore.QSize(30, 40))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Icons/user.svg"))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.page_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_17 = QtWidgets.QFrame(self.page_8)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_11.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_11.addWidget(self.lineEdit_13)
        self.verticalLayout_10.addWidget(self.frame_17)
        self.pushButton_13 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_10.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_10.addWidget(self.pushButton_14)
        self.label_15 = QtWidgets.QLabel(self.page_8)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.stackedWidget_3.addWidget(self.page_8)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Login_Page)
        self.UserProfile_2 = QtWidgets.QWidget()
        self.UserProfile_2.setObjectName("UserProfile_2")
        self.frame_20 = QtWidgets.QFrame(self.UserProfile_2)
        self.frame_20.setGeometry(QtCore.QRect(0, 0, 1131, 761))
        self.frame_20.setStyleSheet("#frame_20{\n"
                                    "    background-color:white;\n"
                                    "}\n"
                                    "\n"
                                    "#frame_20 QLabel{\n"
                                    "    background-color: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton {\n"
                                    "  background-color: transparent;\n"
                                    "  border-radius: 10px;\n"
                                    "  border: 2px solid black;\n"
                                    "  padding: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QTextEdit{\n"
                                    " background-color: transparent;\n"
                                    "  border-radius: 3px;\n"
                                    "  border: 2px solid black;\n"
                                    "  padding: 4px;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_20.setObjectName("frame_20")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_8.setGeometry(QtCore.QRect(870, 630, 150, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_8 = QtWidgets.QLabel(self.frame_20)
        self.label_8.setGeometry(QtCore.QRect(100, 220, 111, 16))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit.setGeometry(QtCore.QRect(100, 250, 211, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 300, 211, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 350, 211, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_4.setGeometry(QtCore.QRect(100, 400, 211, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_58 = QtWidgets.QLabel(self.frame_20)
        self.label_58.setGeometry(QtCore.QRect(520, 210, 71, 16))
        self.label_58.setObjectName("label_58")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_5.setGeometry(QtCore.QRect(520, 240, 91, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_7 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_7.setGeometry(QtCore.QRect(520, 290, 71, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_8.setGeometry(QtCore.QRect(520, 350, 81, 41))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_9.setGeometry(QtCore.QRect(520, 400, 211, 61))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_10.setGeometry(QtCore.QRect(520, 470, 211, 71))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_11.setGeometry(QtCore.QRect(520, 550, 211, 71))
        self.textEdit_11.setObjectName("textEdit_11")
        self.frame_43 = QtWidgets.QFrame(self.frame_20)
        self.frame_43.setGeometry(QtCore.QRect(0, 0, 1081, 161))
        self.frame_43.setStyleSheet("#frame_43{\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:1, stop:0.570621 rgba(46, 46, 46, 255), stop:1 rgba(109, 109, 109, 255));\n"
                                    "}\n"
                                    "\n"
                                    "#frame_43 QLabel{\n"
                                    "    background-color: transparent;\n"
                                    "    text-color: white;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton {\n"
                                    "  background-color: white;\n"
                                    "  border-radius: 10px;\n"
                                    "  border: 2px solid black;\n"
                                    "  padding: 3px;\n"
                                    "}\n"
                                    "")
        self.frame_43.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_43.setObjectName("frame_43")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_43)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 20, 91, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.frame_43)
        self.label.setGeometry(QtCore.QRect(460, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255,255,255);")
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_43)
        self.pushButton_6.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_25 = QtWidgets.QLabel(self.frame_20)
        self.label_25.setGeometry(QtCore.QRect(60, 260, 31, 16))
        self.label_25.setObjectName("label_25")
        self.label_78 = QtWidgets.QLabel(self.frame_20)
        self.label_78.setGeometry(QtCore.QRect(20, 360, 81, 20))
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.frame_20)
        self.label_79.setGeometry(QtCore.QRect(60, 310, 31, 16))
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.frame_20)
        self.label_80.setGeometry(QtCore.QRect(40, 410, 61, 20))
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.frame_20)
        self.label_81.setGeometry(QtCore.QRect(470, 250, 41, 20))
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.frame_20)
        self.label_82.setGeometry(QtCore.QRect(480, 300, 31, 16))
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.frame_20)
        self.label_83.setGeometry(QtCore.QRect(450, 360, 61, 20))
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.frame_20)
        self.label_84.setGeometry(QtCore.QRect(470, 420, 61, 20))
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.frame_20)
        self.label_85.setGeometry(QtCore.QRect(460, 490, 61, 20))
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.frame_20)
        self.label_86.setGeometry(QtCore.QRect(450, 570, 61, 20))
        self.label_86.setObjectName("label_86")
        self.stackedWidget.addWidget(self.UserProfile_2)
        self.Reward = QtWidgets.QWidget()
        self.Reward.setObjectName("Reward")
        self.frame_14 = QtWidgets.QFrame(self.Reward)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 1101, 751))
        self.frame_14.setStyleSheet("#frame_14{\n"
                                    "    background-color:white;\n"
                                    "}\n"
                                    "\n"
                                    "#frame_14 QLabel{\n"
                                    "    background-color: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton {\n"
                                    "  background-color: transparent;\n"
                                    "  border-radius: 10px;\n"
                                    "  border: 2px solid black;\n"
                                    "  padding: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QTextEdit{\n"
                                    " background-color: transparent;\n"
                                    "  border-radius: 3px;\n"
                                    "  border: 2px solid black;\n"
                                    "  padding: 4px;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.Header = QtWidgets.QFrame(self.frame_14)
        self.Header.setGeometry(QtCore.QRect(0, 0, 1111, 111))
        self.Header.setStyleSheet("#Header{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:1, stop:0.570621 rgba(46, 46, 46, 255), stop:1 rgba(109, 109, 109, 255));\n"
                                  "}\n"
                                  "\n"
                                  "#Header QLabel{\n"
                                  "    background-color: transparent;\n"
                                  "    text-color: white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton {\n"
                                  "  background-color: white;\n"
                                  "  border-radius: 10px;\n"
                                  "  border: 2px solid black;\n"
                                  "  padding: 3px;\n"
                                  "}\n"
                                  "")
        self.Header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Header.setObjectName("Header")
        self.label_5 = QtWidgets.QLabel(self.Header)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255,255,255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.Header)
        self.pushButton_9.setGeometry(QtCore.QRect(950, 0, 91, 31))
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Header)
        self.pushButton_10.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.frame_44 = QtWidgets.QFrame(self.frame_14)
        self.frame_44.setGeometry(QtCore.QRect(30, 170, 1021, 531))
        self.frame_44.setStyleSheet("background-color: rgb(236, 224, 193);\n"
                                    "  border-radius: 20px;\n"
                                    "  border: 2px solid black;\n"
                                    "  padding: 4px;\n"
                                    "\n"
                                    "\n"
                                    "")
        self.frame_44.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_44.setObjectName("frame_44")
        self.frame_45 = QtWidgets.QFrame(self.frame_44)
        self.frame_45.setGeometry(QtCore.QRect(15, 15, 493, 163))
        self.frame_45.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_45.setObjectName("frame_45")
        self.label_59 = QtWidgets.QLabel(self.frame_45)
        self.label_59.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label_59.setObjectName("label_59")
        self.label_65 = QtWidgets.QLabel(self.frame_45)
        self.label_65.setGeometry(QtCore.QRect(200, 60, 95, 61))
        self.label_65.setObjectName("label_65")
        self.frame_46 = QtWidgets.QFrame(self.frame_44)
        self.frame_46.setGeometry(QtCore.QRect(15, 184, 493, 163))
        self.frame_46.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_46.setObjectName("frame_46")
        self.label_60 = QtWidgets.QLabel(self.frame_46)
        self.label_60.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_60.setObjectName("label_60")
        self.label_67 = QtWidgets.QLabel(self.frame_46)
        self.label_67.setGeometry(QtCore.QRect(120, 60, 265, 61))
        self.label_67.setObjectName("label_67")
        self.frame_47 = QtWidgets.QFrame(self.frame_44)
        self.frame_47.setGeometry(QtCore.QRect(15, 353, 493, 163))
        self.frame_47.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_47.setObjectName("frame_47")
        self.label_61 = QtWidgets.QLabel(self.frame_47)
        self.label_61.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_61.setObjectName("label_61")
        self.label_69 = QtWidgets.QLabel(self.frame_47)
        self.label_69.setGeometry(QtCore.QRect(130, 60, 210, 61))
        self.label_69.setObjectName("label_69")
        self.frame_52 = QtWidgets.QFrame(self.frame_44)
        self.frame_52.setGeometry(QtCore.QRect(514, 15, 492, 163))
        self.frame_52.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_52.setObjectName("frame_52")
        self.label_62 = QtWidgets.QLabel(self.frame_52)
        self.label_62.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_62.setObjectName("label_62")
        self.label_66 = QtWidgets.QLabel(self.frame_52)
        self.label_66.setGeometry(QtCore.QRect(220, 60, 91, 61))
        self.label_66.setObjectName("label_66")
        self.frame_53 = QtWidgets.QFrame(self.frame_44)
        self.frame_53.setGeometry(QtCore.QRect(514, 184, 492, 163))
        self.frame_53.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_53.setObjectName("frame_53")
        self.label_63 = QtWidgets.QLabel(self.frame_53)
        self.label_63.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_63.setObjectName("label_63")
        self.label_68 = QtWidgets.QLabel(self.frame_53)
        self.label_68.setGeometry(QtCore.QRect(180, 60, 190, 61))
        self.label_68.setObjectName("label_68")
        self.frame_54 = QtWidgets.QFrame(self.frame_44)
        self.frame_54.setGeometry(QtCore.QRect(514, 353, 492, 163))
        self.frame_54.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_54.setObjectName("frame_54")
        self.label_64 = QtWidgets.QLabel(self.frame_54)
        self.label_64.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_64.setObjectName("label_64")
        self.label_70 = QtWidgets.QLabel(self.frame_54)
        self.label_70.setGeometry(QtCore.QRect(120, 60, 315, 61))
        self.label_70.setObjectName("label_70")
        self.label_57 = QtWidgets.QLabel(self.frame_14)
        self.label_57.setGeometry(QtCore.QRect(420, 130, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(30, 89, 165);")
        self.label_57.setObjectName("label_57")
        self.label_71 = QtWidgets.QLabel(self.frame_14)
        self.label_71.setGeometry(QtCore.QRect(50, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.stackedWidget.addWidget(self.Reward)
        self.Home_Page = QtWidgets.QWidget()
        self.Home_Page.setStyleSheet("background-color: grey")
        self.Home_Page.setObjectName("Home_Page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Home_Page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.Home_Page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(-1, 0, 1081, 111))
        self.frame_7.setStyleSheet("#frame_7{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:1, stop:0.570621 rgba(46, 46, 46, 255), stop:1 rgba(109, 109, 109, 255));\n"
"}\n"
"\n"
"#frame_7 QLabel{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: transparent;\n"
"  border-radius: 10px;\n"
"  border: 2px solid black;\n"
"  padding: 10px;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.HButton_8 = QtWidgets.QPushButton(self.frame_7)
        self.HButton_8.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.HButton_8.setText("")
        self.HButton_8.setIcon(icon1)
        self.HButton_8.setIconSize(QtCore.QSize(20, 20))
        self.HButton_8.setObjectName("HButton_8")
        self.Hlabel_1 = QtWidgets.QLabel(self.frame_7)
        self.Hlabel_1.setGeometry(QtCore.QRect(10, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Hlabel_1.setFont(font)
        self.Hlabel_1.setStyleSheet("background-color: transparent;")
        self.Hlabel_1.setObjectName("Hlabel_1")
        self.Hlabel_2 = QtWidgets.QLabel(self.frame_7)
        self.Hlabel_2.setGeometry(QtCore.QRect(10, 10, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Hlabel_2.setFont(font)
        self.Hlabel_2.setObjectName("Hlabel_2")
        self.HButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.HButton_7.setGeometry(QtCore.QRect(930, 0, 111, 41))
        self.HButton_7.setObjectName("HButton_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setGeometry(QtCore.QRect(0, 110, 1091, 481))
        self.frame_8.setStyleSheet("QPushButton {\n"
"  border-radius: 10px;\n"
"  border: 2px solid black;\n"
"  padding: 10px;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.HButton_1 = QtWidgets.QPushButton(self.frame_8)
        self.HButton_1.setGeometry(QtCore.QRect(50, 330, 181, 101))
        self.HButton_1.setStyleSheet("QPushButton {\n"
"  border-radius: 10px;\n"
"  border: 2px solid black;\n"
"  padding: 10px;\n"
"}")
        self.HButton_1.setObjectName("HButton_1")
        self.HButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.HButton_3.setGeometry(QtCore.QRect(760, 330, 181, 101))
        self.HButton_3.setObjectName("HButton_3")
        self.HButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.HButton_4.setGeometry(QtCore.QRect(530, 330, 181, 101))
        self.HButton_4.setObjectName("HButton_4")
        self.HButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.HButton_2.setGeometry(QtCore.QRect(290, 330, 161, 101))
        self.HButton_2.setObjectName("HButton_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setGeometry(QtCore.QRect(-1, 599, 1081, 121))
        self.frame_9.setStyleSheet("QPushButton {\n"
"  border-radius: 10px;\n"
"  border: 2px solid black;\n"
"  padding: 10px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.HButton_6 = QtWidgets.QPushButton(self.frame_9)
        self.HButton_6.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.HButton_6.setObjectName("HButton_6")
        self.HButton_5 = QtWidgets.QPushButton(self.frame_9)
        self.HButton_5.setGeometry(QtCore.QRect(190, 10, 161, 101))
        self.HButton_5.setObjectName("HButton_5")
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Home_Page)
        self.History_Page = QtWidgets.QWidget()
        self.History_Page.setStyleSheet("background-color: #dddddd")
        self.History_Page.setObjectName("History_Page")
        self.frame_10 = QtWidgets.QFrame(self.History_Page)
        self.frame_10.setGeometry(QtCore.QRect(60, 40, 961, 651))
        self.frame_10.setStyleSheet("border-radius: 20px;\n"
"background-color: #F1F3F4\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(-1, -1, 961, 161))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_2 = QtWidgets.QLabel(self.frame_11)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 111, 21))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_10)
        self.tableWidget.setGeometry(QtCore.QRect(0, 160, 961, 491))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_5 = QtWidgets.QPushButton(self.History_Page)
        self.pushButton_5.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.History_Page)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 91, 31))
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.History_Page)
        self.Admin_Page = QtWidgets.QWidget()
        self.Admin_Page.setStyleSheet("background-color: grey")
        self.Admin_Page.setObjectName("Admin_Page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Admin_Page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_13 = QtWidgets.QFrame(self.Admin_Page)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_13)
        self.tabWidget.setGeometry(QtCore.QRect(0, 130, 1081, 591))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border: 1px solid #cccccc;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    width: 194px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.Appointment_List = QtWidgets.QWidget()
        self.Appointment_List.setObjectName("Appointment_List")
        self.label_9 = QtWidgets.QLabel(self.Appointment_List)
        self.label_9.setGeometry(QtCore.QRect(400, 30, 51, 41))
        self.label_9.setObjectName("label_9")
        self.pushButton_16 = QtWidgets.QPushButton(self.Appointment_List)
        self.pushButton_16.setGeometry(QtCore.QRect(710, 30, 220, 50))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.admin_view_appointments)
        self.lineEdit = QtWidgets.QLineEdit(self.Appointment_List)
        self.lineEdit.setGeometry(QtCore.QRect(510, 20, 191, 51))
        self.lineEdit.setStyleSheet("border-color: \"black\"")
        self.lineEdit.setObjectName("lineEdit")
        self.table_widget = QtWidgets.QTableWidget(self.Appointment_List)
        self.table_widget.setGeometry(QtCore.QRect(100, 90, 891, 431))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(7)
        self.table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(6, item)
        self.tabWidget.addTab(self.Appointment_List, "")
        self.User_Management = QtWidgets.QWidget()
        self.User_Management.setObjectName("User_Management")
        self.scrollArea = QtWidgets.QScrollArea(self.User_Management)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1071, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1069, 549))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setGeometry(QtCore.QRect(30, 390, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(200, 470, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_17.setGeometry(QtCore.QRect(600, 30, 231, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setGeometry(QtCore.QRect(30, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 110, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setGeometry(QtCore.QRect(540, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_27.setGeometry(QtCore.QRect(20, 470, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.pushButton_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_18.setGeometry(QtCore.QRect(750, 450, 231, 51))
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(200, 390, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 30, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(690, 110, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(200, 260, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_72 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_72.setGeometry(QtCore.QRect(30, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(200, 190, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_73 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_73.setGeometry(QtCore.QRect(30, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(690, 170, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_74 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_74.setGeometry(QtCore.QRect(540, 170, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(690, 230, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_75 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_75.setGeometry(QtCore.QRect(540, 230, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(200, 330, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_76 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_76.setGeometry(QtCore.QRect(30, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_24.setGeometry(QtCore.QRect(690, 290, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_77 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_77.setGeometry(QtCore.QRect(540, 290, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.User_Management, "")
        self.Report = QtWidgets.QWidget()
        self.Report.setObjectName("Report")
        self.label_19 = QtWidgets.QLabel(self.Report)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.Report)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 80, 721, 441))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.toolBox = QtWidgets.QToolBox(self.Report)
        self.toolBox.setGeometry(QtCore.QRect(790, 80, 241, 441))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 93, 128))
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_68 = QtWidgets.QPushButton(self.page)
        self.pushButton_68.setObjectName("pushButton_68")
        self.verticalLayout_2.addWidget(self.pushButton_68)
        self.pushButton_61 = QtWidgets.QPushButton(self.page)
        self.pushButton_61.setObjectName("pushButton_61")
        self.verticalLayout_2.addWidget(self.pushButton_61)
        self.pushButton_62 = QtWidgets.QPushButton(self.page)
        self.pushButton_62.setObjectName("pushButton_62")
        self.verticalLayout_2.addWidget(self.pushButton_62)
        self.pushButton_63 = QtWidgets.QPushButton(self.page)
        self.pushButton_63.setObjectName("pushButton_63")
        self.verticalLayout_2.addWidget(self.pushButton_63)
        self.toolBox.addItem(self.page, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 93, 128))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_67 = QtWidgets.QPushButton(self.widget)
        self.pushButton_67.setObjectName("pushButton_67")
        self.verticalLayout_4.addWidget(self.pushButton_67)
        self.pushButton_64 = QtWidgets.QPushButton(self.widget)
        self.pushButton_64.setObjectName("pushButton_64")
        self.verticalLayout_4.addWidget(self.pushButton_64)
        self.pushButton_65 = QtWidgets.QPushButton(self.widget)
        self.pushButton_65.setObjectName("pushButton_65")
        self.verticalLayout_4.addWidget(self.pushButton_65)
        self.pushButton_66 = QtWidgets.QPushButton(self.widget)
        self.pushButton_66.setObjectName("pushButton_66")
        self.verticalLayout_4.addWidget(self.pushButton_66)
        self.toolBox.addItem(self.widget, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 241, 360))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_74 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_74.setObjectName("pushButton_74")
        self.verticalLayout_5.addWidget(self.pushButton_74)
        self.pushButton_72 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_72.setObjectName("pushButton_72")
        self.verticalLayout_5.addWidget(self.pushButton_72)
        self.pushButton_75 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_75.setObjectName("pushButton_75")
        self.verticalLayout_5.addWidget(self.pushButton_75)
        self.pushButton_69 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_69.setObjectName("pushButton_69")
        self.verticalLayout_5.addWidget(self.pushButton_69)
        self.pushButton_73 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_73.setObjectName("pushButton_73")
        self.verticalLayout_5.addWidget(self.pushButton_73)
        self.pushButton_77 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_77.setObjectName("pushButton_77")
        self.verticalLayout_5.addWidget(self.pushButton_77)
        self.pushButton_76 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_76.setObjectName("pushButton_76")
        self.verticalLayout_5.addWidget(self.pushButton_76)
        self.pushButton_70 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_70.setObjectName("pushButton_70")
        self.verticalLayout_5.addWidget(self.pushButton_70)
        self.pushButton_71 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_71.setObjectName("pushButton_71")
        self.verticalLayout_5.addWidget(self.pushButton_71)
        self.toolBox.addItem(self.page_2, "")
        self.tabWidget.addTab(self.Report, "")
        self.Hospital_list = QtWidgets.QWidget()
        self.Hospital_list.setObjectName("Hospital_list")
        self.label_20 = QtWidgets.QLabel(self.Hospital_list)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.Hospital_list)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 40, 1071, 531))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.Hospital_list)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 480, 61, 51))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/tool.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_79 = QtWidgets.QPushButton(self.Hospital_list)
        self.pushButton_79.setGeometry(QtCore.QRect(920, 110, 93, 28))
        self.pushButton_79.setObjectName("pushButton_79")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Hospital_list)
        self.lineEdit_2.setGeometry(QtCore.QRect(720, 80, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.Hospital_list)
        self.lineEdit_7.setGeometry(QtCore.QRect(720, 150, 141, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_87 = QtWidgets.QLabel(self.Hospital_list)
        self.label_87.setGeometry(QtCore.QRect(720, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.Hospital_list)
        self.label_88.setGeometry(QtCore.QRect(720, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.Hospital_list)
        self.label_89.setGeometry(QtCore.QRect(720, 260, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.label_90 = QtWidgets.QLabel(self.Hospital_list)
        self.label_90.setGeometry(QtCore.QRect(720, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.Hospital_list)
        self.lineEdit_10.setGeometry(QtCore.QRect(720, 220, 141, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.Hospital_list)
        self.lineEdit_25.setGeometry(QtCore.QRect(720, 290, 141, 31))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.tabWidget.addTab(self.Hospital_list, "")
        self.frame_12 = QtWidgets.QFrame(self.frame_13)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 1081, 131))
        self.frame_12.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:1, stop:0.570621 rgba(46, 46, 46, 255), stop:1 rgba(109, 109, 109, 255));")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_18 = QtWidgets.QLabel(self.frame_12)
        self.label_18.setGeometry(QtCore.QRect(30, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgba(46, 46, 46, 255)")
        self.label_18.setObjectName("label_18")
        self.HButton_9 = QtWidgets.QPushButton(self.frame_12)
        self.HButton_9.setGeometry(QtCore.QRect(970, 0, 111, 41))
        self.HButton_9.setObjectName("HButton_9")
        self.verticalLayout_3.addWidget(self.frame_13)
        self.stackedWidget.addWidget(self.Admin_Page)
        self.Hospital_User = QtWidgets.QWidget()
        self.Hospital_User.setObjectName("Hospital_User")
        self.frame_18 = QtWidgets.QFrame(self.Hospital_User)
        self.frame_18.setGeometry(QtCore.QRect(0, 0, 1080, 713))
        self.frame_18.setStyleSheet("background-color:grey")
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setGeometry(QtCore.QRect(0, 0, 1081, 141))
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_16 = QtWidgets.QLabel(self.frame_19)
        self.label_16.setGeometry(QtCore.QRect(20, 0, 621, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_16.setObjectName("label_16")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_3.setGeometry(QtCore.QRect(950, 0, 91, 31))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_18)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 150, 1071, 531))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.pushButton_15 = QtWidgets.QPushButton(self.Hospital_User)
        self.pushButton_15.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_15.setObjectName("pushButton_15")
        self.stackedWidget.addWidget(self.Hospital_User)
        self.InfoPage = QtWidgets.QWidget()
        self.InfoPage.setObjectName("InfoPage")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.InfoPage)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 150, 1081, 571))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Aboutus = QtWidgets.QWidget()
        self.Aboutus.setObjectName("Aboutus")
        self.frame_39 = QtWidgets.QFrame(self.Aboutus)
        self.frame_39.setGeometry(QtCore.QRect(0, 0, 1081, 541))
        self.frame_39.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_39.setObjectName("frame_39")
        self.frame_40 = QtWidgets.QFrame(self.frame_39)
        self.frame_40.setGeometry(QtCore.QRect(10, 10, 511, 211))
        self.frame_40.setStyleSheet("image: url(:/Poster/sdp/blood.jpg);")
        self.frame_40.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_40.setObjectName("frame_40")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_39)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 250, 501, 121))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_39)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 390, 501, 141))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_39)
        self.textBrowser_4.setGeometry(QtCore.QRect(540, 20, 511, 171))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_39)
        self.textBrowser_5.setGeometry(QtCore.QRect(540, 220, 511, 151))
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.frame_39)
        self.textBrowser_6.setGeometry(QtCore.QRect(540, 390, 511, 141))
        self.textBrowser_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.tabWidget_2.addTab(self.Aboutus, "")
        self.Rewards = QtWidgets.QWidget()
        self.Rewards.setObjectName("Rewards")
        self.label_31 = QtWidgets.QLabel(self.Rewards)
        self.label_31.setGeometry(QtCore.QRect(440, 60, 241, 221))
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.pushButton_19 = QtWidgets.QPushButton(self.Rewards)
        self.pushButton_19.setGeometry(QtCore.QRect(440, 330, 241, 101))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_32 = QtWidgets.QLabel(self.Rewards)
        self.label_32.setGeometry(QtCore.QRect(50, 40, 350, 450))
        self.label_32.setObjectName("label_32")
        self.tabWidget_2.addTab(self.Rewards, "")
        self.drawing_process = QtWidgets.QWidget()
        self.drawing_process.setObjectName("drawing_process")
        self.frame_37 = QtWidgets.QFrame(self.drawing_process)
        self.frame_37.setGeometry(QtCore.QRect(0, 0, 1081, 61))
        self.frame_37.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_37.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_37.setObjectName("frame_37")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.frame_37)
        self.textBrowser_7.setGeometry(QtCore.QRect(0, 0, 1071, 51))
        self.textBrowser_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.477273 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.textBrowser_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textBrowser_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.frame_38 = QtWidgets.QFrame(self.drawing_process)
        self.frame_38.setGeometry(QtCore.QRect(-1, 60, 1081, 481))
        self.frame_38.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_38.setObjectName("frame_38")
        self.frame_48 = QtWidgets.QFrame(self.frame_38)
        self.frame_48.setGeometry(QtCore.QRect(10, 10, 511, 171))
        self.frame_48.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_48.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_48.setObjectName("frame_48")
        self.label_53 = QtWidgets.QLabel(self.frame_48)
        self.label_53.setGeometry(QtCore.QRect(20, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.frame_48)
        self.textBrowser_9.setGeometry(QtCore.QRect(15, 40, 491, 131))
        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.frame_50 = QtWidgets.QFrame(self.frame_38)
        self.frame_50.setGeometry(QtCore.QRect(10, 190, 511, 281))
        self.frame_50.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_50.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_50.setObjectName("frame_50")
        self.label_54 = QtWidgets.QLabel(self.frame_50)
        self.label_54.setGeometry(QtCore.QRect(10, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.frame_50)
        self.textBrowser_10.setGeometry(QtCore.QRect(10, 40, 501, 261))
        self.textBrowser_10.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.frame_49 = QtWidgets.QFrame(self.frame_38)
        self.frame_49.setGeometry(QtCore.QRect(540, 10, 521, 171))
        self.frame_49.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_49.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_49.setObjectName("frame_49")
        self.label_55 = QtWidgets.QLabel(self.frame_49)
        self.label_55.setGeometry(QtCore.QRect(10, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.frame_49)
        self.textBrowser_11.setGeometry(QtCore.QRect(10, 40, 501, 131))
        self.textBrowser_11.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.frame_51 = QtWidgets.QFrame(self.frame_38)
        self.frame_51.setGeometry(QtCore.QRect(540, 190, 521, 281))
        self.frame_51.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_51.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_51.setObjectName("frame_51")
        self.label_56 = QtWidgets.QLabel(self.frame_51)
        self.label_56.setGeometry(QtCore.QRect(10, 10, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.frame_51)
        self.textBrowser_12.setGeometry(QtCore.QRect(15, 41, 501, 161))
        self.textBrowser_12.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.tabWidget_2.addTab(self.drawing_process, "")
        self.Faq = QtWidgets.QWidget()
        self.Faq.setObjectName("Faq")
        self.label_28 = QtWidgets.QLabel(self.Faq)
        self.label_28.setGeometry(QtCore.QRect(10, 0, 891, 401))
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.line = QtWidgets.QFrame(self.Faq)
        self.line.setGeometry(QtCore.QRect(0, 390, 1071, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_29 = QtWidgets.QLabel(self.Faq)
        self.label_29.setGeometry(QtCore.QRect(10, 400, 531, 121))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.Faq)
        self.label_30.setGeometry(QtCore.QRect(540, 400, 531, 121))
        self.label_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.tabWidget_2.addTab(self.Faq, "")
        self.frame_21 = QtWidgets.QFrame(self.InfoPage)
        self.frame_21.setGeometry(QtCore.QRect(0, 0, 1081, 181))
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName("frame_21")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_20.setGeometry(QtCore.QRect(950, 0, 91, 31))
        self.pushButton_20.setIcon(icon1)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_21.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon)
        self.pushButton_21.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_21.setObjectName("pushButton_21")
        self.frame_21.raise_()
        self.tabWidget_2.raise_()
        self.stackedWidget.addWidget(self.InfoPage)
        self.BloodDonationPage = QtWidgets.QWidget()
        self.BloodDonationPage.setObjectName("BloodDonationPage")
        self.frame_41 = QtWidgets.QFrame(self.BloodDonationPage)
        self.frame_41.setGeometry(QtCore.QRect(10, 10, 1061, 121))
        self.frame_41.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_41.setObjectName("frame_41")
        self.label_48 = QtWidgets.QLabel(self.frame_41)
        self.label_48.setGeometry(QtCore.QRect(10, 10, 711, 101))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(48)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_41)
        self.pushButton_58.setGeometry(QtCore.QRect(940, -10, 91, 31))
        self.pushButton_58.setIcon(icon1)
        self.pushButton_58.setObjectName("pushButton_58")
        self.frame_42 = QtWidgets.QFrame(self.BloodDonationPage)
        self.frame_42.setGeometry(QtCore.QRect(9, 139, 1061, 571))
        self.frame_42.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_42.setObjectName("frame_42")
        self.pushButton_55 = QtWidgets.QPushButton(self.frame_42)
        self.pushButton_55.setGeometry(QtCore.QRect(900, 490, 131, 61))
        self.pushButton_55.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_55.setObjectName("pushButton_55")
        self.label_49 = QtWidgets.QLabel(self.frame_42)
        self.label_49.setGeometry(QtCore.QRect(20, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_15.setGeometry(QtCore.QRect(20, 70, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_50 = QtWidgets.QLabel(self.frame_42)
        self.label_50.setGeometry(QtCore.QRect(20, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 170, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_51 = QtWidgets.QLabel(self.frame_42)
        self.label_51.setGeometry(QtCore.QRect(20, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_17.setGeometry(QtCore.QRect(20, 280, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_52 = QtWidgets.QLabel(self.frame_42)
        self.label_52.setGeometry(QtCore.QRect(20, 340, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.comboBox = QtWidgets.QComboBox(self.frame_42)
        self.comboBox.setGeometry(QtCore.QRect(20, 380, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_91 = QtWidgets.QLabel(self.frame_42)
        self.label_91.setGeometry(QtCore.QRect(460, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_26.setGeometry(QtCore.QRect(460, 70, 361, 31))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.pushButton_56 = QtWidgets.QPushButton(self.BloodDonationPage)
        self.pushButton_56.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_56.setText("")
        self.pushButton_56.setIcon(icon)
        self.pushButton_56.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_56.setObjectName("pushButton_56")
        self.stackedWidget.addWidget(self.BloodDonationPage)
        self.Feedback = QtWidgets.QWidget()
        self.Feedback.setObjectName("Feedback")
        self.frame_15 = QtWidgets.QFrame(self.Feedback)
        self.frame_15.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.frame_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.477273 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_22 = QtWidgets.QFrame(self.frame_15)
        self.frame_22.setGeometry(QtCore.QRect(9, 9, 521, 301))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        self.frame_22.setFont(font)
        self.frame_22.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_6 = QtWidgets.QLabel(self.frame_22)
        self.label_6.setGeometry(QtCore.QRect(0, 1, 525, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(30, 89, 165);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        self.frame_23.setGeometry(QtCore.QRect(3, 59, 511, 231))
        self.frame_23.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_23.setObjectName("frame_23")
        self.label_7 = QtWidgets.QLabel(self.frame_23)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(30, 89, 165);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_23)
        self.textBrowser.setGeometry(QtCore.QRect(0, 51, 511, 171))
        font = QtGui.QFont()
        font.setFamily("STKaiti")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.477273 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.frame_24 = QtWidgets.QFrame(self.frame_15)
        self.frame_24.setGeometry(QtCore.QRect(9, 319, 521, 51))
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_24.setObjectName("frame_24")
        self.label_17 = QtWidgets.QLabel(self.frame_24)
        self.label_17.setGeometry(QtCore.QRect(6, 9, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.frame_25 = QtWidgets.QFrame(self.frame_15)
        self.frame_25.setGeometry(QtCore.QRect(10, 380, 521, 51))
        self.frame_25.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_33 = QtWidgets.QLabel(self.frame_25)
        self.label_33.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_33.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_22.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_23.setGeometry(QtCore.QRect(120, 10, 31, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_24.setGeometry(QtCore.QRect(160, 10, 31, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_25.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_26.setGeometry(QtCore.QRect(240, 10, 31, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_34 = QtWidgets.QLabel(self.frame_25)
        self.label_34.setGeometry(QtCore.QRect(290, 10, 31, 31))
        self.label_34.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.frame_26 = QtWidgets.QFrame(self.frame_15)
        self.frame_26.setGeometry(QtCore.QRect(10, 440, 521, 51))
        self.frame_26.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_26.setObjectName("frame_26")
        self.label_35 = QtWidgets.QLabel(self.frame_26)
        self.label_35.setGeometry(QtCore.QRect(6, 9, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.frame_27 = QtWidgets.QFrame(self.frame_15)
        self.frame_27.setGeometry(QtCore.QRect(11, 500, 521, 51))
        self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_27.setObjectName("frame_27")
        self.label_36 = QtWidgets.QLabel(self.frame_27)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 51, 31))
        self.label_36.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_27.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_28.setGeometry(QtCore.QRect(120, 10, 31, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_29.setGeometry(QtCore.QRect(160, 10, 31, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_30.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_31.setGeometry(QtCore.QRect(240, 10, 31, 31))
        self.pushButton_31.setObjectName("pushButton_31")
        self.label_37 = QtWidgets.QLabel(self.frame_27)
        self.label_37.setGeometry(QtCore.QRect(290, 10, 31, 31))
        self.label_37.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.frame_28 = QtWidgets.QFrame(self.frame_15)
        self.frame_28.setGeometry(QtCore.QRect(10, 610, 521, 51))
        self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_28.setObjectName("frame_28")
        self.label_38 = QtWidgets.QLabel(self.frame_28)
        self.label_38.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_38.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_32.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_33.setGeometry(QtCore.QRect(130, 10, 31, 31))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_34.setGeometry(QtCore.QRect(170, 10, 31, 31))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_35.setGeometry(QtCore.QRect(210, 10, 31, 31))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_36.setGeometry(QtCore.QRect(250, 10, 31, 31))
        self.pushButton_36.setObjectName("pushButton_36")
        self.label_39 = QtWidgets.QLabel(self.frame_28)
        self.label_39.setGeometry(QtCore.QRect(290, 10, 31, 31))
        self.label_39.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.frame_29 = QtWidgets.QFrame(self.frame_15)
        self.frame_29.setGeometry(QtCore.QRect(10, 550, 521, 51))
        self.frame_29.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_29.setObjectName("frame_29")
        self.label_40 = QtWidgets.QLabel(self.frame_29)
        self.label_40.setGeometry(QtCore.QRect(6, 9, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.frame_30 = QtWidgets.QFrame(self.frame_15)
        self.frame_30.setGeometry(QtCore.QRect(540, 150, 521, 71))
        self.frame_30.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_30.setObjectName("frame_30")
        self.label_41 = QtWidgets.QLabel(self.frame_30)
        self.label_41.setGeometry(QtCore.QRect(6, 9, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(16)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.frame_31 = QtWidgets.QFrame(self.frame_15)
        self.frame_31.setGeometry(QtCore.QRect(540, 230, 521, 51))
        self.frame_31.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_31.setObjectName("frame_31")
        self.label_42 = QtWidgets.QLabel(self.frame_31)
        self.label_42.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_42.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_37.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_38.setGeometry(QtCore.QRect(120, 10, 31, 31))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_39.setGeometry(QtCore.QRect(160, 10, 31, 31))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_40.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_41.setGeometry(QtCore.QRect(240, 10, 31, 31))
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_43 = QtWidgets.QLabel(self.frame_31)
        self.label_43.setGeometry(QtCore.QRect(280, 10, 31, 31))
        self.label_43.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.frame_32 = QtWidgets.QFrame(self.frame_15)
        self.frame_32.setGeometry(QtCore.QRect(540, 290, 521, 71))
        self.frame_32.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_32.setObjectName("frame_32")
        self.label_44 = QtWidgets.QLabel(self.frame_32)
        self.label_44.setGeometry(QtCore.QRect(6, 9, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(14)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.frame_33 = QtWidgets.QFrame(self.frame_15)
        self.frame_33.setGeometry(QtCore.QRect(540, 370, 521, 51))
        self.frame_33.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_33.setObjectName("frame_33")
        self.label_45 = QtWidgets.QLabel(self.frame_33)
        self.label_45.setGeometry(QtCore.QRect(20, 10, 51, 31))
        self.label_45.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_42.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_43.setGeometry(QtCore.QRect(120, 10, 31, 31))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_44.setGeometry(QtCore.QRect(160, 10, 31, 31))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_45.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_46.setGeometry(QtCore.QRect(240, 10, 31, 31))
        self.pushButton_46.setObjectName("pushButton_46")
        self.label_46 = QtWidgets.QLabel(self.frame_33)
        self.label_46.setGeometry(QtCore.QRect(280, 10, 31, 31))
        self.label_46.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.frame_34 = QtWidgets.QFrame(self.frame_15)
        self.frame_34.setGeometry(QtCore.QRect(540, 430, 521, 71))
        self.frame_34.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_34.setObjectName("frame_34")
        self.label_47 = QtWidgets.QLabel(self.frame_34)
        self.label_47.setGeometry(QtCore.QRect(6, 9, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.frame_35 = QtWidgets.QFrame(self.frame_15)
        self.frame_35.setGeometry(QtCore.QRect(540, 509, 521, 131))
        self.frame_35.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_35.setObjectName("frame_35")
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame_35)
        self.textEdit_6.setGeometry(QtCore.QRect(3, 3, 511, 121))
        self.textEdit_6.setObjectName("textEdit_6")
        self.frame_36 = QtWidgets.QFrame(self.frame_15)
        self.frame_36.setGeometry(QtCore.QRect(540, 650, 521, 61))
        self.frame_36.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_36.setObjectName("frame_36")
        self.pushButton_47 = QtWidgets.QPushButton(self.frame_36)
        self.pushButton_47.setGeometry(QtCore.QRect(0, 10, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("background-color: rgb(30, 89, 165);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_57 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_57.setGeometry(QtCore.QRect(1040, 0, 41, 31))
        self.pushButton_57.setText("")
        self.pushButton_57.setIcon(icon)
        self.pushButton_57.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_59 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_59.setGeometry(QtCore.QRect(950, 0, 91, 31))
        self.pushButton_59.setIcon(icon1)
        self.pushButton_59.setObjectName("pushButton_59")
        self.stackedWidget.addWidget(self.Feedback)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("background-color: #199ce6")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Icons/user.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 28, 24))
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_48 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_48.setGeometry(QtCore.QRect(10, 190, 171, 71))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_49.setGeometry(QtCore.QRect(10, 80, 171, 81))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_50.setGeometry(QtCore.QRect(10, 290, 171, 81))
        self.pushButton_50.setObjectName("pushButton_50")
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_51 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_51.setGeometry(QtCore.QRect(20, 90, 131, 23))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_52.setGeometry(QtCore.QRect(20, 120, 131, 23))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_53.setGeometry(QtCore.QRect(20, 60, 131, 23))
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_54.setGeometry(QtCore.QRect(20, 30, 131, 23))
        self.pushButton_54.setObjectName("pushButton_54")
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "Sign Up/Register"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.pushButton_11.setText(_translate("MainWindow", "Register"))
        self.pushButton_12.setText(_translate("MainWindow", "Login"))
        self.label_12.setText(_translate("MainWindow", "Fishy\'s Blood Donation"))
        self.label_14.setText(_translate("MainWindow", "Login"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_13.setText(_translate("MainWindow", "Login"))
        self.pushButton_14.setText(_translate("MainWindow", "Not registered? Register Now!"))
        self.label_15.setText(_translate("MainWindow", "Fishy's Donation"))
        self.pushButton_8.setText(_translate("MainWindow", "Edit Profile"))
        self.label_8.setText(_translate("MainWindow", "USER INFO"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name</p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email</p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mobile Number</p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Password</p></body></html>"))
        self.label_58.setText(_translate("MainWindow", "USER RECORD"))
        self.textEdit_5.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gender</p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Age</p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Blood Type</p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Disease</p></body></html>"))
        self.textEdit_10.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Diagnosis</p></body></html>"))
        self.textEdit_11.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Medication</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Profile"))
        self.pushButton_7.setText(_translate("MainWindow", "Home Page"))
        self.label.setText(_translate("MainWindow", "Profile"))
        self.label_25.setText(_translate("MainWindow", "Name:"))
        self.label_78.setText(_translate("MainWindow", "Mobile Number:"))
        self.label_79.setText(_translate("MainWindow", "Email:"))
        self.label_80.setText(_translate("MainWindow", "Password:"))
        self.label_81.setText(_translate("MainWindow", "Gender:"))
        self.label_82.setText(_translate("MainWindow", "Age:"))
        self.label_83.setText(_translate("MainWindow", "Blood Type:"))
        self.label_84.setText(_translate("MainWindow", "Disease:"))
        self.label_85.setText(_translate("MainWindow", "Diagnosis:"))
        self.label_86.setText(_translate("MainWindow", "Medication:"))
        self.label_5.setText(_translate("MainWindow", "Rewards Available"))
        self.pushButton_9.setText(_translate("MainWindow", "Home Page"))
        self.label_59.setText(_translate("MainWindow", "First Donation"))
        self.label_65.setText(_translate("MainWindow", "Donor Plaque"))
        self.label_60.setText(_translate("MainWindow", "Tenth Donation"))
        self.label_67.setText(_translate("MainWindow", "Gift Card RM 10 & Double Chocolate Cookies"))
        self.label_61.setText(_translate("MainWindow", "50th Donation"))
        self.label_69.setText(_translate("MainWindow", "Gift Card RM 50 & Free Consultation"))
        self.label_62.setText(_translate("MainWindow", "Fifth Donation"))
        self.label_66.setText(_translate("MainWindow", "Gift card RM 5"))
        self.label_63.setText(_translate("MainWindow", "25th Donation"))
        self.label_68.setText(_translate("MainWindow", "Gift Card RM 25 & Termal Flask"))
        self.label_64.setText(_translate("MainWindow", "100th Donation"))
        self.label_70.setText(_translate("MainWindow", "Spin the Wheel to stand a chance to win a proton saga"))
        self.label_57.setText(_translate("MainWindow", "Rewards Milestones"))
        self.label_71.setText(_translate("MainWindow", "Your Donations:"))
        self.Hlabel_1.setText(_translate("MainWindow", "Home Page"))
        self.Hlabel_2.setText(_translate("MainWindow", "Fishy\'s Blood Donation"))
        self.HButton_7.setText(_translate("MainWindow", "Log out"))
        self.HButton_1.setText(_translate("MainWindow", "Donate Today"))
        self.HButton_3.setText(_translate("MainWindow", "Donation Hitory"))
        self.HButton_4.setText(_translate("MainWindow", "Hospitals List"))
        self.HButton_2.setText(_translate("MainWindow", "Donation Rewards"))
        self.HButton_6.setText(_translate("MainWindow", "Leave a Feedback"))
        self.HButton_5.setText(_translate("MainWindow", "Know more About Us"))
        self.label_2.setText(_translate("MainWindow", "History"))
        self.label_4.setText(_translate("MainWindow", "Previous Donations"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Appointment ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DonationType"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "BloodType"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        self.pushButton_2.setText(_translate("MainWindow", "Home Page"))
        self.label_21.setText(_translate("MainWindow", "ID: "))
        self.label_9.setText(_translate("MainWindow", "Name: "))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Appointment ID"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username "))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hospital ID"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Donation type"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Blood type"))
        item = self.table_widget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))
        item = self.table_widget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Time"))
        self.pushButton_16.setText(_translate("MainWindow", "View Appointments"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Appointment_List), _translate("MainWindow", "User Appointments"))
        self.label_26.setText(_translate("MainWindow", "Email:"))
        self.pushButton_17.setText(_translate("MainWindow", "Show Info"))
        self.label_22.setText(_translate("MainWindow", "Username:"))
        self.label_24.setText(_translate("MainWindow", "Name:"))
        self.label_21.setText(_translate("MainWindow", "Blood Type:"))
        self.label_27.setText(_translate("MainWindow", "Telephone:"))
        self.pushButton_18.setText(_translate("MainWindow", "Update Info"))
        self.label_72.setText(_translate("MainWindow", "Age:"))
        self.label_73.setText(_translate("MainWindow", "<html><head/><body><p>Gender:</p></body></html>"))
        self.label_74.setText(_translate("MainWindow", "Dieseases:"))
        self.label_75.setText(_translate("MainWindow", "Medication:"))
        self.label_76.setText(_translate("MainWindow", "Address:"))
        self.label_77.setText(_translate("MainWindow", "Diagnosis:"))
        self.pushButton_17.setText(_translate("MainWindow", "Show Info"))
        self.pushButton_18.setText(_translate("MainWindow", "Update Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.User_Management), _translate("MainWindow", "Admin User management"))
        self.label_19.setText(_translate("MainWindow", "Donations Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Report), _translate("MainWindow", "Report Generation"))
        self.label_20.setText(_translate("MainWindow", "Hospital List"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hospital Name"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hospital ID"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address"))
        self.pushButton_79.setText(_translate("MainWindow", "ADD"))
        self.label_87.setText(_translate("MainWindow", "Hospital Name"))
        self.label_88.setText(_translate("MainWindow", "City"))
        self.label_89.setText(_translate("MainWindow", "Address"))
        self.label_90.setText(_translate("MainWindow", "HospitalID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hospital_list), _translate("MainWindow", "Manage hospital List"))
        self.label_18.setText(_translate("MainWindow", "Admin Panel"))
        self.HButton_9.setText(_translate("MainWindow", "Log out"))
        self.label_16.setText(_translate("MainWindow", "Hospital Location"))
        self.pushButton_3.setText(_translate("MainWindow", "Home Page"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hospital Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hospital ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">The first recorded instance of blood transfusion dates back to ancient Greece, where physicians attempted to treat patients by using animal blood. However, these early attempts at transfusion were largely unsuccessful due to the lack of knowledge about blood types and the risks of infection.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">In the 17th century, the English physician William Harvey discovered the circulation of blood in the human body, laying the groundwork for the development of modern blood transfusion. In 1818, the first successful human-to-human blood transfusion was performed by British physician James Blundell, who used the patient\'s husband as a donor.</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Despite the early successes of blood transfusion, the practice remained risky and unpredictable until the early 20th century when the discovery of blood types and the development of safe transfusion techniques revolutionized the field. In 1901, the Austrian physician Karl Landsteiner discovered the ABO blood group system, which remains the basis for modern blood typing.</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">During World War II, the demand for blood transfusions increased dramatically, leading to the development of large-scale blood donation programs. In the United States, the American Red Cross played a crucial role in organizing blood drives and ensuring a steady supply of blood for the military and civilians alike.</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Today, blood donation continues to be an essential part of modern medicine, with millions of people around the world donating blood every year. In addition to providing a lifeline for patients in need of transfusions, blood donation also plays a vital role in medical research and the development of new treatments for a wide range of illnesses and diseases.</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Aboutus), _translate("MainWindow", "About us"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">We reward people who contribute regularly, saving more lives than one might think. With our rewards program, regular donors will enjoy many more benefits for free that you can find out below!</span></p></body></html>"))
        self.pushButton_19.setText(_translate("MainWindow", "Learn more!"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Poster/Membership Poster 350x450.png\"/></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Rewards), _translate("MainWindow", "Rewards"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,Arial,Helvetica Neue,Helvetica,sans-serif\'; font-size:18pt; color:#000000; background-color:#ffffff;\">The blood donation process from the time you arrive until the time you leave takes about an hour. The donation itself is only about 8-10 minutes on average.</span></p></body></html>"))
        self.label_53.setText(_translate("MainWindow", "Registration"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">We’ll sign you in and go over basic eligibility.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">You’ll be asked to show ID, such as your driver’s license.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">You’ll read some information about donating blood.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">We’ll ask you for your complete address.  Your address needs to be complete (including PO Box, street/apartment number) and the place where you will receive your mail 8 weeks from donation.</span></p></body></html>"))
        self.label_54.setText(_translate("MainWindow", "Your Donation"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:16pt; font-weight:296; color:#0a0a09;\">You’ll answer a few questions about your health history and places you’ve traveled, during a private and confidential interview.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:16pt; font-weight:296; color:#0a0a09;\">You’ll tell us about any prescription and/or over the counter medications that may be iYou’ll answer a few questions about your health history and places you’ve traveled, during a private and confidential interview.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:16pt; font-weight:296; color:#0a0a09;\">You’ll tell us about any prescription and/or over the counter medications that may be in your system.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:16pt; font-weight:296; color:#0a0a09;\">We’ll check your temperature, pulse, blood pressure and hemoglobin level.n your system.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:16pt; font-weight:296; color:#0a0a09;\">We’ll check your temperature, pulse, blood pressure and hemoglobin level.</span></p></body></html>"))
        self.label_55.setText(_translate("MainWindow", "Health History"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">You’ll answer a few questions about your health history and places you’ve traveled, during a private and confidential interview.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">You’ll tell us about any prescription and/or over the counter medications that may be in your system.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">We’ll check your temperature, pulse, blood pressure and hemoglobin level.</span></p></body></html>"))
        self.label_56.setText(_translate("MainWindow", "Refreshment and Recovery"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">After donating blood, you’ll have a snack and something to drink in the refreshment area.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">You’ll leave after 10-15 minutes and continue your normal routine.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Enjoy the feeling of accomplishment knowing you are helping to save lives.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Take a selfie, or simply share your good deed with friends. It may inspire them to become blood donors.</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.drawing_process), _translate("MainWindow", "Blood Drawing Process"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Q: What is a blood donation?</span></p><p><span style=\" font-size:12pt;\">A: Blood donation is the process of voluntarily giving blood to a blood bank or blood donation organization, who will then use the blood to save lives.</span></p><p><br/></p><p><span style=\" font-size:12pt;\">Q: Who can donate blood? </span></p><p><span style=\" font-size:12pt;\">A: Anyone who is healthy, and over 17 years old (unless with parental consent).</span></p><p><br/></p><p><span style=\" font-size:12pt;\">Q: Can I donate blood if I have received a COVID-19 vaccine? A: Yes, most individuals who have received a COVID-19 vaccine are still eligible to donate blood, although there may be a waiting period depending on the type of vaccine and the organization\'s guidelines. It\'s best to check with the blood donation organization for specific guidance.</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Telphone 1: 012-393-1348</span></p><p><span style=\" font-size:12pt;\">Telephone 2: 011-209-4897</span></p><p><span style=\" font-size:12pt;\">Emergency hospital line: 988</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Email: BlooodDonation@hospital.mail.com</span></p><p><span style=\" font-size:12pt;\">Instagram: @BloodDono</span></p><p><span style=\" font-size:12pt;\">Twitter: @BloodDono</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Faq), _translate("MainWindow", "FAQ"))
        self.pushButton_20.setText(_translate("MainWindow", "Home Page"))
        self.label_48.setText(_translate("MainWindow", "BLOOD DONATION PAGE"))
        self.pushButton_58.setText(_translate("MainWindow", "Home Page"))
        self.pushButton_55.setText(_translate("MainWindow", "SUBMIT"))
        self.label_49.setText(_translate("MainWindow", "Date"))
        self.label_50.setText(_translate("MainWindow", "Time"))
        self.label_51.setText(_translate("MainWindow", "Hospital"))
        self.label_52.setText(_translate("MainWindow", "Donation Type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Blood Plasma"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Platelet"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Blood"))
        self.label_91.setText(_translate("MainWindow", "Blood Type"))
        self.label_6.setText(_translate("MainWindow", "Feedback"))
        self.label_7.setText(_translate("MainWindow", "We would love to receive your feedback!"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'STKaiti\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#1e59a5;\">Our goal is to create a platform that makes it easier for users to donate blood.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#1e59a5;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#1e59a5;\">After you\'ve used the app, we want to know what you think of it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#1e59a5;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#1e59a5;\">We appreciate getting your feedback, thank you!</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "I can easily find the function I want."))
        self.label_33.setText(_translate("MainWindow", "Disagree"))
        self.pushButton_22.setText(_translate("MainWindow", "1"))
        self.pushButton_23.setText(_translate("MainWindow", "2"))
        self.pushButton_24.setText(_translate("MainWindow", "3"))
        self.pushButton_25.setText(_translate("MainWindow", "4"))
        self.pushButton_26.setText(_translate("MainWindow", "5"))
        self.label_34.setText(_translate("MainWindow", "Agree"))
        self.label_35.setText(_translate("MainWindow", "I think my privacy is well protected."))
        self.label_36.setText(_translate("MainWindow", "Disagree"))
        self.pushButton_27.setText(_translate("MainWindow", "1"))
        self.pushButton_28.setText(_translate("MainWindow", "2"))
        self.pushButton_29.setText(_translate("MainWindow", "3"))
        self.pushButton_30.setText(_translate("MainWindow", "4"))
        self.pushButton_31.setText(_translate("MainWindow", "5"))
        self.label_37.setText(_translate("MainWindow", "Agree"))
        self.label_38.setText(_translate("MainWindow", "Disagree"))
        self.pushButton_32.setText(_translate("MainWindow", "1"))
        self.pushButton_33.setText(_translate("MainWindow", "2"))
        self.pushButton_34.setText(_translate("MainWindow", "3"))
        self.pushButton_35.setText(_translate("MainWindow", "4"))
        self.pushButton_36.setText(_translate("MainWindow", "5"))
        self.label_39.setText(_translate("MainWindow", "Agree"))
        self.label_40.setText(_translate("MainWindow", "This platform is easy to use."))
        self.label_41.setText(_translate("MainWindow", "Is the user interface easy to navigate and visually \n"
" appealing?"))
        self.label_42.setText(_translate("MainWindow", "Disagree"))
        self.pushButton_37.setText(_translate("MainWindow", "1"))
        self.pushButton_38.setText(_translate("MainWindow", "2"))
        self.pushButton_39.setText(_translate("MainWindow", "3"))
        self.pushButton_40.setText(_translate("MainWindow", "4"))
        self.pushButton_41.setText(_translate("MainWindow", "5"))
        self.label_43.setText(_translate("MainWindow", "Agree"))
        self.label_44.setText(_translate("MainWindow", "Is the process of updating your personal information and blood type in your user profile simple and \n"
" straightforward?"))
        self.label_45.setText(_translate("MainWindow", "Disagree"))
        self.pushButton_42.setText(_translate("MainWindow", "1"))
        self.pushButton_43.setText(_translate("MainWindow", "2"))
        self.pushButton_44.setText(_translate("MainWindow", "3"))
        self.pushButton_45.setText(_translate("MainWindow", "4"))
        self.pushButton_46.setText(_translate("MainWindow", "5"))
        self.label_46.setText(_translate("MainWindow", "Agree"))
        self.label_47.setText(_translate("MainWindow", "Are there any features or functions that you would like \n"
" the application to have but do not?"))
        self.pushButton_47.setText(_translate("MainWindow", "Submit"))
        self.pushButton_59.setText(_translate("MainWindow", "Home Page"))
        self.pushButton_48.setText(_translate("MainWindow", "History"))
        self.pushButton_49.setText(_translate("MainWindow", "Profile"))
        self.pushButton_50.setText(_translate("MainWindow", "Hospitals Available."))
        self.pushButton_51.setText(_translate("MainWindow", "Leave A Feed back"))
        self.pushButton_52.setText(_translate("MainWindow", "Log out?"))
        self.pushButton_53.setText(_translate("MainWindow", "More About us!"))
        self.pushButton_54.setText(_translate("MainWindow", "Rewards"))
        self.pushButton_68.setText(_translate("MainWindow", "Any"))
        self.pushButton_61.setText(_translate("MainWindow", "Hospital A"))
        self.pushButton_62.setText(_translate("MainWindow", "Hospital B"))
        self.pushButton_63.setText(_translate("MainWindow", "Hospital C"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Hospitals"))
        self.pushButton_67.setText(_translate("MainWindow", "Any"))
        self.pushButton_64.setText(_translate("MainWindow", "Blood"))
        self.pushButton_65.setText(_translate("MainWindow", "Plasma"))
        self.pushButton_66.setText(_translate("MainWindow", "platelet"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), _translate("MainWindow", "Donation Type"))
        self.pushButton_74.setText(_translate("MainWindow", "Any"))
        self.pushButton_72.setText(_translate("MainWindow", "O+"))
        self.pushButton_75.setText(_translate("MainWindow", "O-"))
        self.pushButton_69.setText(_translate("MainWindow", "A+"))
        self.pushButton_73.setText(_translate("MainWindow", "A-"))
        self.pushButton_77.setText(_translate("MainWindow", "B+"))
        self.pushButton_76.setText(_translate("MainWindow", "B-"))
        self.pushButton_70.setText(_translate("MainWindow", "AB+"))
        self.pushButton_71.setText(_translate("MainWindow", "AB-"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Blood Type"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Report), _translate("MainWindow", "Report Generation"))
        self.value = None
        self.value_2 = None
        self.value_3 = None

        #Item Attribute Change
        self.tableWidget.setColumnWidth(0, 175)
        self.tableWidget.setColumnWidth(1, 175)
        self.tableWidget.setColumnWidth(2, 175)
        self.tableWidget.setColumnWidth(3, 175)
        self.tableWidget.setColumnWidth(4, 175)

        self.tableWidget_2.setColumnWidth(0, 200)
        self.tableWidget_2.setColumnWidth(1, 200)
        self.tableWidget_2.setColumnWidth(2, 200)
        self.tableWidget_2.setColumnWidth(3, 200)

        self.tableWidget_3.setColumnWidth(0, 175)
        self.tableWidget_3.setColumnWidth(1, 175)
        self.tableWidget_3.setColumnWidth(2, 175)
        self.tableWidget_3.setColumnWidth(3, 175)

        #Initialise Functions
        self.SideMenuClose()
        self.createConnection()
        self.HospitalList()
        self.admin_manage_hospital()
        self.feedbackid()
        #Connections
        self.pushButton.clicked.connect(self.SideMenuClose)
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_5.clicked.connect(self.SideMenuOpen)
        self.pushButton_6.clicked.connect(self.SideMenuOpen)
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_8.clicked.connect(self.EditProfile)
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_10.clicked.connect(self.SideMenuOpen)
        self.pushButton_11.clicked.connect(self.register)
        self.pushButton_12.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.pushButton_13.clicked.connect(self.login)
        self.pushButton_14.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.pushButton_15.clicked.connect(self.SideMenuOpen)
        self.pushButton_17.clicked.connect(lambda: self.edit_user())
        self.pushButton_18.clicked.connect(lambda: self.update_user())
        self.pushButton_19.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_21.clicked.connect(self.SideMenuOpen)
        self.pushButton_22.clicked.connect(lambda: self.Q1(0))
        self.pushButton_23.clicked.connect(lambda: self.Q1(1))
        self.pushButton_24.clicked.connect(lambda: self.Q1(2))
        self.pushButton_25.clicked.connect(lambda: self.Q1(3))
        self.pushButton_26.clicked.connect(lambda: self.Q1(4))
        self.pushButton_27.clicked.connect(lambda: self.Q2(0))
        self.pushButton_28.clicked.connect(lambda: self.Q2(1))
        self.pushButton_29.clicked.connect(lambda: self.Q2(2))
        self.pushButton_30.clicked.connect(lambda: self.Q2(3))
        self.pushButton_31.clicked.connect(lambda: self.Q2(4))
        self.pushButton_32.clicked.connect(lambda: self.Q3(0))
        self.pushButton_33.clicked.connect(lambda: self.Q3(1))
        self.pushButton_34.clicked.connect(lambda: self.Q3(2))
        self.pushButton_35.clicked.connect(lambda: self.Q3(3))
        self.pushButton_36.clicked.connect(lambda: self.Q3(4))
        self.pushButton_37.clicked.connect(lambda: self.Q4(0))
        self.pushButton_38.clicked.connect(lambda: self.Q4(1))
        self.pushButton_39.clicked.connect(lambda: self.Q4(2))
        self.pushButton_40.clicked.connect(lambda: self.Q4(3))
        self.pushButton_41.clicked.connect(lambda: self.Q4(4))
        self.pushButton_42.clicked.connect(lambda: self.Q5(0))
        self.pushButton_43.clicked.connect(lambda: self.Q5(1))
        self.pushButton_44.clicked.connect(lambda: self.Q5(2))
        self.pushButton_45.clicked.connect(lambda: self.Q5(3))
        self.pushButton_46.clicked.connect(lambda: self.Q5(4))
        self.pushButton_47.clicked.connect(self.FeedbackSubmit)
        self.pushButton_20.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_48.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_49.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_50.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.pushButton_51.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.pushButton_52.clicked.connect(self.logout)
        self.pushButton_53.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.pushButton_54.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_55.clicked.connect(self.donation)
        self.pushButton_56.clicked.connect(self.SideMenuOpen)
        self.pushButton_57.clicked.connect(self.SideMenuOpen)
        self.pushButton_58.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_59.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_61.clicked.connect(lambda: self.Temp(value = "H001"))
        self.pushButton_62.clicked.connect(lambda: self.Temp(value = "H002"))
        self.pushButton_63.clicked.connect(lambda: self.Temp(value = "H003"))
        self.pushButton_64.clicked.connect(lambda: self.Temp(value_2 = "Blood Donation"))
        self.pushButton_65.clicked.connect(lambda: self.Temp(value_2 = "Plasma Donation"))
        self.pushButton_66.clicked.connect(lambda: self.Temp(value_2 = "Platelet Donation"))
        self.pushButton_67.clicked.connect(lambda: self.Temp(value_2 = 0))
        self.pushButton_68.clicked.connect(lambda: self.Temp(value = 0))
        self.pushButton_69.clicked.connect(lambda: self.Temp(value_3 = "A+"))
        self.pushButton_70.clicked.connect(lambda: self.Temp(value_3 = "AB+"))
        self.pushButton_71.clicked.connect(lambda: self.Temp(value_3 = "B-"))
        self.pushButton_72.clicked.connect(lambda: self.Temp(value_3 = "O+"))
        self.pushButton_73.clicked.connect(lambda: self.Temp(value_3 = "A-"))
        self.pushButton_74.clicked.connect(lambda: self.Temp(value_3 = 0))
        self.pushButton_75.clicked.connect(lambda: self.Temp(value_3 = "O-"))
        self.pushButton_76.clicked.connect(lambda: self.Temp(value_3 = "B-"))
        self.pushButton_77.clicked.connect(lambda: self.Temp(value_3 = "B+"))
        self.pushButton_79.clicked.connect(self.admin_manage_hospital_add)

        #Home Connections
        self.HButton_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        self.HButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.HButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.HButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.HButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.HButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.HButton_7.clicked.connect(self.logout)
        self.HButton_8.clicked.connect(self.SideMenuOpen)
        self.HButton_9.clicked.connect(self.logout)
        #Initial variables

    def SideMenuClose(self):
        self.frame.setMaximumSize(QtCore.QSize(0, 16777215))
        self.centralwidget.setMaximumSize(QtCore.QSize(1080, 16777215))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        MainWindow.resize(1080, 720)

    def SideMenuOpen(self):
            if self.frame.maximumWidth() == 0:  # Menu is closed
                    self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
                    self.centralwidget.setMaximumSize(QtCore.QSize(1280, 16777215))
                    MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
                    MainWindow.resize(1280, 720)
            else:  # Menu is open
                    self.frame.setMaximumSize(QtCore.QSize(0, 16777215))
                    self.centralwidget.setMaximumSize(QtCore.QSize(1080, 16777215))
                    MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
                    MainWindow.resize(1080, 720)

        #Initialise
    def __init__(self):
        self.row_count = None
        self.lastButtonIndex_q1 = None
        self.lastButtonIndex_q2 = None
        self.lastButtonIndex_q3 = None
        self.lastButtonIndex_q4 = None
        self.lastButtonIndex_q5 = None
        self.buttonList_q1 = None
        self.buttonList_q2 = None
        self.buttonList_q3 = None
        self.buttonList_q4 = None
        self.buttonList_q5 = None


    def logout(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        if self.frame.maximumWidth() > 0:  #
                self.frame.setMaximumSize(QtCore.QSize(0, 16777215))
                self.centralwidget.setMaximumSize(QtCore.QSize(1080, 16777215))
                MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
                MainWindow.resize(1080, 720)
        username = " "

    def login(self):
        log_Username = self.lineEdit_12.text()
        log_Password = self.lineEdit_13.text()
        # sqlStatement = "where [Username]=log_Username AND [UserPass] = log_Password"
        # qry = QSqlQuery(db)
        # qry.prepare(sqlStatement)
        # qry.exec()
        query = QSqlQuery(db)
        is_valid_query = query.prepare("SELECT * FROM Users WHERE Username = ? and UserPass = ?")
        if is_valid_query:
                query.addBindValue(log_Username)
                query.addBindValue(log_Password)
                if query.exec():
                        if query.first():
                                user_type = query.value(2)
                                global username
                                username = log_Username
                                if user_type == "admin":
                                    self.stackedWidget.setCurrentIndex(5)
                                else:
                                    self.UserProfile()
                                    self.HistoryData()
                                    self.stackedWidget.setCurrentIndex(3)
                        else:
                            self.pushButton_13.setText("Incorrect Password/Usersname")
                            QTimer.singleShot(3000, lambda: self.pushButton_13.setText("Login"))
                            return True
                else:
                        print(query.lastError().text())

    def register(self):
        log_Username = self.lineEdit_4.text()
        log_Password = self.lineEdit_5.text()
        log_ConfPassword = self.lineEdit_6.text()

        if log_Password != log_ConfPassword:
            self.pushButton_11.setText("Passwords do not match")
            return True

        query = QSqlQuery(db)
        is_valid_query = query.prepare("SELECT COUNT(*) FROM Users WHERE Username = ?")
        if is_valid_query:
            query.addBindValue(log_Username)
            if query.exec() and query.first():
                count = query.value(0)
                if count > 0:
                    self.pushButton_11.setText("Username already exist")
                    QTimer.singleShot(3500, lambda: self.pushButton_11.setText("Register"))
                    return True
            else:
                print(query.lastError().text())
                return True

        query = QSqlQuery(db)
        is_valid_query = query.prepare("INSERT INTO Users (Username, UserPass, UserType) VALUES (?, ?, 'Donor')")
        if is_valid_query:
            query.addBindValue(log_Username)
            query.addBindValue(log_Password)
            if query.exec():
                self.stackedWidget_3.setCurrentIndex(1)
            else:
                print(query.lastError().text())
        else:
            print(query.lastError().text())

        # Insert username into UserProfile with "Not Filled" values
        query = QSqlQuery(db)
        query.prepare(
            "INSERT INTO UserProfile (Username, Name, Password, [Phone Number], Email, Telephone, Address) VALUES (:Username, 'Not Filled', 'Not Filled', NULL, 'Not Filled', NULL, 'Not Filled')")
        query.bindValue(":Username", log_Username)
        if not query.exec():
            print("Failed to insert user into UserProfile:", query.lastError().text())

        # Insert username into Records with "Not Filled" values
        query = QSqlQuery(db)
        query.prepare(
            "INSERT INTO Records (Username, BloodType, Disease, Medication, diagnosis, Age, Gender) VALUES (:Username, 'Not Filled', 'Not Filled', 'Not Filled', 'Not Filled', NULL, 'Not Filled')")
        query.bindValue(":Username", log_Username)
        if not query.exec():
            print("Failed to insert user into Records:", query.lastError().text())


    def donation(self):
        query = QSqlQuery("SELECT COUNT(*) FROM Appointments")
        query.next()
        appointment_id = query.value(0) + 1

        donor_username = username
        donate_date = self.lineEdit_15.text()
        donate_time = self.lineEdit_16.text()
        donate_hospital = self.lineEdit_17.text()
        donate_type = self.comboBox.currentText()
        blood_type = self.lineEdit_26.text()

        query = QSqlQuery()
        query.prepare("INSERT INTO Appointments (AppointmentID, Username, HospitalID, DonationType, BloodType, "
                      "Date, Time) VALUES (?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(appointment_id)
        query.addBindValue(donor_username)
        query.addBindValue(donate_hospital)
        query.addBindValue(donate_type)
        query.addBindValue(blood_type)
        query.addBindValue(donate_date)
        query.addBindValue(donate_time)

        if query.exec():
            self.stackedWidget.setCurrentIndex(3)
            self.HistoryData()
        else:
            print(query.lastError().text())

    def HospitalList(self):
        # prepare query
        query = QSqlQuery(db)
        query.prepare(
            "SELECT * FROM Hospital")
        if query.exec():
            # Loop over the results and populate the table widget with appointment data
            self.tableWidget_2.setRowCount(0)
            row = 0
            while query.next():
                hospital_name = query.value(0)
                hospital_id = query.value(1)
                city = query.value(2)
                address = query.value(3)

                self.tableWidget_2.insertRow(row)
                self.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(hospital_name)))
                self.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(hospital_id)))
                self.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(city)))
                self.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(address)))
                row += 1

        else:
            print(query.lastError().text())

    def admin_manage_hospital(self):
        # prepare query
        query = QSqlQuery(db)
        query.prepare("SELECT * FROM Hospital")
        if query.exec():
            # Loop over the results and populate the table widget with appointment data
            self.tableWidget_3.setRowCount(0)
            row = 0
            while query.next():
                hospital_name = query.value(0)
                hospital_id = query.value(1)
                city = query.value(2)
                address = query.value(3)

                self.tableWidget_3.insertRow(row)
                self.tableWidget_3.setItem(row, 0, QTableWidgetItem(str(hospital_name)))
                self.tableWidget_3.setItem(row, 1, QTableWidgetItem(str(hospital_id)))
                self.tableWidget_3.setItem(row, 2, QTableWidgetItem(str(city)))
                self.tableWidget_3.setItem(row, 3, QTableWidgetItem(str(address)))
                row += 1
        else:
            print(query.lastError().text())

    def admin_manage_hospital_add(self):

        hospital_name = self.lineEdit_2.text()
        hospital_id = self.lineEdit_7.text()
        city = self.lineEdit_10.text()
        address = self.lineEdit_25.text()

        query = QSqlQuery(db)
        query.prepare("INSERT INTO Hospital (HospitalName, HospitalID, City, Address) VALUES (?, ?, ?, ?)")
        query.addBindValue(hospital_name)
        query.addBindValue(hospital_id)
        query.addBindValue(city)
        query.addBindValue(address)

        if query.exec():
            self.stackedWidget.setCurrentIndex(5)
            self.admin_manage_hospital()
        else:
            print(query.lastError().text())



    def FeedbackSubmit(self):
        self.pushButton_47.setStyleSheet("background-color: grey;")
        feedback_id = self.row_count
        self.lastButtonIndex_q1 = self.lastButtonIndex_q1 +1
        self.lastButtonIndex_q2 = self.lastButtonIndex_q2 + 1
        self.lastButtonIndex_q3 = self.lastButtonIndex_q3 + 1
        self.lastButtonIndex_q4 = self.lastButtonIndex_q4 + 1
        self.lastButtonIndex_q5 = self.lastButtonIndex_q5 + 1
        q1 = str(self.lastButtonIndex_q1)
        q2 = str(self.lastButtonIndex_q2)
        q3 = str(self.lastButtonIndex_q3)
        q4 = str(self.lastButtonIndex_q4)
        q5 = str(self.lastButtonIndex_q5)
        q6 = self.textEdit_6.toPlainText()



        query = QSqlQuery(db)
        query.prepare("INSERT INTO Feedback ([Feedback ID], Username, Q1, Q2, Q3, Q4, Q5, Q6) VALUES (:feedback_id, :name, :q1, :q2, :q3, :q4, :q5, :q6)")
        query.bindValue(":feedback_id", feedback_id)
        query.bindValue(":name", username)
        query.bindValue(":q1", q1)
        query.bindValue(":q2", q2)
        query.bindValue(":q3", q3)
        query.bindValue(":q4", q4)
        query.bindValue(":q5", q5)
        query.bindValue(":q6", q6)
        if query.exec():
            print("Success")





    def Q1(self, index_q1):
        self.buttonList_q1 = [self.pushButton_22,self.pushButton_23,self.pushButton_24,self.pushButton_25,self.pushButton_26]
        if self.lastButtonIndex_q1 is not None:
            self.buttonList_q1[self.lastButtonIndex_q1].setStyleSheet("")
        self.buttonList_q1[index_q1].setStyleSheet("background-color: grey;")
        self.lastButtonIndex_q1 = index_q1

    def Q2(self, index_q2):
        self.buttonList_q2 = [self.pushButton_27, self.pushButton_28, self.pushButton_29, self.pushButton_30,self.pushButton_31]
        if self.lastButtonIndex_q2 is not None:
            self.buttonList_q2[self.lastButtonIndex_q2].setStyleSheet("")
        self.buttonList_q2[index_q2].setStyleSheet("background-color: grey;")
        self.lastButtonIndex_q2 = index_q2

    def Q3(self, index_q3):
        self.buttonList_q3 = [self.pushButton_32, self.pushButton_33, self.pushButton_34, self.pushButton_35,self.pushButton_36]
        if self.lastButtonIndex_q3 is not None:
            self.buttonList_q3[self.lastButtonIndex_q3].setStyleSheet("")
        self.buttonList_q3[index_q3].setStyleSheet("background-color: grey;")
        self.lastButtonIndex_q3 = index_q3

    def Q4(self, index_q4):
        self.buttonList_q4 = [self.pushButton_37, self.pushButton_38, self.pushButton_39, self.pushButton_40,self.pushButton_41]
        if self.lastButtonIndex_q4 is not None:
            self.buttonList_q4[self.lastButtonIndex_q4].setStyleSheet("")
        self.buttonList_q4[index_q4].setStyleSheet("background-color: grey;")
        self.lastButtonIndex_q4 = index_q4

    def Q5(self, index_q5):
        self.buttonList_q5 = [self.pushButton_42, self.pushButton_43, self.pushButton_44, self.pushButton_45,self.pushButton_46]
        if self.lastButtonIndex_q5 is not None:
            self.buttonList_q5[self.lastButtonIndex_q5].setStyleSheet("")
        self.buttonList_q5[index_q5].setStyleSheet("background-color: grey;")
        self.lastButtonIndex_q5 = index_q5

    def feedbackid(self):
        query = QSqlQuery(db)
        query.exec("SELECT COUNT(*) FROM Feedback")
        if query.next():
            self.row_count = query.value(0) + 1



    def createConnection(self):
        SERVER_NAME = 'LAPTOP-Q1SP2NU1'                 #LAPTOP-Q1SP2NU1 #LAPTOP-GISFMR8S #LAPTOP-Joseph #DESKTOP-T07EGLG
        DATABASE_NAME = 'Accounts'
        Username = " "
        Password = " "

        # connString = f'DRIVER = {{SQL Server}};'\
        #             f'SERVER = {Server_Name};'\
        #             f'DATABASE ={Database_Name}'
        connString = (
            f"DRIVER={{SQL Server}};" f"SERVER={SERVER_NAME};" f"DATABASE={DATABASE_NAME}"
        )
        global db
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(connString)
        if db.open():
            print('connected to SQL Server successfully')
            return True
        else:
            print('connection failed')
            return False

    def HistoryData(self):
        # Retrieve the currently logged in username from the cache
        # Query the database for appointments for the current user
        query = QSqlQuery(db)
        query.prepare(
                "SELECT AppointmentID, DonationType, BloodType, Date, Time FROM Appointments WHERE Username = ?")
        query.addBindValue(username)
        if query.exec():
                # Loop over the results and populate the table widget with appointment data
                self.tableWidget.setRowCount(0)
                row = 0
                while query.next():
                        appointment_id = query.value(0)
                        donation_type = query.value(1)
                        blood_type = query.value(2)
                        date = query.value(3)
                        time = query.value(4)

                        self.tableWidget.insertRow(row)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(appointment_id)))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(donation_type))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(blood_type))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(date)))
                        self.tableWidget.setItem(row, 4, QTableWidgetItem(str(time)))
                        row += 1

        else:
                print(query.lastError().text())

    def UserProfile(self):
        # Query the database for user profile data
        query = QSqlQuery(db)
        query.prepare(
            "SELECT * FROM UserProfile WHERE Username = ?")
        query.addBindValue(username)
        if query.exec():
            # Fetch the data from the query result
            query.next()
            Name = query.value(1)
            Password = query.value(2)
            Phone_Number = query.value(3)
            Email = query.value(4)
            Telephone = query.value(5)
            Address = query.value(6)

            # Set the text of the QTextEdit widget
            self.textEdit.setPlainText(Name)
            self.textEdit_2.setPlainText(Email)
            self.textEdit_3.setPlainText(str(Phone_Number))
            self.textEdit_4.setPlainText(Password)
        else:
            print(query.lastError().text())  # print the error message if the query fails

        query.prepare(
            "SELECT Username, BloodType, Disease, Medication, diagnosis, Age, Gender FROM Records WHERE Username = ?")
        query.addBindValue(username)
        if query.exec():
            query.next()
            BloodType = query.value(1)
            Disease = query.value(2)
            Medication = query.value(3)
            diagnosis = query.value(4)
            Age = query.value(5)
            Gender = query.value(6)

            self.textEdit_5.setPlainText(Gender)
            self.textEdit_7.setPlainText(str(Age))
            self.textEdit_8.setPlainText(BloodType)
            self.textEdit_9.setPlainText(Disease)
            self.textEdit_10.setPlainText(diagnosis)
            self.textEdit_11.setPlainText(Medication)



    def EditProfile(self):
        # Get the new data from the textEdit widgets
        edit_name = self.textEdit.toPlainText()
        edit_email = self.textEdit_2.toPlainText()
        edit_mobilenumber = self.textEdit_3.toPlainText()
        edit_password = self.textEdit_4.toPlainText()

        # Update the user profile table with the new data
        query = QSqlQuery(db)
        query.prepare(
            "UPDATE UserProfile SET Name = ?, Email = ?, [Phone Number] = ?, Password = ? WHERE Username = ?")
        query.addBindValue(edit_name)
        query.addBindValue(edit_email)
        query.addBindValue(edit_mobilenumber)
        query.addBindValue(edit_password)
        query.addBindValue(username)
        print(query)
        if query.exec():
            print("Data updated successfully")
        else:
            print("Error updating data:", query.lastError().text())

        edit_gender = self.textEdit_5.toPlainText()
        edit_age = self.textEdit_7.toPlainText()
        edit_blood = self.textEdit_8.toPlainText()
        edit_disease = self.textEdit_9.toPlainText()
        edit_diagnosis = self.textEdit_10.toPlainText()
        edit_medication = self.textEdit_11.toPlainText()

        try:
            edit_age = int(edit_age)
        except ValueError:
            self.pushButton_8.setText("Error: Invalid Age")
            QTimer.singleShot(3500, lambda: self.pushButton_8.setText("Edit Profile"))
            return

        if edit_gender not in ('Male', 'Female'):
            self.pushButton_8.setText("Error: Invalid Gender")
            QTimer.singleShot(3500, lambda: self.pushButton_8.setText("Edit Profile"))
            return

        valid_blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
        if edit_blood not in valid_blood_types:
            self.pushButton_8.setText("Error: Invalid Blood Type")
            QTimer.singleShot(3500, lambda: self.pushButton_8.setText("Edit Profile"))
            return


        # Update the record table with the new data
        query = QSqlQuery(db)
        query.prepare(
            "UPDATE Records SET Gender = ?, Age = ?, BloodType = ?, Disease = ?, Medication = ?, Diagnosis = ? WHERE Username = ?")
        query.addBindValue(edit_gender)
        query.addBindValue(edit_age)
        query.addBindValue(edit_blood)
        query.addBindValue(edit_disease)
        query.addBindValue(edit_medication)
        query.addBindValue(edit_diagnosis)
        query.addBindValue(username)
        if query.exec():
            print("Data updated successfully")
        else:
            print("Error updating data:", query.lastError().text())



    def admin_view_appointments(self):
        # get name for query
        try:
            name = self.lineEdit.text()

            # prepare query
            query = QSqlQuery(db)
            query.prepare("SELECT * from [Appointments] WHERE Username = ?")

            query.addBindValue(name)
            if query.exec():
                if query.isActive() and query.size() > 0:
                    self.table_widget.setRowCount(0)
                    rows = 0
                    while query.next():
                        self.table_widget.insertRow(rows)
                        for i in range(query.record().count()):
                            print(i)
                            self.table_widget.setItem(rows, i, QTableWidgetItem(str(query.value(i))))
                        rows += 1
                else:
                    msgBox = QMessageBox()
                    msgBox.setText('Invalid username')
                    msgBox.addButton(QMessageBox.StandardButton.Ok)
                    msgBox.setIcon(QMessageBox.Icon.Warning)
                    msgBox.exec()
            else:
                print(query.lastError().text())
        except Exception as e:
            print(f"an error occured: {e}")

    def edit_user(self):
        # get username
        username = str(self.lineEdit_3.text())
        print(username)

        # query
        query = QSqlQuery(db)
        query.prepare(
            "Select Distinct Name, Records.Username, Gender, Age, Address, Email, Telephone, BloodType, Disease, Medication, diagnosis from Records inner join UserProfile on Records.Username = UserProfile.Username where Records.Username = :username")
        query.addBindValue(username)
        if query.exec():
            print("query successful")
            while (query.next()):
                # name
                self.lineEdit_8.setText(str(query.value(0)))
                # Gender
                self.lineEdit_20.setText(str(query.value(2)))
                # Age
                self.lineEdit_19.setText(str(query.value(3)))
                # Address
                self.lineEdit_23.setText(str(query.value(4)))
                # Email
                self.lineEdit_11.setText(str(query.value(5)))
                # Telephone
                self.lineEdit_14.setText(str(query.value(6)))
                # Blood Type
                self.lineEdit_18.setText(str(query.value(7)))
                # Diseases
                self.lineEdit_21.setText(str(query.value(8)))
                # Medication
                self.lineEdit_22.setText(str(query.value(9)))
                # Diagnosis
                self.lineEdit_24.setText(str(query.value(10)))
        else:
            print("query failed")

    def update_user(self):
        list = []
        name = self.lineEdit_8.text()
        list.append(name)
        gender = self.lineEdit_20.text()
        list.append(gender)
        age = int(self.lineEdit_19.text())
        list.append(age)
        address = self.lineEdit_23.text()
        list.append(address)
        email = self.lineEdit_11.text()
        list.append(email)
        telephone = self.lineEdit_14.text()
        list.append(telephone)
        bloodType = self.lineEdit_18.text()
        list.append(bloodType)
        disease = self.lineEdit_21.text()
        list.append(disease)
        medication = self.lineEdit_22.text()
        list.append(medication)
        diagnosis = self.lineEdit_24.text()
        list.append(diagnosis)

        try:
            if not all(list):
                QMessageBox.critical(self.pushButton_18, "Error", "One or more fields are not filled in")
                return
        except Exception as e:
            print(f"An error occurred: {e}")

        username = str(self.lineEdit_3.text())
        print(username)

        print(list)

        # query
        query = QSqlQuery(db)
        query.prepare("""
update UserProfile set Name = :name, [Phone Number] = :telephone, Email = :email, Address = :address where Username = :username;
update Records set BloodType = :bloodtype, Disease = :disease, Medication = :medication, diagnosis = :diagnosis, Age = :age, Gender = :gender where Username = :username;""")

        query.bindValue(":name", name)
        query.bindValue(":username", username)
        query.bindValue(":gender", gender)
        query.bindValue(":age", age)
        query.bindValue(":address", address)
        query.bindValue(":email", email)
        query.bindValue(":telephone", telephone)
        query.bindValue(":bloodtype", bloodType)
        query.bindValue(":disease", disease)
        query.bindValue(":medication", medication)
        query.bindValue(":diagnosis", diagnosis)

        if query.exec():
            print("Update successful")
            try:
                QMessageBox.information(self.pushButton_18, "Success", "Update successful.")
            except Exception as e:
                print("Error: ", e)
        else:
            QMessageBox.critical(self.pushButton_18, "Error", "There was an error parsing the query", QMessageBox.StandardButton.Ok)
            print("update failed")


    def Temp(self, value=None, value_2=None, value_3=None):
        if value is not None:
            self.value = value
        if value_2 is not None:
            self.value_2 = value_2
        if value_3 is not None:
            self.value_3 = value_3
        self.run_query()

    def run_query(self):
        self.tableWidget_4.clearContents()
        self.tableWidget_4.setRowCount(0)

        query_str = "SELECT * FROM Appointments"
        conditions = []
        if self.value is not None and self.value != 0:
            conditions.append("HospitalID = :hospital_id")
        if self.value_2 is not None and self.value_2 != 0:
            conditions.append("DonationType = :donation_type")
        if self.value_3 is not None and self.value_3 != 0:
            conditions.append("BloodType = :blood_type")

        if conditions:
            query_str += " WHERE " + " AND ".join(conditions)
        query = QSqlQuery(db)
        query.prepare(query_str)

        if self.value is not None and self.value != 0:
            query.bindValue(":hospital_id", self.value)
        if self.value_2 is not None and self.value_2 != 0:
            query.bindValue(":donation_type", self.value_2)
        if self.value_3 is not None and self.value_3 != 0:
            query.bindValue(":blood_type", self.value_3)

        if query.exec():
            self.tableWidget_4.setRowCount(query.size())
            num_fields = query.record().count()
            self.tableWidget_4.setColumnCount(num_fields)
            for i in range(num_fields):
                column_name = query.record().fieldName(i)
                header_item = QTableWidgetItem(column_name)
                self.tableWidget_4.setHorizontalHeaderItem(i, header_item)

            row = 0
            while query.next():
                self.tableWidget_4.insertRow(row)
                for i in range(num_fields):
                    field_value = query.value(i)
                    item = QTableWidgetItem(str(field_value))
                    self.tableWidget_4.setItem(row, i, item)
                row += 1
        else:
            print("Query execution failed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
