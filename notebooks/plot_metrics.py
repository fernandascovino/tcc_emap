import plotly.graph_objs as go
import cufflinks as cf

from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

def plot_confusion(y_test, y_pred, labels, title):
    """
    Plota matriz de confusão para os dados de treino e teste (preditos).
    
    y_test, y_pred : np.array
    """

    cfm = confusion_matrix(y_test, y_pred)
    cfm = cfm.astype(float) / cfm.sum(axis=1)[:, np.newaxis]
    
    cfm = pd.DataFrame(cfm).transpose()
    
    x_labels = {'ticktext': list(labels.values()), 'tickvals': list(labels.keys()), 'title': 'Predito'}
    y_labels = {'autorange': 'reversed', 'ticktext': list(labels.values()), 'tickvals': list(labels.keys()), 'title': 'Real'}

    cfm.iplot(kind='heatmap', colorscale='Blues', filename='cufflinks/simple-heatmap', 
             layout={'xaxis': x_labels, 'yaxis': y_labels, 'title': title})

def plot_roc(y_test, y_score, title):
    """
    Plota a curva ROC para os dados de treino e teste (preditos).
    
    y_test, y_score : np.array
    title : str
    """
    
    # Compute ROC curve and ROC area for each class
    fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=1)
    roc_auc = auc(fpr, tpr)

    ref = np.linspace(0,1)

    data = [go.Scatter(x=ref, y=ref, mode='markers', showlegend=False), 
              go.Scatter(x=fpr, y=tpr, mode='lines', name='ROC curve (area = %0.2f)' % roc_auc)]

    layout = dict(xaxis=dict(title='Especificidade: VN/(VP+VN)'), yaxis=dict(title='Sensibilidade: VP/(VP+VN)'), 
                  title=title)

    fig = go.Figure(data, layout)
    cf.iplot(fig)