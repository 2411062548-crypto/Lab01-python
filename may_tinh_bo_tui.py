import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, 
    QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Máy tính bỏ túi")
        self.resize(300, 400)
        main_layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 5px;")
        main_layout.addWidget(self.display)
        grid_layout = QGridLayout()
        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2, 1, 2)  # Nút '=' kéo dài 2 cột
        ]
        for btn_info in buttons:
            if len(btn_info) == 3:
                text, row, col = btn_info
                row_span, col_span = 1, 1
            else:
                text, row, col, row_span, col_span = btn_info

            button = QPushButton(text)
            button.setFixedHeight(50)
            button.setStyleSheet("font-size: 16px; font-weight: bold;")
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col, row_span, col_span)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.setText("")
        elif text == '=':
            try:
                bieu_thuc = self.display.text()
                ket_qua = eval(bieu_thuc)
                self.display.setText(str(ket_qua))
            except Exception:
                self.display.setText("Lỗi")
        else:
            if self.display.text() == "Lỗi":
                self.display.setText(text)
            else:
                self.display.setText(self.display.text() + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MayTinhBoTui()
    window.show()
    sys.exit(app.exec_())