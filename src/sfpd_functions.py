import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def proportion(value_series):
    return round((value_series / sum(value_series)) * 100, 2)


def series_to_arr(series):
    labels = series.index.astype(str).to_numpy()
    y = series.to_numpy()
    return labels, y


def series_to_pie(ax, series):
    labels, y = series_to_arr(series)
    labels[y/sum(y) < 0.008] = ''
    return ax.pie(y, labels=labels, labeldistance=1.05)


def set_fontsize_for_pie(texts, bigsize, smallsize, smallsize_idx):
    texts[0].set_fontsize(bigsize)
    for i, text in enumerate(texts):  
        if i > smallsize_idx:
            text.set_fontsize(smallsize)


def get_month_hour(data, year):
    month_str = data[data['Incident Year'] == year]['Incident Month'].astype(str)
    hour_str = data['Incident Hour']
    return ('M:'+ month_str +' H:' + hour_str).value_counts().sort_index()