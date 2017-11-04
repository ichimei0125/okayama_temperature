import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

from caltemp import cal_temp


class ProjectUI(QWidget):
    def __init__(self):
        super().__init__()

        self.widgets_x = 30
        self.widgets_y = 50

        self.file_path = ""
        self.method = ""
        self.month = 0

        self.init_browse_file()
        self.init_select_method()
        self.init_select_month()
        self.init_gui()

    def init_browse_file(self):
        # ラベルと選択ウィジェットの位置
        file_x = self.widgets_x
        file_y = self.widgets_y

        # ラベル
        lbl1 = QLabel('Select the file', self)
        lbl1.move(file_x, file_y)

        # ブラウズファイル
        btn = QPushButton('Browse file', self)
        btn.clicked.connect(self.open_file)
        btn.resize(btn.sizeHint())
        btn.move(file_x + 10, file_y + 25)

        self.lbl1 = QLabel(self)
        self.lbl1.move(file_x + 30, file_y + 60)

    def init_select_method(self):
        # ラベルと選択ウィジェットの位置
        method_x = self.widgets_x
        method_y = self.widgets_y + 100

        # ラベル
        lbl1 = QLabel('Select the calculation method', self)
        lbl1.move(method_x, method_y)

        # 計算方法を選択する
        combo_select_method = QComboBox(self)
        combo_select_method.addItem("")
        combo_select_method.addItem("max")
        combo_select_method.addItem("min")
        combo_select_method.addItem("average")
        # combo_select_method.setCurrentIndex("")

        combo_select_method.move(method_x + 10, method_y + 25)

        # 選択したものを下の「def method_activated(self, text):」へ送信する
        combo_select_method.activated[str].connect(self.method_activated)

    def init_select_month(self):  # 月選択の初期化
        # ラベルと選択ウィジェットの位置
        month_x = self.widgets_x
        month_y = self.widgets_y + 200

        # ラベル
        lbl2 = QLabel('Select the month', self)
        lbl2.move(month_x, month_y)

        # 月を選択する
        combo_select_month = QComboBox(self)
        combo_select_month.addItem("")
        combo_select_month.addItem("1")
        combo_select_month.addItem("2")
        combo_select_month.addItem("3")
        combo_select_month.addItem("4")
        combo_select_month.addItem("5")
        combo_select_month.addItem("6")
        combo_select_month.addItem("7")
        combo_select_month.addItem("8")
        combo_select_month.addItem("9")
        combo_select_month.addItem("10")
        combo_select_month.addItem("11")
        combo_select_month.addItem("12")

        combo_select_month.move(month_x + 10, month_y + 25)

        # 選択したものを下の「def month_activated(self, text):」へ送信する
        combo_select_month.activated[str].connect(self.month_activated)

    def init_gui(self):  # ビジュアルの初期化
        self.lbl = QLabel(self)
        self.lbl.move(15, 470)

        btn_cal = QPushButton('calculate', self)
        btn_cal.clicked.connect(self.cal)
        btn_cal.resize(btn_cal.sizeHint())
        btn_cal.move(500, 450)

        btn_quit = QPushButton('Quit', self)
        # btn_quit.clicked.connect(self.close_event)  # メッセージボックス
        btn_quit.clicked.connect(QCoreApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(100, 450)

        self.setGeometry(300, 100, 700, 500)
        self.setWindowTitle('Okayama Temperature')

    def open_file(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Open File",
                                                "./source", "Excel file (*.xls);;All Files (*)"
                                                , options=options)
        if files:
            self.lbl1.setText("File selected")
            self.lbl1.adjustSize()
            self.file_path = files[0]

    def month_activated(self, text):  # 月を選択した後
        self.month = int(text)
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def method_activated(self, text):  # 月を選択した後
        self.method = text
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def cal(self):
        cal_temp(self.file_path, self.method, self.month)

    """
    #  終了するときにメッセージボックスを現れる
    def close_event(self):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProjectUI()
    ex.show()
    sys.exit(app.exec_())
