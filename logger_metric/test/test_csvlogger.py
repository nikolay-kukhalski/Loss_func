import os
import csv
from logger_metric.loggers import csvlog


def test_csvlog():
    # test variables
    file_path = 'Loss_tabl'
    step = 1

    # importing a module for a test
    logger = csvlog.CSVLogger(file_path=file_path,
                              metric_key_list=['Loss', 'Accuracy'])

    # simulation of the values of the model training metrics
    loss = {'Loss': 0.123, 'Accuracy': 0.987}
    logger.log(metric_value_list=[loss['Loss'],
               loss['Accuracy']],
               step=step
               )

    # reading metrics from a file
    with open(file_path + '.csv') as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for row in reader:
            tabl = row

    mistake_csvlogger = 'data type mismatch or the inequality of values'

    # test of written data in the test file
    assert float(tabl['Loss']) == loss['Loss'], mistake_csvlogger
    assert float(tabl['Accuracy']) == loss['Accuracy'], mistake_csvlogger
    assert int(tabl['step']) == step, mistake_csvlogger

    # delete test file
    if os.path.isfile(file_path + '.csv'):
        os.remove(file_path + '.csv')
