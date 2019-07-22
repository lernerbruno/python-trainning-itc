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
df['date'] = pd.to_datetime(df['date'])
df = df.dropna(axis=1)
train = df[df['date'] < '2018-11-13']
test = df[df['date'] >= '2018-11-13']
X_train = train.drop(['label', 'date'], axis=1)
X_test = test.drop(['label', 'date'], axis=1)
y_train = train['label']
y_test = test['label']

xgb_ = xgb.XGBClassifier()
xgb_.fit(X_train, y_train)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

proba_xgb = xgb_.predict_proba(X_test)
proba_rf = rf.predict_proba(X_test)


def func_to_maximize(tp, fp):
    return tp/(6*fp + tp)


threshold = np.arange(0.1, 1, 0.01)
score_xgb = []
score_rf = []
for th in threshold:
    y_pred_xgb = [1 if p[1] > th else 0 for p in proba_xgb]
    _, fp, _, tp = confusion_matrix(y_test, y_pred_xgb).ravel()
    score_xgb.append(func_to_maximize(tp, fp) * 100)

    y_pred_rf = [1 if p[1] > th else 0 for p in proba_rf]
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred_rf).ravel()
    score_rf.append(func_to_maximize(tp, fp) * 100)


pred_xgb = test.copy()
pred_xgb = pred_xgb[['date', 'label']]
pred_rf = test.copy()
pred_rf = pred_rf[['date', 'label']]
final = pd.DataFrame(columns=['date', 'model', 'threshold', 'precision', 'recall', 'f1', 'score', 'num_obs'])
i = 0
for th in threshold:
    y_pred_xgb = [1 if p[1] >= th else 0 for p in proba_xgb]
    pred_xgb['pred'] = y_pred_xgb
    for j, date in enumerate(pred_xgb['date'].unique()):
        temp = pred_xgb[pred_xgb['date'] == date]
        tn, fp, fn, tp = confusion_matrix(temp['label'], temp['pred']).ravel()
        precision, recall = tp/(tp+fp), tp/(tp+fn)
        f1 = precision*recall*2/(precision + recall)
        num_obs = len(temp)
        score = func_to_maximize(tp, fp)
        final.loc[i] = [date, 'xgb', np.round(th, 2), precision, recall, f1, score, num_obs]
        i += 1

for th in threshold:
    y_pred_rf = [1 if p[1] >= th else 0 for p in proba_rf]
    pred_rf['pred'] = y_pred_rf
    for j, date in enumerate(pred_rf['date'].unique()):
        temp = pred_rf[pred_rf['date'] == date]
        tn, fp, fn, tp = confusion_matrix(temp['label'], temp['pred']).ravel()
        precision, recall = tp/(tp+fp), tp/(tp+fn)
        f1 = precision*recall*2/(precision + recall)
        num_obs = len(temp)
        score = func_to_maximize(tp, fp)
        final.loc[i] = [date, 'rf', np.round(th, 2), precision, recall, f1, score, num_obs]
        i += 1

final = final.fillna(0)
TOOLTIPS_1 = [
    ("(threshold, score)", "($x, $y)"),
]

plot = figure(plot_width=600, plot_height=300, tooltips=TOOLTIPS_1)

plot.square(threshold, score_xgb, legend="XGB", fill_color=None, line_color="green")
plot.line(threshold, score_xgb, legend="XGB", line_color="green")

plot.circle(threshold, score_rf, legend="Random Forrest", fill_color=None)
plot.line(threshold, score_rf, legend="Random Forrest")

plot.title.text = "Score Threshold graph "
plot.xaxis[0].axis_label = 'Threshold'
plot.yaxis[0].axis_label = 'Score (%)'

plot.legend.location = "bottom_right"
plot.legend.border_line_color = "navy"
plot.legend.click_policy = "hide"


output = Paragraph()
output2 = Paragraph()
output2.text = 'Mouse over the lines, click on the legend to remove a line'

threshold = Slider(title="Threshold", value=0.1, start=0.1, end=0.9, step=0.01)

model_menu = [("Random Forest", 'rf'), None, ("XGBoost", 'xgb')]
model_dropdown = Dropdown(label="Model", button_type="warning", menu=model_menu, value='rf')

