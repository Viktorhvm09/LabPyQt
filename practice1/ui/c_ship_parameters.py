# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_ship_parameters.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(379, 273)
        Form.setMinimumSize(QSize(379, 273))
        Form.setMaximumSize(QSize(379, 273))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditTemp = QLineEdit(self.groupBox)
        self.lineEditTemp.setObjectName(u"lineEditTemp")
        self.lineEditTemp.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.horizontalLayout.addWidget(self.lineEditTemp)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_Dehermitization = QLabel(self.groupBox)
        self.label_Dehermitization.setObjectName(u"label_Dehermitization")
        self.label_Dehermitization.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_Dehermitization)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_Tank1 = QLabel(self.groupBox)
        self.label_Tank1.setObjectName(u"label_Tank1")
        self.label_Tank1.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_Tank1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_Tank2 = QLabel(self.groupBox)
        self.label_Tank2.setObjectName(u"label_Tank2")
        self.label_Tank2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_Tank2)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_Tank3 = QLabel(self.groupBox)
        self.label_Tank3.setObjectName(u"label_Tank3")
        self.label_Tank3.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_Tank3)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.lineEditTemp.setText(QCoreApplication.translate("Form", u"22 C", None))
        self.label_Dehermitization.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_Tank1.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21161", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_Tank2.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21162", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_Tank3.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21163", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

