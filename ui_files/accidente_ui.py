# Form implementation generated from reading ui file './ui_files/accidente.ui'
#
# Created by: PyQt6 UI code generator 6.9.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(557, 583)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.registrar_btn = QtWidgets.QPushButton(parent=Form)
        self.registrar_btn.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.registrar_btn.setAutoDefault(False)
        self.registrar_btn.setDefault(False)
        self.registrar_btn.setFlat(False)
        self.registrar_btn.setObjectName("registrar_btn")
        self.gridLayout.addWidget(self.registrar_btn, 10, 0, 1, 3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.descanso_label = QtWidgets.QLabel(parent=Form)
        self.descanso_label.setObjectName("descanso_label")
        self.verticalLayout_5.addWidget(self.descanso_label)
        self.descanso_input = QtWidgets.QDateEdit(parent=Form)
        self.descanso_input.setObjectName("descanso_input")
        self.verticalLayout_5.addWidget(self.descanso_input)
        self.gridLayout.addLayout(self.verticalLayout_5, 5, 2, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fecha_aviso_label = QtWidgets.QLabel(parent=Form)
        self.fecha_aviso_label.setObjectName("fecha_aviso_label")
        self.verticalLayout_8.addWidget(self.fecha_aviso_label)
        self.fecha_aviso_input = QtWidgets.QDateEdit(parent=Form)
        self.fecha_aviso_input.setObjectName("fecha_aviso_input")
        self.verticalLayout_8.addWidget(self.fecha_aviso_input)
        self.gridLayout.addLayout(self.verticalLayout_8, 6, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.inf_emp_label = QtWidgets.QLabel(parent=Form)
        self.inf_emp_label.setObjectName("inf_emp_label")
        self.horizontalLayout_8.addWidget(self.inf_emp_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.no_emp_label = QtWidgets.QLabel(parent=Form)
        self.no_emp_label.setObjectName("no_emp_label")
        self.horizontalLayout_7.addWidget(self.no_emp_label)
        self.no_emp_input = QtWidgets.QLineEdit(parent=Form)
        self.no_emp_input.setObjectName("no_emp_input")
        self.horizontalLayout_7.addWidget(self.no_emp_input)
        self.nombre_label = QtWidgets.QLabel(parent=Form)
        self.nombre_label.setObjectName("nombre_label")
        self.horizontalLayout_7.addWidget(self.nombre_label)
        self.nombre_input = QtWidgets.QLineEdit(parent=Form)
        self.nombre_input.setReadOnly(True)
        self.nombre_input.setObjectName("nombre_input")
        self.horizontalLayout_7.addWidget(self.nombre_input)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cege_label = QtWidgets.QLabel(parent=Form)
        self.cege_label.setObjectName("cege_label")
        self.horizontalLayout_9.addWidget(self.cege_label)
        self.cege_input = QtWidgets.QLineEdit(parent=Form)
        self.cege_input.setReadOnly(False)
        self.cege_input.setObjectName("cege_input")
        self.horizontalLayout_9.addWidget(self.cege_input)
        self.area_label = QtWidgets.QLabel(parent=Form)
        self.area_label.setObjectName("area_label")
        self.horizontalLayout_9.addWidget(self.area_label)
        self.area_input = QtWidgets.QLineEdit(parent=Form)
        self.area_input.setReadOnly(True)
        self.area_input.setObjectName("area_input")
        self.horizontalLayout_9.addWidget(self.area_input)
        self.categoria_label = QtWidgets.QLabel(parent=Form)
        self.categoria_label.setObjectName("categoria_label")
        self.horizontalLayout_9.addWidget(self.categoria_label)
        self.categoria_input = QtWidgets.QLineEdit(parent=Form)
        self.categoria_input.setReadOnly(True)
        self.categoria_input.setObjectName("categoria_input")
        self.horizontalLayout_9.addWidget(self.categoria_input)
        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 0, 1, 3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horario_label = QtWidgets.QLabel(parent=Form)
        self.horario_label.setObjectName("horario_label")
        self.verticalLayout_6.addWidget(self.horario_label)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.de_label = QtWidgets.QLabel(parent=Form)
        self.de_label.setObjectName("de_label")
        self.horizontalLayout_12.addWidget(self.de_label)
        self.horario_input_1 = QtWidgets.QTimeEdit(parent=Form)
        self.horario_input_1.setCurrentSection(QtWidgets.QDateTimeEdit.Section.HourSection)
        self.horario_input_1.setObjectName("horario_input_1")
        self.horizontalLayout_12.addWidget(self.horario_input_1)
        self.a_label = QtWidgets.QLabel(parent=Form)
        self.a_label.setObjectName("a_label")
        self.horizontalLayout_12.addWidget(self.a_label)
        self.horario_input_2 = QtWidgets.QTimeEdit(parent=Form)
        self.horario_input_2.setObjectName("horario_input_2")
        self.horizontalLayout_12.addWidget(self.horario_input_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout_6, 5, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.aceptacion_label = QtWidgets.QLabel(parent=Form)
        self.aceptacion_label.setObjectName("aceptacion_label")
        self.verticalLayout_9.addWidget(self.aceptacion_label)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.aceptacion_si_button = QtWidgets.QRadioButton(parent=Form)
        self.aceptacion_si_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.aceptacion_si_button.setObjectName("aceptacion_si_button")
        self.horizontalLayout_11.addWidget(self.aceptacion_si_button)
        self.aceptacion_no_button = QtWidgets.QRadioButton(parent=Form)
        self.aceptacion_no_button.setObjectName("aceptacion_no_button")
        self.horizontalLayout_11.addWidget(self.aceptacion_no_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout_9, 6, 2, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lugar_label = QtWidgets.QLabel(parent=Form)
        self.lugar_label.setObjectName("lugar_label")
        self.horizontalLayout_13.addWidget(self.lugar_label)
        self.lugar_input = QtWidgets.QLineEdit(parent=Form)
        self.lugar_input.setObjectName("lugar_input")
        self.horizontalLayout_13.addWidget(self.lugar_input)
        self.gridLayout.addLayout(self.horizontalLayout_13, 7, 0, 1, 3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hora_label = QtWidgets.QLabel(parent=Form)
        self.hora_label.setObjectName("hora_label")
        self.verticalLayout_4.addWidget(self.hora_label)
        self.hora_input = QtWidgets.QTimeEdit(parent=Form)
        self.hora_input.setObjectName("hora_input")
        self.verticalLayout_4.addWidget(self.hora_input)
        self.gridLayout.addLayout(self.verticalLayout_4, 5, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(4, 5, 4, 5)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.title_accidente_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_accidente_label.setFont(font)
        self.title_accidente_label.setObjectName("title_accidente_label")
        self.horizontalLayout_6.addWidget(self.title_accidente_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 3)
        self.q_table_layout = QtWidgets.QVBoxLayout()
        self.q_table_layout.setContentsMargins(-1, 5, -1, 5)
        self.q_table_layout.setObjectName("q_table_layout")
        self.table_label = QtWidgets.QLabel(parent=Form)
        self.table_label.setObjectName("table_label")
        self.q_table_layout.addWidget(self.table_label)
        self.table_display = QtWidgets.QTableWidget(parent=Form)
        self.table_display.setObjectName("table_display")
        self.table_display.setColumnCount(0)
        self.table_display.setRowCount(0)
        self.q_table_layout.addWidget(self.table_display)
        self.gridLayout.addLayout(self.q_table_layout, 9, 0, 1, 3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fecha_prt_label = QtWidgets.QLabel(parent=Form)
        self.fecha_prt_label.setObjectName("fecha_prt_label")
        self.verticalLayout_7.addWidget(self.fecha_prt_label)
        self.fecha_prt_input = QtWidgets.QDateEdit(parent=Form)
        self.fecha_prt_input.setObjectName("fecha_prt_input")
        self.verticalLayout_7.addWidget(self.fecha_prt_input)
        self.gridLayout.addLayout(self.verticalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.comentarios_label = QtWidgets.QLabel(parent=Form)
        self.comentarios_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.comentarios_label.setObjectName("comentarios_label")
        self.horizontalLayout_14.addWidget(self.comentarios_label)
        self.comentarios_input = QtWidgets.QTextEdit(parent=Form)
        self.comentarios_input.setPlaceholderText("")
        self.comentarios_input.setObjectName("comentarios_input")
        self.horizontalLayout_14.addWidget(self.comentarios_input)
        self.gridLayout.addLayout(self.horizontalLayout_14, 8, 0, 1, 3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.inf_inf_label = QtWidgets.QLabel(parent=Form)
        self.inf_inf_label.setObjectName("inf_inf_label")
        self.horizontalLayout_10.addWidget(self.inf_inf_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_10, 4, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.registrar_btn.setText(_translate("Form", "Registrar"))
        self.descanso_label.setText(_translate("Form", "Día de descanso"))
        self.fecha_aviso_label.setText(_translate("Form", "Fecha de aviso al CEGE"))
        self.inf_emp_label.setText(_translate("Form", "Información del Empleado"))
        self.no_emp_label.setText(_translate("Form", "No. Empleado"))
        self.nombre_label.setText(_translate("Form", "Nombre"))
        self.cege_label.setText(_translate("Form", "CEGE"))
        self.cege_input.setText(_translate("Form", "S.S.C"))
        self.area_label.setText(_translate("Form", "Área"))
        self.categoria_label.setText(_translate("Form", "Categoría"))
        self.horario_label.setText(_translate("Form", "Horario de trabajo"))
        self.de_label.setText(_translate("Form", "De"))
        self.horario_input_1.setDisplayFormat(_translate("Form", "hh:mm"))
        self.a_label.setText(_translate("Form", "A"))
        self.horario_input_2.setDisplayFormat(_translate("Form", "hh:mm"))
        self.aceptacion_label.setText(_translate("Form", "Aceptación del P.R.T"))
        self.aceptacion_si_button.setText(_translate("Form", "Sí"))
        self.aceptacion_no_button.setText(_translate("Form", "No"))
        self.lugar_label.setText(_translate("Form", "Lugar del accidente"))
        self.hora_label.setText(_translate("Form", "Hora del accidente"))
        self.hora_input.setDisplayFormat(_translate("Form", "hh:mm"))
        self.title_accidente_label.setText(_translate("Form", "Accidente de Trabajo"))
        self.table_label.setText(_translate("Form", "Registros recientes"))
        self.fecha_prt_label.setText(_translate("Form", "Fecha de P.R.T"))
        self.comentarios_label.setText(_translate("Form", "Comentarios"))
        self.comentarios_input.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Se anexa formato de calificación de probable accidente de trabajo ST- 7 y tarjeta informativa</p></body></html>"))
        self.inf_inf_label.setText(_translate("Form", "Información del Informe"))
