import plotly.graph_objs as go
import cufflinks as cf

from sklearn.metrics import roc_curve, auc, precision_recall_curve, confusion_matrix, classification_report
import numpy as np
import pandas as pd

from sklearn.metrics import matthews_corrcoef
from scipy.stats import pointbiserialr, pearsonr

colorscale = ['#025951', '#8BD9CA', '#BF7F30', '#F2C124', '#8C470B', '#DFC27D']

def plot_bin_corr(df, columns, title, margin=dict(l=250, b=150, r=100)):
    """
    Plota a matriz de correlação de variáveis binárias (Chi / Pearson).
    """

    corr_indicadoras = pd.DataFrame(index=columns, columns=columns)

    for i in columns:
        for j in columns:
            
            corr_indicadoras[i][j] = pearsonr(df[i], df[j])[0]
#             if len(df[j].unique()) > 2: # contínua x binária
#                 corr_indicadoras[i][j] = pointbiserialr(df[i], df[j])
                
#             elif len(df[i].unique()) > 2: # contínua x binária
#                 corr_indicadoras[i][j] = pointbiserialr(df[j], df[i])
                
#             else: # binária x binária
#                 corr_indicadoras[i][j] = matthews_corrcoef(df[i], df[j])   
            
    corr_indicadoras.iplot(kind='heatmap', margin=margin,
                           colorscale='brbg', title=title, center_scale=0, theme='white')
    
def plot_confusion(y_test, y_pred, labels, title):
    """
    Plota matriz de confusão para os dados de treino e teste (preditos).
    
    y_test, y_pred : numpy.array
    """

    cfarray = confusion_matrix(y_test, y_pred)
    cfm = cfarray.astype(float) / cfarray.sum(axis=1)[:, np.newaxis]
    
    cfm = pd.DataFrame(cfm).transpose()
    
    x_labels = {'ticktext': list(labels.values()), 'tickvals': list(labels.keys()), 'title': 'Predito'}
    y_labels = {'autorange': 'reversed', 'ticktext': list(labels.values()), 'tickvals': list(labels.keys()), 'title': 'Real'}

    cfm.iplot(kind='heatmap', colorscale='blues', filename='cufflinks/simple-heatmap', 
             layout={'xaxis': x_labels, 'yaxis': y_labels, 'title': title}, theme='white')
    
    print(classification_report(y_test, y_pred, target_names=labels.values()))
    return cfarray

def plot_roc(y_test, y_score, title, colors=colorscale):
    """
    Plota a curva ROC para os dados de treino e teste (preditos).
    
    y_test : numpy.array
    y_score : pandas.DataFrame (scores dos modelos a serem comparados)
    
    title : str
    """
    
    ref = np.linspace(0,1)
    data = [go.Scatter(x=ref, y=ref, mode='markers', marker=dict(color='grey'), showlegend=False)]
    
    i = 0
    for model in y_score.columns:
        # Compute ROC curve and ROC area for each class
        fpr, tpr, _ = roc_curve(y_test, y_score[model], pos_label=1)
        roc_auc = auc(fpr, tpr)

        data.append(go.Scatter(x=fpr, y=tpr, mode='lines', 
                               marker=dict(color=colors[i]), 
                               name='{} (area = {})'.format(model, round(roc_auc, 2))))
        i +=1

    layout = dict(xaxis=dict(title='Especificidade: VN/(FP+FN)'), 
                  yaxis=dict(title='Sensibilidade: VP/(VP+FN)'), 
                  title=title)

    fig = go.Figure(data, layout)
    cf.iplot(fig)
    
from sklearn.metrics import precision_score, recall_score
from tqdm import tqdm_notebook as tqdm

def calculate_prec_recall(df, feature=None, n_limits=100):
    """
    Calcula precision e recall escolhendo iterando o threshold pela lista ordenada da prob. dos alunos.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe da prob e indicadora de evasao por aluno
        
    feature: str
        Feature para ordenação dos alunos (default=None, i.e., ordena pela probabilidade)
        
    n_limits : int
        Número de pontos percentuais (default=100)
        
    Returns
    -------
    precision, recall : lists
    
    """
    n_alunos = list(range(1, len(df)))
    
    if feature:
        df = df.sort_values(feature, ascending=False)
     
    else:
        # Ordenando pelas prob (decrescente)
        df = df.sort_values('prob', ascending=False)

    # Indice da linha ordenada
    df['idx'] = range(len(df)) 
    
    # Lista de limites 
    limits = np.linspace(1, len(df), n_limits)

    # Calculo das metricas
    precision=[]
    recall = []
    
    for i in tqdm(limits):
        # Classificando como evadidos probs acima do limite
        pred = df['idx'].map(lambda x: 1 if x < i else 0)
        precision.append(precision_score(df['in_evasao'], pred))
        recall.append(recall_score(df['in_evasao'], pred))
    
    t = pd.DataFrame(list(zip(limits/len(df), precision, recall)), 
                     columns=['perc_cover', 'precision', 'recall'])
    return t
    
def plot_cover(df_cover, df_cover_rand, label_rand, title='Percentual de cobertura'):
    """
    Plota a curva de precisão-recall para comparação de duas métricas de ordenamento dos alunos (ex: probabilidade de evasão do modelo e idade)
    
    df_cover, df_cover_rand : pandas.DataFrame
        Tabelas ordenadas com a métrica de ordenação, precision e recall (gerada pela função calculate_prec_recall)
        
    label_rand, title : str
        Nome do modelo de comparação (ex: random, idade) e titulo de grafico, respectivamente
    """

    # Plot
    data = [go.Scatter(x=df_cover_rand['perc_cover'], 
                       y=df_cover_rand['precision'], 

                       mode='markers', marker=dict(color=colorscale[1], opacity=.7), name='Precision ({})'.format(label_rand)), 
            go.Scatter(x=df_cover_rand['perc_cover'], 
                       y=df_cover_rand['recall'], 
                       mode='markers', marker=dict(color=colorscale[5], opacity=.7), name='Recall ({})'.format(label_rand)),

            go.Scatter(x=df_cover['perc_cover'], 
                       y=df_cover['precision'], 
                       mode='lines', marker=dict(color=colorscale[0]), name='Precision'), 
            go.Scatter(x=df_cover['perc_cover'], 
                       y=df_cover['recall'], 
                       mode='lines', marker=dict(color=colorscale[4]), name='Recall')
           ]

    layout = dict(xaxis=dict(title='% de alunos cobertos (ordenado pela prob. de evasão)'), title=title)
    fig = go.Figure(data, layout)
    cf.iplot(fig)