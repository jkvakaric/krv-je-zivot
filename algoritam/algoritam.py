import pandas as pd
import importlib.util


spec = importlib.util.spec_from_file_location("module.name", "constants.py")
constants = importlib.util.module_from_spec(spec)
spec.loader.exec_module(constants)
donors = pd.read_csv('donors.csv', sep=',', header=None)


def loss_function(o_min, o_max, x, r):
    if x <= o_min:
        return 200 / r * (o_min - x) + 35
    if o_min < x <= r / 3 + o_min:
        return 100 / r * (o_min + r / 3 - x)
    if r / 3 + o_min < x <= 2 * r / 3 + o_min:
        return 0
    if 2 / r * 3 + o_min < x <= o_max:
        return 100 / r * (x - 2 * r / 3 - o_min)
    return 200 / r * (x - o_max) + 35


def loss_function_sum():