start_date = DateSlider(title='Start date',
                        value=min(final['date']),
                        start=min(final['date']),
                        end=max(final['date']),
                        step=1)

end_date = DateSlider(title='End date',
                      value=max(final['date']),
                      start=min(final['date']),
                      end=max(final['date']),
                      step=1)

output.text = model_dropdown.value + ' with a threshold ' + str(threshold.value)

source = ColumnDataSource(data=dict(date=[], model=[], precision=[], recall=[], f1=[], score=[], num_obs=[]))


TOOLTIPS = [
    ("(value)", "($y)"),
]

precision_recall = figure(plot_width=600, plot_height=300, tooltips=TOOLTIPS, x_axis_type="datetime",
                          title='Precision and Recall')

precision_recall.square('date', 'precision', source=source, legend="Precision", fill_color=None, line_color="green")
precision_recall.line('date', 'precision', source=source, legend="Precision", line_color="green")

precision_recall.square('date', 'recall', source=source, legend="Recall", fill_color=None, line_color="blue")
precision_recall.line('date', 'recall', source=source, legend="Recall", line_color="blue")

precision_recall.legend.location = "bottom_left"
precision_recall.legend.border_line_color = "black"
precision_recall.legend.click_policy="hide"


f1 = figure(plot_width=600, plot_height=300, x_axis_type="datetime", title="F1 over time", tooltips=TOOLTIPS)
f1.square('date', 'f1', source=source, legend="f1_score", fill_color=None, line_color="red")
f1.line('date', 'f1', source=source, legend="f1_score", line_color="red")

score_graph = figure(plot_width=600,
                     plot_height=300,
                     x_axis_type="datetime",
                     title="Score to maximize",
                     tooltips=TOOLTIPS)

score_graph.circle('date', 'score', source=source, legend="Score", size=10, color="firebrick", alpha=0.5)

columns = [TableColumn(field="date", title="Date", formatter=DateFormatter()),
           TableColumn(field="precision", title="Precision"),
           TableColumn(field="recall", title="Recall"),
           TableColumn(field="f1", title="F1"),
           TableColumn(field="score", title="Score"),
           TableColumn(field="num_obs", title="Observation")]

data_table = DataTable(source=source, columns=columns, width=500, height=280)


def update_data(attrname, old, new):
    thr = np.round(threshold.value, 2)
    model = model_dropdown.value
    start = start_date.value
    end = end_date.value
    output.text = model.upper() + ' with a threshold of ' + str(thr)
    source.data = source.from_df(final[final['date'] >= start]
                                 [final['date'] <= end]
                                 [final['model'] == model]
                                 [final['threshold'] == thr])


update_data(None, None, None)

model_dropdown.on_change('value', update_data)
threshold.on_change('value', update_data)
start_date.on_change('value', update_data)
end_date.on_change('value', update_data)

# source.on_change('value', update_data)

importance = pd.DataFrame(xgb_.feature_importances_, index=X_train.columns,
                          columns=['importance_xgb']).sort_values('importance_xgb', ascending=False)

importance = importance.reset_index()
importance.columns = ['features_model', 'xgb']

source_2 = ColumnDataSource(data=dict(features=[], xgb=[], rf=[]))
source_2.data = source_2.from_df(importance)

columns_2 = [TableColumn(field="features_model", title="Features"), TableColumn(field="xgb", title="XGBoost")]

data_table_2 = DataTable(source=source_2, columns=columns_2, width=400, height=280)

importance = pd.DataFrame(rf.feature_importances_, index=X_train.columns,
                          columns=['importance_rf']).sort_values('importance_rf', ascending=False)

importance = importance.reset_index()
importance.columns = ['features_model', 'rf']

source_3 = ColumnDataSource(data=dict(features=[], xgb=[], rf=[]))
source_3.data = source_3.from_df(importance)

columns_3 = [TableColumn(field="features_model", title="Features"), TableColumn(field="rf", title="Random Forest")]

data_table_3 = DataTable(source=source_3, columns=columns_3, width=400, height=280)


inputs = widgetbox(model_dropdown, threshold, start_date, end_date, output, output2)
