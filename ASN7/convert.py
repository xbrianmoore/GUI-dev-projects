# converter.py
# Student: Brian Moore | Project: Assignment 7 (PySide6)

import os
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QMessageBox, QFrame, QSizePolicy
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

INCH_TO_METER = 0.0254


def inches_to_meters(inches: float) -> float:
    return inches * INCH_TO_METER


def meters_to_inches(meters: float) -> float:
    return meters / INCH_TO_METER


class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Converter App")
        self._build_ui()
        self._wire_events()
        self._reset_form()

    def _build_ui(self):
        central = QWidget(self)
        self.setCentralWidget(central)
        central.setStyleSheet("background: #e8820a;")

        # title label
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.lblTitle.setFont(QFont("Arial", 22, QFont.Bold))
        self.lblTitle.setStyleSheet("color: #1a0000; background: transparent;")

        # prompt label
        self.lblPrompt = QLabel("Enter a value and\nchoose conversion")
        self.lblPrompt.setFont(QFont("Arial", 13, QFont.Bold))
        self.lblPrompt.setStyleSheet("color: #1a0000; background: transparent;")

        # numeric input box
        self.txtInput = QLineEdit()
        self.txtInput.setFixedWidth(90)
        self.txtInput.setFixedHeight(34)
        self.txtInput.setFont(QFont("Arial", 13))
        self.txtInput.setAlignment(Qt.AlignCenter)
        self.txtInput.setStyleSheet(
            "background: #b85c00; color: white; padding: 4px; border: none;"
        )
        self.txtInput.setPlaceholderText("e.g. 10")

        # radio group
        self.grp = QGroupBox("Convert Measurement")
        self.grp.setFont(QFont("Arial", 11, QFont.Bold))
        self.grp.setStyleSheet("""
            QGroupBox {
                color: white;
                background: #b85c00;
                border: 2px solid #ffcc88;
                border-radius: 4px;
                margin-top: 18px;
                padding: 8px 16px 8px 8px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                color: white;
            }
            QRadioButton {
                color: white;
                font-size: 13px;
                background: transparent;
            }
            QRadioButton::indicator {
                width: 13px;
                height: 13px;
                border-radius: 7px;
                border: 2px solid white;
                background: transparent;
            }
            QRadioButton::indicator:checked {
                background: #000000;
                border: 2px solid white;
            }
        """)
        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")
        vgrp = QVBoxLayout()
        vgrp.setSpacing(6)
        vgrp.addWidget(self.rbInToM)
        vgrp.addWidget(self.rbMToIn)
        self.grp.setLayout(vgrp)

        # result label
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setFont(QFont("Arial", 14))
        self.lblResult.setStyleSheet("color: #1a0000; background: transparent;")

        # house image
        self.imgFrame = QFrame()
        self.imgFrame.setFixedSize(200, 180)
        self.imgFrame.setStyleSheet("background: white; border: 2px solid #ffcc88;")
        self.imgLabel = QLabel(self.imgFrame)
        self.imgLabel.setAlignment(Qt.AlignCenter)
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "house.png")
        pix = QPixmap(img_path)
        self.imgLabel.setPixmap(
            pix.scaled(190, 170, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        vimg = QVBoxLayout(self.imgFrame)
        vimg.setContentsMargins(4, 4, 4, 4)
        vimg.addWidget(self.imgLabel)

        # buttons
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")
        btn_style = """
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                padding: 8px 20px;
                background: #e8820a;
                color: #1a0000;
                border: 2px solid #1a0000;
            }
            QPushButton:hover { background: #ffaa44; }
            QPushButton:pressed { background: #000000; color: #1a0000; }
        """
        for btn in (self.btnConvert, self.btnClear, self.btnExit):
            btn.setStyleSheet(btn_style)
            btn.setFixedHeight(42)

        # grid layout
        grid = QGridLayout(central)
        grid.setContentsMargins(16, 16, 16, 12)
        grid.setSpacing(12)

        grid.addWidget(self.lblTitle,   0, 0, 1, 2)
        grid.addWidget(self.lblPrompt,  1, 0)
        grid.addWidget(self.txtInput,   1, 1)
        grid.addWidget(self.grp,        2, 0, 1, 2)
        grid.addWidget(self.lblResult,  3, 0, 1, 2)
        grid.addWidget(self.imgFrame,   0, 2, 4, 1, Qt.AlignTop)

        hbtns = QHBoxLayout()
        hbtns.addStretch(1)
        hbtns.addWidget(self.btnConvert)
        hbtns.addWidget(self.btnClear)
        hbtns.addWidget(self.btnExit)
        grid.addLayout(hbtns,           4, 0, 1, 3)

    def _wire_events(self):
        self.btnConvert.clicked.connect(self.on_convert)
        self.btnClear.clicked.connect(self.on_clear)
        self.btnExit.clicked.connect(QApplication.instance().quit)

    def _reset_form(self):
        self.txtInput.clear()
        self.lblResult.clear()
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def _error(self, message: str):
        QMessageBox.critical(self, "Error", message)

    def on_clear(self):
        self._reset_form()

    def on_convert(self):
        text = self.txtInput.text().strip()

        # check non-empty
        if not text:
            self._error("Please enter a value.")
            return

        # check numeric
        try:
            value = float(text)
        except ValueError:
            self._error("Value entered is not numeric.")
            return

        # check positive
        if value <= 0:
            self._error("Value must be positive.")
            return

        if self.rbInToM.isChecked():
            result = inches_to_meters(value)
            if result < 0:
                self._error("Converted value is negative.")
                return
            # format matches rubric example: "12.0 inches = 0.305 meters"
            self.lblResult.setText(f"{value:.3f} inches = {result:.3f} meters")
        else:
            result = meters_to_inches(value)
            if result < 0:
                self._error("Converted value is negative.")
                return
            self.lblResult.setText(f"{value:.3f} meters = {result:.3f} inches")


def main():
    app = QApplication(sys.argv)
    w = ConverterWindow()
    w.resize(720, 320)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()