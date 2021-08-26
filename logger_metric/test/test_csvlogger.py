import os
import csv
from logger_metric.loggers import csvlog


def test_csvlog():
# CSV логгирование
    logger = csvlog.CSVLogger(file_path='Loss_tabl', metric_key_list =['Loss', 'Accuracy'])

    loss = {'Loss': 0.123, 'Accuracy': 0.987}

    logger.log(metric_value_list = [loss['Loss'], loss['Accuracy']], step = 1)


    with open(file_path + '.csv') as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for row in reader:
            tabl = row

    assert isinstance(tabl['Loss'], float) == True, 'data type mismatch'
    assert isinstance(tabl['Accuracy'], float) == True, 'data type mismatch'
    assert isinstance(tabl['step'], int) == True, 'data type mismatch'

    if os.path.isfile(file_path + '.csv'):
        os.remove(file_path + '.csv')
