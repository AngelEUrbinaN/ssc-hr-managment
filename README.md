# License Manager – SSCG

This is a desktop application developed in **Python** using **PyQt6** and **Qt Designer**, created for the **Human Resources Department of SSCG**. The program streamlines and automates the generation of employee licenses and permissions across multiple categories.

## 🧩 Overview

The application allows users to register, consult, and manage various types of administrative **licenses** or **permissions** granted to staff. Each section is represented in a sidebar menu, with individual views for:

- **Quinquenio**
- **Lactancia**
- **Vacaciones**
- **Permisos**
- **Modificación de Periodo Vacacional**
- **Movimiento de Personal**
- **Tiempo por Tiempo**
- **Accidente de Trabajo**

Each module is tailored to capture specific data and can export structured records to Excel or pre-designed Word templates.

## ⚙️ Technologies Used

- **Python 3**
- **PyQt6**
- **Qt Designer**
- **pandas** – data handling
- **python-docx** – Word document generation
- **openpyxl** – Excel read/write

## 📁 Project Structure

```plaintext
ssc-hr-managment/
├── assets/                # Good use of static files
│   ├── icon/
│   └── style.qss
│
├── data/                  # Excellent for internal data handling
│   ├── database/
│   └── templates/
│
├── sections/              # Contains logic for different UI sections
│   ├── quinquenio.py
│   └── quinquenio_ui.py   # Optional if generated code kept close
│
├── ui_files/              # Source `.ui` and generated `.py` files
│   ├── main.ui
│   ├── main_ui.py
│   ├── quinquenio.ui
│   └── quinquenio_ui.py   # (may be redundant with sections/ copy)
│
├── .gitignore
├── main.py
└── README.md