from xgboost import XGBClassifier
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import numpy as np
import xgboost as xgb
from bokeh.models.widgets import Slider, Dropdown, Paragraph, TableColumn, DateFormatter, DataTable, DateSlider
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.layouts import row, column
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

df = pd.read_csv('data_itc.csv')

# Cleaning the data
df = df.dropna(axis=1)

# Splitting data
df['date'] = pd.to_datetime(df['date'])
train = df[df['date'] < '2018-11-13']
y_train = train['label']
X_train = train.drop(['label', 'date'], axis=1)

test = df[df['date'] >= '2018-11-13']
y_test = test['label']
X_test = test.drop(['label', 'date'], axis=1)

# Training model
random_forest_model = RandomForestClassifier(n_estimators=50, max_depth=15)
random_forest_model.fit(X_train, y_train)
random_forest_pp = random_forest_model.predict_proba(X_test)

xg_boost_model = XGBClassifier()
xg_boost_model.fit(X_train, y_train)
xg_boost_pp = xg_boost_model.predict_proba(X_test)


def prediction(predict_proba, threshold):
    y_pred = np.zeros(len(predict_proba))
    for i, pred_prob in enumerate(predict_proba):
        if pred_prob[1] > threshold:
            y_pred[i] = 1
    return y_pred


def X_func(tp, fp):
    return tp / (6 * fp + tp)


threshold_list = np.arange(0.1, 1.05, .05)
function_score_rf = np.array([])
function_score_xg = np.array([])

for threshold in threshold_list:
    y_pred_random_forest = prediction(random_forest_pp, threshold)
    y_pred_xg_boost = prediction(xg_boost_pp, threshold)

    _, fp_rf, _, tp_rf = confusion_matrix(y_test, y_pred_random_forest).ravel()
    _, fp_xg, _, tp_xg = confusion_matrix(y_test, y_pred_xg_boost).ravel()

    function_score_rf = np.append(function_score_rf, X_func(tp_rf, fp_rf))
    function_score_xg = np.append(function_score_xg, X_func(tp_xg, fp_xg))

date_label_xgb = test.copy()[['date', 'label']]
date_label_rf = date_label_xgb.copy()
plots_source = pd.DataFrame(
    columns=['date', 'model', 'threshold', 'precision', 'recall', 'score', 'f1', 'total_samples'])
plots_source['date'] = pd.to_datetime(plots_source['date'])
source = ColumnDataSource(
    data=dict(date=[], model=[], threshold=[], precision=[], recall=[], score=[], f1=[], total_samples=[]))

index = 0
for threshold in threshold_list:
    y_pred_random_forest = prediction(random_forest_pp, threshold)
    date_label_rf['pred'] = y_pred_random_forest
    y_pred_xg_boost = prediction(xg_boost_pp, threshold)
    date_label_xgb['pred'] = y_pred_xg_boost

    for i, date in enumerate(date_label_xgb['date'].unique()):
        t = date_label_xgb[date_label_xgb['date'] == date]
        tn, fp, fn, tp = confusion_matrix(t['label'], t['pred']).ravel()
        precision, recall = tp / (tp + fp), tp / (tp + fn)
        score = X_func(tp, fp)
        f1 = precision * recall * 2 / (precision + recall)
        total_samples = len(t)
        plots_source.loc[index] = [date, 'xgb', threshold, precision, recall, score, f1, total_samples]
        index += 1

    for i, date in enumerate(date_label_rf['date'].unique()):
        t = date_label_rf[date_label_rf['date'] == date]
        tn, fp, fn, tp = confusion_matrix(t['label'], t['pred']).ravel()
        precision, recall = tp / (tp + fp), tp / (tp + fn)
        score = X_func(tp, fp)
        f1 = precision * recall * 2 / (precision + recall)
        total_samples = len(t)
        plots_source.loc[index] = [date, 'rf', threshold, precision, recall, score, f1, total_samples]
        index += 1

plots_source = plots_source.fillna(0)

model_selector = Dropdown(label="Select a model", menu=[('XGBoost', 'xgb'), ('Random Forest', 'rf')], value='xgb')
minimum_date = min(plots_source['date'])
maximum_date = max(plots_source['date'])
start_slider = DateSlider(title='Select start date', value=minimum_date, start=minimum_date,
                          end=maximum_date, step=1)
threshold_slider = Slider(title='Threshold', value=.5, start=.1, end=1, step=.05)

description = Paragraph()
description.text = "You have selected {} model, with threshold {}".format(model_selector.value, threshold_slider.value)


def update(attrname, old, new):
    thr = np.round(threshold_slider.value, 2)
    model = model_selector.value
    start = start_slider.value
    description.text = "You have selected {} model, with threshold {}".format(model.upper(), thr)
    source.data = source.from_df(plots_source[plots_source['date'] >= start]
                                 [plots_source['model'] == model]
                                 [np.round(plots_source['threshold'], 2) == thr])


update(None, None, None)

model_selector.on_change('value', update)
threshold_slider.on_change('value', update)
start_slider.on_change('value', update)

TOOLTIPS = [
    ("(value)", "($y)"),
]

# Plots
plot = figure(plot_width=600, plot_height=300, tooltips=TOOLTIPS)

plot.square(threshold_list, function_score_xg, legend="XGB", fill_color=None, line_color="green")
plot.line(threshold_list, function_score_xg, legend="XGB", line_color="green")

plot.circle(threshold_list, function_score_rf, legend="Random Forrest", fill_color=None)
plot.line(threshold_list, function_score_rf, legend="Random Forrest")

plot.title.text = "Score by Threshold"
plot.xaxis[0].axis_label = 'Threshold'
plot.yaxis[0].axis_label = 'Score'

plot.legend.location = "bottom_right"
plot.legend.border_line_color = "navy"
plot.legend.click_policy = "hide"

precision_recall = figure(plot_width=600, plot_height=300, tooltips=TOOLTIPS, x_axis_type="datetime",
                          title='Precision and Recall')

precision_recall.square('date', 'precision', source=source, legend="Precision", fill_color=None, line_color="green")
precision_recall.line('date', 'precision', source=source, legend="Precision", line_color="green")

precision_recall.square('date', 'recall', source=source, legend="Recall", fill_color=None, line_color="blue")
precision_recall.line('date', 'recall', source=source, legend="Recall", line_color="blue")

precision_recall.legend.location = "bottom_left"
precision_recall.legend.border_line_color = "black"
precision_recall.legend.click_policy = "hide"

f1 = figure(plot_width=600, plot_height=300, x_axis_type="datetime", title="F1 over time", tooltips=TOOLTIPS)
f1.square('date', 'f1', source=source, legend="f1_score", fill_color=None, line_color="red")
f1.line('date', 'f1', source=source, legend="f1_score", line_color="red")

columns = [TableColumn(field="date", title="Date", formatter=DateFormatter()),
           TableColumn(field="precision", title="Precision"),
           TableColumn(field="recall", title="Recall"),
           TableColumn(field="f1", title="F1"),
           TableColumn(field="score", title="Score"),
           TableColumn(field="total_samples", title="Total number of samples")]

data_table = DataTable(source=source, columns=columns, width=500, height=280)

inputs = widgetbox(model_selector, threshold_slider, start_slider, description)
curdoc().add_root(row(inputs, column(plot, precision_recall, f1), column(f1, data_table)))
curdoc().title = "Bruno and Dan"
