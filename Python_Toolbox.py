"""
This program is designed to place the most common tools I use for python right
at my fingertips.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from QT_Converter import QtConverter
from Py_Installer import PyInstaller
import resource

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        button_size = 40
        TabWidget.setObjectName("TabWidget")
        TabWidget.setWindowModality(QtCore.Qt.ApplicationModal)
        TabWidget.resize(1300, 350)
        TabWidget.setMinimumSize(QtCore.QSize(1300, 350))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        TabWidget.setFont(font)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        TabWidget.setElideMode(QtCore.Qt.ElideNone)
        TabWidget.setMovable(True)
        TabWidget.setTabBarAutoHide(False)
        self.converter_page = QtWidgets.QWidget()
        self.converter_page.setMinimumSize(QtCore.QSize(0, 0))
        self.converter_page.setAutoFillBackground(False)
        self.converter_page.setStyleSheet("QWidget #converter_page{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(165, 165, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.converter_page.setObjectName("converter_page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.converter_page)
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.qt_error_lab = QtWidgets.QLabel(self.converter_page)
        font = QtGui.QFont()
        self.qt_error_lab.setFont(font)
        self.qt_error_lab.setText("")
        self.qt_error_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.qt_error_lab.setObjectName("qt_error_lab")
        self.gridLayout_3.addWidget(self.qt_error_lab, 8, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.browse_ui = QtWidgets.QToolButton(self.converter_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/addfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_ui.setIcon(icon)
        self.browse_ui.setIconSize(QtCore.QSize(
                button_size,
                button_size))
        self.browse_ui.setAutoRaise(True)
        self.browse_ui.setObjectName("browse_ui")
        self.gridLayout_3.addWidget(self.browse_ui, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 9, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.converter_page)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 0, 0, 1, 4)
        self.ui_from = QtWidgets.QLineEdit(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_from.setFont(font)
        self.ui_from.setReadOnly(True)
        self.ui_from.setObjectName("ui_from")
        self.gridLayout_3.addWidget(self.ui_from, 1, 2, 1, 1)
        self.browse_ui_dest = QtWidgets.QToolButton(self.converter_page)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/addfolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_ui_dest.setIcon(icon1)
        self.browse_ui_dest.setIconSize(QtCore.QSize(button_size,
                                                     button_size))
        self.browse_ui_dest.setAutoRaise(True)
        self.browse_ui_dest.setObjectName("browse_ui_dest")
        self.gridLayout_3.addWidget(self.browse_ui_dest, 2, 3, 1, 1)
        self.ui_dest = QtWidgets.QLineEdit(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_dest.setFont(font)
        self.ui_dest.setReadOnly(True)
        self.ui_dest.setObjectName("ui_dest")
        self.gridLayout_3.addWidget(self.ui_dest, 2, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.converter_page)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 6, 0, 1, 4)
        self.ui_name_change = QtWidgets.QLineEdit(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui_name_change.setFont(font)
        self.ui_name_change.setObjectName("ui_name_change")
        self.gridLayout_3.addWidget(self.ui_name_change, 3, 2, 1, 2)
        self.qt_init = QtWidgets.QToolButton(self.converter_page)
        font = QtGui.QFont()
        self.qt_init.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.qt_init.setIcon(icon2)
        self.qt_init.setIconSize(QtCore.QSize(button_size,
                                              button_size))
        self.qt_init.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.qt_init.setAutoRaise(True)
        self.qt_init.setObjectName("qt_init")
        self.gridLayout_3.addWidget(self.qt_init, 7, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.converter_page)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 1, 4, 1)
        self.qt_prog_bar = QtWidgets.QProgressBar(self.converter_page)
        font = QtGui.QFont()
        self.qt_prog_bar.setFont(font)
        self.qt_prog_bar.setProperty("value", 0)
        self.qt_prog_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.qt_prog_bar.setObjectName("qt_prog_bar")
        self.gridLayout_3.addWidget(self.qt_prog_bar, 7, 0, 1, 3)
        self.ui_resource = QtWidgets.QLineEdit(self.converter_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_resource.setFont(font)
        self.ui_resource.setReadOnly(True)
        self.ui_resource.setObjectName("ui_resource")
        self.gridLayout_3.addWidget(self.ui_resource, 4, 2, 1, 1)
        self.browse_ui_resource = QtWidgets.QToolButton(self.converter_page)
        self.browse_ui_resource.setIcon(icon)
        self.browse_ui_resource.setIconSize(QtCore.QSize(button_size,
                                                         button_size))
        self.browse_ui_resource.setAutoRaise(True)
        self.browse_ui_resource.setObjectName("browse_ui_resource")
        self.gridLayout_3.addWidget(self.browse_ui_resource, 4, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/convert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.converter_page, icon3, "")
        self.pyinstaller_page = QtWidgets.QWidget()
        self.pyinstaller_page.setAutoFillBackground(False)
        self.pyinstaller_page.setStyleSheet("QWidget #pyinstaller_page{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(165, 165, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.pyinstaller_page.setObjectName("pyinstaller_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pyinstaller_page)
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.line_4 = QtWidgets.QFrame(self.pyinstaller_page)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_6.addWidget(self.line_4, 4, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 1)
        self.pyinstaller_to = QtWidgets.QLineEdit(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pyinstaller_to.setFont(font)
        self.pyinstaller_to.setReadOnly(True)
        self.pyinstaller_to.setObjectName("pyinstaller_to")
        self.gridLayout_6.addWidget(self.pyinstaller_to, 2, 2, 1, 2)
        self.pyinstaller_from = QtWidgets.QLineEdit(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pyinstaller_from.setFont(font)
        self.pyinstaller_from.setReadOnly(True)
        self.pyinstaller_from.setObjectName("pyinstaller_from")
        self.gridLayout_6.addWidget(self.pyinstaller_from, 1, 2, 1, 2)
        self.browse_pyinstaller_dest = QtWidgets.QToolButton(self.pyinstaller_page)
        self.browse_pyinstaller_dest.setIcon(icon1)
        self.browse_pyinstaller_dest.setIconSize(QtCore.QSize(button_size,
                                                              button_size))
        self.browse_pyinstaller_dest.setAutoRaise(True)
        self.browse_pyinstaller_dest.setArrowType(QtCore.Qt.NoArrow)
        self.browse_pyinstaller_dest.setObjectName("browse_pyinstaller_dest")
        self.gridLayout_6.addWidget(self.browse_pyinstaller_dest, 2, 4, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.pyinstaller_page)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_6.addWidget(self.line_3, 1, 1, 3, 1)
        self.pyinstaller_init = QtWidgets.QToolButton(self.pyinstaller_page)
        self.pyinstaller_init.setIcon(icon2)
        self.pyinstaller_init.setIconSize(QtCore.QSize(button_size,
                                                       button_size))
        self.pyinstaller_init.setAutoRaise(True)
        self.pyinstaller_init.setArrowType(QtCore.Qt.NoArrow)
        self.pyinstaller_init.setObjectName("pyinstaller_init")
        self.gridLayout_6.addWidget(self.pyinstaller_init, 5, 4, 1, 1)
        self.pyinstaller_prog_bar = QtWidgets.QProgressBar(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pyinstaller_prog_bar.setFont(font)
        self.pyinstaller_prog_bar.setProperty("value", 0)
        self.pyinstaller_prog_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.pyinstaller_prog_bar.setObjectName("pyinstaller_prog_bar")
        self.gridLayout_6.addWidget(self.pyinstaller_prog_bar, 5, 0, 1, 4)
        self.pyinstaller_error_lab = QtWidgets.QLabel(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pyinstaller_error_lab.setFont(font)
        self.pyinstaller_error_lab.setText("")
        self.pyinstaller_error_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.pyinstaller_error_lab.setObjectName("pyinstaller_error_lab")
        self.gridLayout_6.addWidget(self.pyinstaller_error_lab, 6, 0, 1, 5)
        self.browse_pyinstaller_from = QtWidgets.QToolButton(self.pyinstaller_page)
        self.browse_pyinstaller_from.setIcon(icon)
        self.browse_pyinstaller_from.setIconSize(QtCore.QSize(button_size,
                                                              button_size))
        self.browse_pyinstaller_from.setAutoRaise(True)
        self.browse_pyinstaller_from.setArrowType(QtCore.Qt.NoArrow)
        self.browse_pyinstaller_from.setObjectName("browse_pyinstaller_from")
        self.gridLayout_6.addWidget(self.browse_pyinstaller_from, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 2, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.pyinstaller_page)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_6.addWidget(self.line_5, 0, 0, 1, 5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.onefile_check = QtWidgets.QCheckBox(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.onefile_check.setFont(font)
        self.onefile_check.setTristate(False)
        self.onefile_check.setObjectName("onefile_check")
        self.verticalLayout.addWidget(self.onefile_check)
        self.noconsole_check = QtWidgets.QCheckBox(self.pyinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.noconsole_check.setFont(font)
        self.noconsole_check.setObjectName("noconsole_check")
        self.verticalLayout.addWidget(self.noconsole_check)
        self.gridLayout_6.addLayout(self.verticalLayout, 3, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 7, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 2, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/oneway.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.pyinstaller_page, icon4, "")
        self.pipinstaller_page = QtWidgets.QWidget()
        self.pipinstaller_page.setStyleSheet("QWidget #pipinstaller_page{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(165, 165, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.pipinstaller_page.setObjectName("pipinstaller_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.pipinstaller_page)
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line_8 = QtWidgets.QFrame(self.pipinstaller_page)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_5.addWidget(self.line_8, 0, 0, 1, 4)
        self.pip_req = QtWidgets.QLineEdit(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pip_req.setFont(font)
        self.pip_req.setReadOnly(True)
        self.pip_req.setObjectName("pip_req")
        self.gridLayout_5.addWidget(self.pip_req, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 7, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)
        self.pip_from = QtWidgets.QLineEdit(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pip_from.setFont(font)
        self.pip_from.setReadOnly(True)
        self.pip_from.setObjectName("pip_from")
        self.gridLayout_5.addWidget(self.pip_from, 1, 2, 1, 1)
        self.browse_pip_req = QtWidgets.QToolButton(self.pipinstaller_page)
        self.browse_pip_req.setIcon(icon)
        self.browse_pip_req.setIconSize(QtCore.QSize(button_size,
                                                     button_size))
        self.browse_pip_req.setAutoRaise(True)
        self.browse_pip_req.setArrowType(QtCore.Qt.NoArrow)
        self.browse_pip_req.setObjectName("browse_pip_req")
        self.gridLayout_5.addWidget(self.browse_pip_req, 2, 3, 1, 1)
        self.pip_prog_bar = QtWidgets.QProgressBar(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.pip_prog_bar.setFont(font)
        self.pip_prog_bar.setProperty("value", 0)
        self.pip_prog_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.pip_prog_bar.setObjectName("pip_prog_bar")
        self.gridLayout_5.addWidget(self.pip_prog_bar, 5, 0, 1, 3)
        self.browse_pip_from = QtWidgets.QToolButton(self.pipinstaller_page)
        self.browse_pip_from.setIcon(icon)
        self.browse_pip_from.setIconSize(QtCore.QSize(button_size,
                                                      button_size))
        self.browse_pip_from.setAutoRaise(True)
        self.browse_pip_from.setArrowType(QtCore.Qt.NoArrow)
        self.browse_pip_from.setObjectName("browse_pip_from")
        self.gridLayout_5.addWidget(self.browse_pip_from, 1, 3, 1, 1)
        self.pip_init = QtWidgets.QToolButton(self.pipinstaller_page)
        self.pip_init.setIcon(icon2)
        self.pip_init.setIconSize(QtCore.QSize(button_size,
                                               button_size))
        self.pip_init.setAutoRaise(True)
        self.pip_init.setArrowType(QtCore.Qt.NoArrow)
        self.pip_init.setObjectName("pip_init")
        self.gridLayout_5.addWidget(self.pip_init, 5, 3, 1, 1)
        self.pip_error_lab = QtWidgets.QLabel(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.pip_error_lab.setFont(font)
        self.pip_error_lab.setText("")
        self.pip_error_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.pip_error_lab.setObjectName("pip_error_lab")
        self.gridLayout_5.addWidget(self.pip_error_lab, 6, 0, 1, 4)
        self.line_9 = QtWidgets.QFrame(self.pipinstaller_page)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_5.addWidget(self.line_9, 4, 0, 1, 4)
        self.line_7 = QtWidgets.QFrame(self.pipinstaller_page)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_5.addWidget(self.line_7, 1, 1, 3, 1)
        self.pip_remove_check = QtWidgets.QCheckBox(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pip_remove_check.setFont(font)
        self.pip_remove_check.setTristate(False)
        self.pip_remove_check.setObjectName("pip_remove_check")
        self.gridLayout_5.addWidget(self.pip_remove_check, 3, 2, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.pyinstaller_error_lab_2 = QtWidgets.QLabel(self.pipinstaller_page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pyinstaller_error_lab_2.setFont(font)
        self.pyinstaller_error_lab_2.setText("")
        self.pyinstaller_error_lab_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pyinstaller_error_lab_2.setObjectName("pyinstaller_error_lab_2")
        self.gridLayout_7.addWidget(self.pyinstaller_error_lab_2, 3, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/collect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.pipinstaller_page, icon5, "")
        self.virtualenv_page = QtWidgets.QWidget()
        self.virtualenv_page.setStyleSheet("QWidget #virtualenv_page{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(165, 165, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.virtualenv_page.setObjectName("virtualenv_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.virtualenv_page)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.virtual_to = QtWidgets.QLineEdit(self.virtualenv_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.virtual_to.setFont(font)
        self.virtual_to.setReadOnly(True)
        self.virtual_to.setObjectName("virtual_to")
        self.gridLayout.addWidget(self.virtual_to, 1, 2, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.virtualenv_page)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 0, 0, 1, 3)
        self.virtual_prog_bar = QtWidgets.QProgressBar(self.virtualenv_page)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.virtual_prog_bar.setFont(font)
        self.virtual_prog_bar.setProperty("value", 0)
        self.virtual_prog_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.virtual_prog_bar.setObjectName("virtual_prog_bar")
        self.gridLayout.addWidget(self.virtual_prog_bar, 4, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.virtualenv_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.virtual_init = QtWidgets.QToolButton(self.virtualenv_page)
        self.virtual_init.setIcon(icon2)
        self.virtual_init.setIconSize(QtCore.QSize(button_size,
                                                   button_size))
        self.virtual_init.setAutoRaise(True)
        self.virtual_init.setObjectName("virtual_init")
        self.gridLayout.addWidget(self.virtual_init, 4, 3, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.virtualenv_page)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 3, 0, 1, 3)
        self.browse_virtual_to = QtWidgets.QToolButton(self.virtualenv_page)
        self.browse_virtual_to.setIcon(icon1)
        self.browse_virtual_to.setIconSize(QtCore.QSize(button_size,
                                                        button_size))
        self.browse_virtual_to.setAutoRaise(True)
        self.browse_virtual_to.setObjectName("browse_virtual_to")
        self.gridLayout.addWidget(self.browse_virtual_to, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.virtualenv_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.virtual_new_python = QtWidgets.QLineEdit(self.virtualenv_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.virtual_new_python.setFont(font)
        self.virtual_new_python.setReadOnly(True)
        self.virtual_new_python.setObjectName("virtual_new_python")
        self.gridLayout.addWidget(self.virtual_new_python, 2, 2, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.virtualenv_page)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout.addWidget(self.line_12, 1, 1, 2, 1)
        self.browse_virtual_python = QtWidgets.QToolButton(self.virtualenv_page)
        self.browse_virtual_python.setIcon(icon)
        self.browse_virtual_python.setIconSize(QtCore.QSize(button_size,
                                                            button_size))
        self.browse_virtual_python.setAutoRaise(True)
        self.browse_virtual_python.setObjectName("browse_virtual_python")
        self.gridLayout.addWidget(self.browse_virtual_python, 2, 3, 1, 1)
        self.virtual_error_lab = QtWidgets.QLabel(self.virtualenv_page)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setItalic(True)
        self.virtual_error_lab.setFont(font)
        self.virtual_error_lab.setText("")
        self.virtual_error_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.virtual_error_lab.setObjectName("virtual_error_lab")
        self.gridLayout.addWidget(self.virtual_error_lab, 5, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/physics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.virtualenv_page, icon6, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

        self.LoadInit()

        # %% QT CONVERSION DEFINITION
        self.browse_ui.clicked.connect(self.UiFileLocation)
        self.browse_ui_dest.clicked.connect(self.UiDestLocation)
        self.browse_ui_resource.clicked.connect(self.UiResourceLocation)
        self.ui_name_change.textChanged.connect(self.UiNameChanged)
        self.qt_init.clicked.connect(self.QtConverInit)

        # %% PYINSTALLER DEFINITION
        self.browse_pyinstaller_from.clicked.connect(self.PyinstallerFrom)
        self.browse_pyinstaller_dest.clicked.connect(self.PyinstallerTo)
        self.onefile_check.stateChanged.connect(self.PyinstallerOneFile)
        self.noconsole_check.stateChanged.connect(self.PyinstallerNoConsole)
        self.pyinstaller_init.clicked.connect(self.PyinstallerInit)

        # %% PIP INSTALLER DEFINITION
        # %% VIRTUALENV DEFINITION

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.label.setText(_translate("TabWidget", "Step 1: Browse for the .ui file."))
        self.label_2.setText(_translate("TabWidget", "Step 2: Browse for the destination to place your new .py file."))
        self.browse_ui.setText(_translate("TabWidget", "..."))
        self.label_3.setText(_translate("TabWidget", "Step 3: If you would like to change the file name, do so here."))
        self.browse_ui_dest.setText(_translate("TabWidget", "..."))
        self.ui_name_change.setPlaceholderText(_translate("TabWidget", "...Leave blank if the .ui file name is what you would like. Naming Ex: newname or newname.py"))
        self.qt_init.setText(_translate("TabWidget", "..."))
        self.label_11.setText(_translate("TabWidget", "Step 4: If you have a resource file, browse to it."))
        self.ui_resource.setPlaceholderText(_translate("TabWidget", "...Leave blank if you do not have a resource file."))
        self.browse_ui_resource.setText(_translate("TabWidget", "..."))
        TabWidget.setTabText(TabWidget.indexOf(self.converter_page), _translate("TabWidget", "QT Converter"))
        TabWidget.setTabToolTip(TabWidget.indexOf(self.converter_page), _translate("TabWidget", "Use for converting QT files (.ui) to (.py)."))
        self.label_6.setText(_translate("TabWidget", "Step 3: Determine whether you would like to condense everything into one .exe file or if you don\'t want a console to show."))
        self.browse_pyinstaller_dest.setText(_translate("TabWidget", "..."))
        self.pyinstaller_init.setText(_translate("TabWidget", "..."))
        self.browse_pyinstaller_from.setText(_translate("TabWidget", "..."))
        self.label_4.setText(_translate("TabWidget", "Step 1: Browse for the .py file."))
        self.label_5.setText(_translate("TabWidget", "Step 2: Browse to the destination you would like to place your Executable"))
        self.onefile_check.setText(_translate("TabWidget", "On File?"))
        self.noconsole_check.setText(_translate("TabWidget", "No Console?"))
        TabWidget.setTabText(TabWidget.indexOf(self.pyinstaller_page), _translate("TabWidget", "PyInstaller"))
        TabWidget.setTabToolTip(TabWidget.indexOf(self.pyinstaller_page), _translate("TabWidget", "Use for generating a .EXE of a .py file."))
        self.label_8.setText(_translate("TabWidget", "Step 2: If you are installing from a requirements file, browse for the .txt file."))
        self.label_9.setText(_translate("TabWidget", "Step 3: If you are looking to remove packages, select the remove checkbox."))
        self.label_7.setText(_translate("TabWidget", "Step 1: Browse for the .py file."))
        self.browse_pip_req.setText(_translate("TabWidget", "..."))
        self.browse_pip_from.setText(_translate("TabWidget", "..."))
        self.pip_init.setText(_translate("TabWidget", "..."))
        self.pip_remove_check.setText(_translate("TabWidget", "Remove?"))
        TabWidget.setTabText(TabWidget.indexOf(self.pipinstaller_page), _translate("TabWidget", "Pip Installer"))
        TabWidget.setTabToolTip(TabWidget.indexOf(self.pipinstaller_page), _translate("TabWidget", "Use to Pip install specific modules."))
        self.label_10.setText(_translate("TabWidget", "Step 1: Browse to the directory you wish to create the virtual environment in."))
        self.virtual_init.setText(_translate("TabWidget", "..."))
        self.browse_virtual_to.setText(_translate("TabWidget", "..."))
        self.label_12.setText(_translate("TabWidget", "Step 2: If you choose not to use the default Python installed, browse to the desired Python.exe."))
        self.virtual_new_python.setPlaceholderText(_translate("TabWidget", "...Leave blank if default is desired."))
        self.browse_virtual_python.setText(_translate("TabWidget", "..."))
        TabWidget.setTabText(TabWidget.indexOf(self.virtualenv_page), _translate("TabWidget", "Virtualenv Creator"))
        TabWidget.setTabToolTip(TabWidget.indexOf(self.virtualenv_page), _translate("TabWidget", "Use to create a virtual environment at desired location."))

    def LoadInit(self):
        self.dialog = QtWidgets.QFileDialog()

        # %% QT VARIABLES INIT
        self.ui_location = None
        self.ui_destination = None
        self.ui_resource_location = None
        self.ui_new_name = None

        # %% PYINSTALLER VARIABLES INIT
        self.pyinstaller_location = None
        self.pyinstaller_destination = None
        self.onefile = False
        self.noconsole = False

        # %% PIP INSTALLER VARIABLES INIT

        # %% VIRTUALENV VARIABLES INIT

    # %% QT CONVERSION REGION
    def UiFileLocation(self):
        self.ui_location = self.dialog.getOpenFileName(
                None,
                "Select a .ui File",
                "C:\\",
                "UI Files (*.ui)")[0]
        self.ui_from.setText(self.ui_location)

    def UiDestLocation(self):
        self.ui_destination = self.dialog.getExistingDirectory()
        self.ui_dest.setText(self.ui_destination)

    def UiResourceLocation(self):
        self.ui_resource_location = self.dialog.getOpenFileName(
                None,
                "Select a Resource File",
                "C:\\",
                "Resource Files (*.qrc)")[0]
        self.ui_resource.setText(self.ui_resource_location)

    def UiNameChanged(self, newname):
        self.ui_new_name = newname

    def QtConverInit(self):

        if self.ui_location is None:
            self.ErrorHandler(
                    self.qt_error_lab,
                    "Please Select a .ui File and Destination Location",
                    False)
        else:
            self.ErrorHandler(
                    self.qt_error_lab,
                    "Running",
                    True)
            try:
                QtConverter(
                        uisrc=self.ui_location,
                        pydst=self.ui_destination,
                        resourcesrc=self.ui_resource_location,
                        newname=self.ui_new_name)
            except Exception as e:
                self.ErrorHandler(
                        self.qt_error_lab,
                        "Failed: {0}".format(e),
                        True)
                self.ProgressBarUpdate(
                        self.qt_prog_bar,
                        0,
                        1)
            else:
                self.ErrorHandler(
                        self.qt_error_lab,
                        "Successfully Completed",
                        True)
                self.ProgressBarUpdate(
                        self.qt_prog_bar,
                        1,
                        1)

    # %% PYINSTALLER REGION
    def PyinstallerFrom(self):
        self.pyinstaller_location = self.dialog.getOpenFileName(
                None,
                "Select a .py File",
                "C:\\",
                "Python Files (*.py)")[0]
        self.pyinstaller_from.setText(self.pyinstaller_location)

    def PyinstallerTo(self):
        self.pyinstaller_destination = self.dialog.getExistingDirectory()
        self.pyinstaller_to.setText(self.pyinstaller_destination)

    def PyinstallerOneFile(self, state_):
        if state_ == 0:
            self.onefile = False
        else:
            self.onefile = True

    def PyinstallerNoConsole(self, state_):
        if state_ == 0:
            self.noconsole = False
        else:
            self.noconsole= True

    def PyinstallerInit(self):
        if self.pyinstaller_location is not None:
            PyInstaller(
                    pysrc=self.pyinstaller_location,
                    exedst=self.pyinstaller_destination,
                    onefile=self.onefile,
                    noconsole=self.noconsole)

    # %% ERROR HANDLING
    """Handles Writing Errors to error labels and style"""
    def ErrorHandler(self, label_, text_, good_):
        label_.setText(text_)

        if good_ is True:
            label_.setStyleSheet(
                    """.QLabel{
                    background-color: rgb(0, 255, 0); color: black;}""")
        else:
            label_.setStyleSheet(
                    """.QLabel{
                    background-color: rgb(255, 0, 0); color: black;}""")

    # %% PROGRESS BAR HANDLER
    def ProgressBarUpdate(self, prog_bar, val_, tot_):
        prog_bar.setProperty("value", (val_/tot_)*100)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
