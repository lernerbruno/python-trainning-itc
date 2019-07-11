from numpy.random import random

import pandas as pd

from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.models.widgets import Select, TextInput

from bokeh.io import curdoc

from bokeh.models import ColumnDataSource

from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression

from collections import defaultdict

from sklearn.metrics import f1_score
from bokeh.palettes import Category10_10

from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown

import json

from datetime import datetime, timedelta

from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource
from bokeh.models import DatetimeTickFormatter
from math import pi
from bokeh.models import Legend

from sklearn.metrics import roc_curve, auc

from bokeh.models.widgets import TextInput, Button, Paragraph

STARTING_DATE = '23/10/2017'
N = 60
TRAIN_DAYS = 40
TEST_DAYS = N - TRAIN_DAYS


def get_data(path):
    with open(path, 'r') as f:
        res = json.load(f)

    with open('dates.json', 'r') as f:
        dates = json.load(f)

    dates = [datetime.strptime(date, '%d/%m/%Y') for date in dates]

    data = defaultdict(list)

    for i, (k, v) in enumerate(res.items()):
        data['time'].append(dates)
        data['models'].append(k)
        data['f1'].append(v)
        data['color'].append(Category10_10[i])

    return data


def get_f1s():
    source = ColumnDataSource(data=get_data('results.json'))

    p = figure(x_axis_type="datetime", title="F1 scores")

    p.xaxis[0].formatter.days = '%d/%m/%Y'

    p.multi_line(xs='time', ys='f1', legend="models",
                 line_width=5, line_color='color', line_alpha=0.6,
                 hover_line_color='color', hover_line_alpha=1.0,
                 source=source)

    p.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[
        ('Model', '@models'),
        ('F1', '$data_y')]))

    p.legend.location = "center_left"
    p.legend.orientation = "vertical"

    return p


def get_roc_data(path, model, d):
    with open(path, 'r') as f:
        rocs = json.load(f)
    return {'x': rocs[model][d][0], 'y': rocs[model][d][1]}


def make_date_menu(dates):
    date_list = []
    for i, date in enumerate(dates):
        date_list.append((date, date))
    return date_list


def run():
    output = Paragraph()

    f1 = get_f1s()

    with open('dates.json', 'r') as f:
        dates = json.load(f)

    model_menu = [("Random Forest", 'RF'), None, ("Logistic regression", 'LR'), None, ("SVM", 'SVM')]
    model_dropdown = Dropdown(label="Model", button_type="warning", menu=model_menu, value='RF')

    date_menu = make_date_menu(dates)
    date_dropdown = Dropdown(label="Date", button_type='primary', menu=date_menu, value='13/11/2017')

    output.text = model_dropdown.value + ' on the ' + date_dropdown.value

    def update(attr, old, new):
        model = model_dropdown.value
        d = date_dropdown.value

        output.text = model + ' on the ' + d
        source.data = get_roc_data('rocs.json', model, dates.index(d))

    model_dropdown.on_change('value', update)
    date_dropdown.on_change('value', update)

    roc = figure()

    source = ColumnDataSource(data=get_roc_data('rocs.json', 'RF', 5))

    roc.line('x', 'y', source=source)

    layout = row(f1, column(row(model_dropdown, date_dropdown), output, roc))

    curdoc().add_root(layout)


def test():
    output = Paragraph()

    button = Button(label="Say HI")

    layout = column(output, button)

    curdoc().add_root(layout)

run()
#test()