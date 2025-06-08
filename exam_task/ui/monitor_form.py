# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitor_formMrMZJu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QPlainTextEdit, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 400)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit_info = QPlainTextEdit(self.tab)
        self.plainTextEdit_info.setObjectName(u"plainTextEdit_info")

        self.verticalLayout_2.addWidget(self.plainTextEdit_info)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget_processes = QTableWidget(self.tab_2)
        if (self.tableWidget_processes.columnCount() < 5):
            self.tableWidget_processes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_processes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_processes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_processes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_processes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_processes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_processes.setObjectName(u"tableWidget_processes")

        self.verticalLayout_3.addWidget(self.tableWidget_processes)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget_services = QTableWidget(self.tab_3)
        if (self.tableWidget_services.columnCount() < 5):
            self.tableWidget_services.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_services.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_services.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_services.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_services.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_services.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_services.setObjectName(u"tableWidget_services")

        self.verticalLayout_4.addWidget(self.tableWidget_services)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget_task = QTableWidget(self.tab_4)
        if (self.tableWidget_task.columnCount() < 1):
            self.tableWidget_task.setColumnCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_task.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        self.tableWidget_task.setObjectName(u"tableWidget_task")

        self.verticalLayout_5.addWidget(self.tableWidget_task)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f (\u0441\u0435\u043a):", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"5", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"10", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"30", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        ___qtablewidgetitem = self.tableWidget_processes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem1 = self.tableWidget_processes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget_processes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0426\u041f", None));
        ___qtablewidgetitem3 = self.tableWidget_processes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u043c\u044f\u0442\u044c", None));
        ___qtablewidgetitem4 = self.tableWidget_processes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u043a", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        ___qtablewidgetitem5 = self.tableWidget_services.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem6 = self.tableWidget_services.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u0418\u0414 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 \u0441\u043b\u0443\u0436\u0431\u044b", None));
        ___qtablewidgetitem7 = self.tableWidget_services.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem8 = self.tableWidget_services.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None));
        ___qtablewidgetitem9 = self.tableWidget_services.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        ___qtablewidgetitem10 = self.tableWidget_task.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
    # retranslateUi

