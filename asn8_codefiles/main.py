# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt

from ui_asn8 import Ui_root


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set up ui
        self.ui = Ui_root()
        self.ui.setupUi(self)
        self.setWindowTitle("Personal Information Form")

        # connect buttons
        self.ui.btnS.clicked.connect(self.handle_submit)
        self.ui.btnR.clicked.connect(self.handle_reset)
        self.ui.btnQ.clicked.connect(self.handle_quit)

    def handle_submit(self):
        first_name = self.ui.entFirst.text().strip()
        last_name  = self.ui.entLast.text().strip()
        email      = self.ui.entEmail.text().strip()
        phone      = self.ui.entPhone.text().strip()

        # validate required fields
        if not first_name or not last_name:
            missing = []
            if not first_name:
                missing.append("First Name")
            if not last_name:
                missing.append("Last Name")
            QMessageBox.warning(
                self,
                "Validation Error",
                "The following required field(s) are empty:\n  • " + "\n  • ".join(missing)
            )
            return

        QMessageBox.information(
            self,
            "Submission Successful",
            f"Data submitted successfully!\n\n"
            f"Name  : {first_name} {last_name}\n"
            f"Email : {email  if email  else '(not provided)'}\n"
            f"Phone : {phone  if phone  else '(not provided)'}"
        )

    def handle_reset(self):
        # clear all fields
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

    def handle_quit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())