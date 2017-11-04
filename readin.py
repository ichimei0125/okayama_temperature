"""
文字を入れずに読み込む
"""
import numpy as np
import xlrd


def read_file(path):
    excel_file = path  # 入力のパス

    book = xlrd.open_workbook(excel_file)
    sheet_1 = book.sheet_by_index(0)

    cols = sheet_1.ncols  # 列数
    rows = sheet_1.nrows  # 行数

    # 追加する配列の要素数は初期化して、行の長さ（列数）と一致させる
    data_excel = np.empty((0, cols))

    for row in range(rows):
        data_excel_tmp = np.array([])  # しばらく、各行のデータをdata_excel_tmpに読み込む

        for col in range(cols):
            cell = sheet_1.cell_value(row, col)
            cell_type = sheet_1.cell_type(row, col)

            # 先頭のセルタイプを読み出して、文字列(1)と空白(0)を読み飛ばす
            if cell_type != 1 and cell_type != 0:
                data_excel_tmp = np.append(data_excel_tmp, cell)

        # 列を加える
        if data_excel_tmp.size != 0:
            data_excel = np.append(data_excel, [data_excel_tmp], axis=0)

    return data_excel

# read_file("./source/OkayamaTemp2016.xls")
