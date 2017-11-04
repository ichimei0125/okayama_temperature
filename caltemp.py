from readin import read_file
from cal import cal
from printout import draw_picture
from funcs import return_value


class CalData:
    def __init__(self, path, mon, keyword):
        self.path = path
        self.month = mon
        self.key = keyword

    def read_data(self):
        return read_file(self.path)

    def calculate_data(self, data_cal):
        return cal(data_cal, self.month, self.key, self.path)

    def output_data(self, day_draw, data_draw):
        draw_picture(day_draw, data_draw, self.month, self.key)


"""
# gui不要の場合
if __name__ == '__main__':

    # デバッグするため
    path_of_excel_file = "./source/OkayamaTemp2016.xls"
    calculate_type = "max"
    month = 12

    # コマンドラインから入力する
    print("Please input file path")
    path_of_excel_file = input()
    print("Please input which calculate method you want, average, max, min")
    calculate_type = input()
    print("Please input the month which you want to draw")
    month = int(input())
    
"""


def cal_temp(path, method, month):  # gui.pyを使用するため

    # gui.pyから三つのパラメーターをもらう
    path_of_excel_file = path
    calculate_type = method
    month = month

    # 以下はgui.pyと関係ない
    if calculate_type == "average":
        key = 1
    if calculate_type == "max":
        key = 2
    if calculate_type == "min":
        key = 3

    calculation = CalData(path_of_excel_file, month, key)  # 初期化

    # データを読み込む
    data = calculation.read_data()

    # 入力の月と計算のタイプにより、データを取り出す
    data_wanted = calculation.calculate_data(data)

    # 出力
    day = []
    for i in range(len(data[:, 0])):
        month_wanted = return_value(path_of_excel_file, data[i, 0], "month")

        if month_wanted == month:
            day_tmp = return_value(path_of_excel_file, data[i, 0], "day")
            day.append(day_tmp)

    # return (day, data_wanted)

    calculation.output_data(day, data_wanted)
