import matplotlib.pyplot as plt
import numpy as np
from funcs import month_to_str
from PIL import Image


def draw_picture(day, data, month, key):
    if key == 1:
        type = "average"
    if key == 2:
        type = "max"
    if key == 3:
        type = "min"

    month = month_to_str(month)

    # 見やすため
    y_max = np.amax(data) + 5
    y_min = np.amin(data) - 5

    title = "The " + type + " temperature of Okayama in " + month
    plt.title(title)
    plt.xlabel("date")
    plt.ylabel("temperature")

    plt.ylim(y_min, y_max)

    plt.plot(day, data, '^', day, data)

    save_path = "./output/"
    save_name = save_path + month + "_" + type + ".png"
    plt.savefig(save_name, dpi=120, format='png')

    # plt.show()  # pyqt5と連携するときに、バグがある

    image = Image.open(save_name)
    image.show()
