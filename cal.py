import numpy as np
from funcs import return_value


def cal(data, month, key, path):
    # 入力の月により、データを取り出す
    data_wanted = np.array([])

    for i in range(len(data[:, 0])):
        data_month = return_value(path, data[i, 0], "month")

        if data_month == month:
            data_wanted = np.append(data_wanted, data[i, key])

    return data_wanted

"""
min = np.amin(行列)  # 行列の中に、最小値を探す
man = np.amax(行列)  # 行列の中に、最大値を探す
average = np.sum(行列) / len(行列)  # 行列の中に、平均値を探す
"""
