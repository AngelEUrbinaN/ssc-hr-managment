import sys
import os
import shutil

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QGridLayout, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

# Import the UI class from the 'quinquenio_ui' module
from sections.quinquenio import QuinquenioWidget

# Import the UI class from the 'main_ui' module
from ui_files.main_ui import Ui_MainWindow

# Define a custom MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize UI elements
        self.title_label = self.ui.title_label
        self.title_label.setText("Licencias")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap("./assets/icon/icon.svg"))
        self.title_icon.setScaledContents(False)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.menu_btn = self.ui.pushButton
        self.menu_btn.setObjectName("menu_btn")
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("./assets/icon/close.svg"))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

        self.main_content = self.ui.stackedWidget

        self.menu_list = [
            {
                "name": "Quinquenio",
                "icon": "./assets/icon/quinquenio.svg",
            },
            {
                "name": "Lactancia",
                "icon": "./assets/icon/lactancia.svg",
            },
            {
                "name": "Vacaciones",
                "icon": "./assets/icon/vacaciones.svg",
            },
            {
                "name": "Permisos",
                "icon": "./assets/icon/permisos.svg",
            },
            {
                "name": "Modif. Vacaciones",
                "icon": "./assets/icon/modif.svg",
            },
            {
                "name": "Movimiento",
                "icon": "./assets/icon/movimiento.svg",
            },
            {
                "name": "Tiempo X Tiempo",
                "icon": "./assets/icon/tiempo.svg",
            },
            {
                "name": "Accidente",
                "icon": "./assets/icon/accidente.svg",
            },
        ]

        self.init_list_widget()
        self.init_single_slot()
        self.init_stackwidget()

        # Set the actions of the menu bar
        self.ui.actionAgregar_base_de_datos.triggered.connect(self.import_main_db)
        self.ui.actionExportar_Base_de_Datos.triggered.connect(self.export_main_db)
        os.makedirs("data", exist_ok=True)

        # Set the initial state of the side menu
        initial_state = self.menu_btn.isChecked()
        self.side_menu.setHidden(initial_state)
        self.title_label.setHidden(initial_state)
        self.title_icon.setHidden(initial_state)
        self.side_menu_icon_only.setVisible(initial_state)

    def init_single_slot(self):
        # Connect signals and slots for menu button and side menu
        self.menu_btn.toggled["bool"].connect(self.side_menu.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title_label.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title_icon.setHidden)
        self.menu_btn.toggled["bool"].connect(self.side_menu_icon_only.setVisible)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged["int"].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged["int"].connect(self.side_menu.setCurrentRow)

        self.menu_btn.toggled.connect(self.button_icon_change)

    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.menu_btn.setIcon(QIcon("./assets/icon/menu.svg"))
        else:
            self.menu_btn.setIcon(QIcon("./assets/icon/close.svg"))

    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu.clear()
        self.side_menu_icon_only.clear()

        for menu in self.menu_list:
            # Set items for the side menu with icons only
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)

            # Set items for the side menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)

    def init_stackwidget(self):
        # Initialize the stack widget with content page
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        self.main_content.addWidget(QuinquenioWidget())     # index 0
        self.main_content.addWidget(QWidget())              # Lactancia (por ahora vacío)
        self.main_content.addWidget(QWidget())              # Vacaciones
        self.main_content.addWidget(QWidget())              # Permisos
        self.main_content.addWidget(QWidget())              # Modif. Vacaciones
        self.main_content.addWidget(QWidget())              # Movimiento
        self.main_content.addWidget(QWidget())              # Tiempo X Tiempo
        self.main_content.addWidget(QWidget())              # Accidente

    def import_main_db(self):
        # Import the main (employees) database
        db_file, _ = QFileDialog.getOpenFileName(self, "Importar Base de Datos", "", "Archivos Excel (*.xlxs *.xlsx)")

        if db_file:
            try:
                shutil.copyfile(db_file, "./data/main.db")
                QMessageBox.information(self, "Importar Base de Datos", "Base de Datos importada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Importar Base de Datos", f"Error al importar la Base de Datos: {str(e)}")

    def export_main_db(self):
        # Export the main (employees) database
        current_dir = os.path.join("data", "main.db")

        if not os.path.exists(current_dir):
            QMessageBox.critical(self, "Exportar Base de Datos", "No se pudo encontrar la Base de Datos.")
            return

        new_dir = QFileDialog.getSaveFileName(self, "Exportar Base de Datos", "", "Archivos Excel (*.xlxs *.xlsx)")[0]

        if new_dir:
            try:
                shutil.copyfile(current_dir, new_dir)
                QMessageBox.information(self, "Exportar Base de Datos", "Base de Datos exportada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Exportar Base de Datos", f"Error al exportar la Base de Datos: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load style file
    with open("./assets/style.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())