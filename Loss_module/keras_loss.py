import tensorflow as tf

class LossCallback(tf.keras.callbacks.Callback):
        
    def on_epoch_end(self, epoch, logs=None, name = None):
        import pandas as pd
        import os
        from IPython.display import clear_output # очистка вывода для джуперта
        
        if 'df_loss_data' not in globals():
            global df_loss_data 
            df_loss_data= pd.DataFrame()
        
        os.system("cls")
        clear_output(wait=True) #  очистка вывода для джуперта
        
        dict_1 = {'epoch': epoch + 1, 'training_loss': logs["loss"], 'test_loss': logs["val_loss"]}
        df_loss_data = df_loss_data.append(dict_1, ignore_index=True)
        df_loss_data.to_csv('loss_DF.csv',  encoding='utf-8', index=False)
        print(df_loss_data)
        
        
        from plotly.offline import init_notebook_mode, iplot
        import plotly
        import plotly.graph_objs as go

        init_notebook_mode(connected=True)
    
        # выведение интерактивного графика обучения

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
        if name != None:
            plotly.offline.plot(fig, filename= name +'.html', show_link=False)  