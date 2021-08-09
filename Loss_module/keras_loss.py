import csv
import os
import pandas as pd
import tensorflow as tf

import plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot

# from IPython.display import clear_output # очистка вывода для джуперта

class LossCallback(tf.keras.callbacks.Callback):
    """
    Параметры:
    file_path (str) - имя файла для записи  значений Loss в csv-файл;
    graf_show (boolean, default=False) - выводить ли графики Loss во время обучения после каждой эпохи
    graf_save (str, default=None) - сохранять ли в html-файл интерактивные графики значений Loss

    """

    def __init__(self, file_path: str, graf_show = False, graf_save = None):
        self.file_path = file_path + '.csv'
        self.graf_save = graf_save
        self.graf_show = graf_show
        super().__init__()

        with open(self.file_path, 'w', newline='') as csvfile:
            fieldnames = ['epoch','training_loss', 'test_loss']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
       
        
    def on_epoch_end(self, epoch, logs=None):
        os.system("cls")
#        clear_output(wait=True) #  очистка вывода для джуперта
        
        dict_1 = {'epoch': epoch + 1, 'training_loss': logs["loss"], 'test_loss': logs["val_loss"]}

        with open(self.file_path, 'a', newline='') as csvfile:
            fieldnames = ['epoch','training_loss', 'test_loss']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict_1)

    
        # выведение интерактивного графика обучения
        if self.graf_show is not False:

            df_loss_data = pd.read_csv(self.file_path)

            trace0 = go.Scatter(
                x=df_loss_data['epoch'],
                y=df_loss_data["training_loss"],
                name='loss'
            )

            trace1 = go.Scatter(
                x=df_loss_data['epoch'],
                y=df_loss_data["test_loss"],
                name='val_loss'
            )

            data = [trace0, trace1]
            layout = {'title': 'Result of training model (loss)'}

            fig = go.Figure(data=data, layout=layout)

            iplot(fig, show_link=False)
    
        # сохранение файла html
            if self.graf_save is not None:
                plotly.offline.plot(fig, filename= self.graf_save +'.html', show_link=False, auto_open=False)  