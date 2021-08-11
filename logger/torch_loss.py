import csv
import os
import pandas as pd

import plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot

# from IPython.display import clear_output # очистка вывода для джуперта

class LossTorch:
    """
    Параметры:

    file_path (str) - имя файла для записи  значений Loss в csv-файл;
    metric_key (str) - название метрики для сохранение в файл и отображения на графике;
    graf_show (boolean, default=False) - выводить ли графики Loss во время обучения после каждой эпохи;
    graf_save (str, default=None) - сохранять ли в html-файл интерактивные графики значений Loss.
    
    """

    def __init__(self, file_path: str, metric_key:str, graf_show = False, graf_save = None):
        self.file_path = file_path + '.csv'
        self.metric_key = metric_key
        self.graf_save = graf_save
        self.graf_show = graf_show
   
    def log(self, epoch:int, loss):
        os.system("cls")
#        clear_output(wait=True) #  очистка вывода для джуперта
        
        dict_1 = {'epoch': epoch + 1, 'loss': loss.item()}

        if epoch==0:
            with open(self.file_path, 'w', newline='') as csvfile:
                fieldnames = ['epoch','loss']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        with open(self.file_path, 'a', newline='') as csvfile:
            fieldnames = ['epoch','loss']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict_1)

    
        # выведение интерактивного графика обучения
        if self.graf_show is not False:

            df_loss_data = pd.read_csv(self.file_path)

            trace0 = go.Scatter(
                x=df_loss_data['epoch'],
                y=df_loss_data["loss"],
                name='loss'
            )

            # trace1 = go.Scatter(
            #     x=df_loss_data['epoch'],
            #     y=df_loss_data["test_loss"],
            #     name='val_loss'
            # )

            data = [trace0] #, trace1]
            layout = {'title': 'Result of training model. ' + self.metric_key}

            fig = go.Figure(data=data, layout=layout)

            iplot(fig, show_link=False)
    
        # сохранение файла html
            if self.graf_save is not None:
                plotly.offline.plot(fig, filename= self.graf_save +'.html', show_link=False, auto_open=False)  