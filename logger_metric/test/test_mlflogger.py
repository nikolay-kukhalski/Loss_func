import mlflow
import shutil

from logger_metric.loggers import mlflog


def test_mlflog():
    # test variables
    dir_path = 'mlruns5'
    step = 1

    # importing a module for a test
    logger = mlflog.MLFLogger(dir_path=dir_path,
                              metric_key_list=['Loss', 'Accuracy'])

    # simulation of the values of the model training metrics
    with mlflow.start_run(run_name='MLFLogger') as run:
        run = mlflow.active_run()
        loss = {'Loss': 0.123, 'Accuracy': 0.987}
        logger.log(metric_value_list=[loss['Loss'],
                   loss['Accuracy']],
                   step=step)
        tracking_uri = mlflow.get_tracking_uri()

    mistake_tblogger = 'data type mismatch or the inequality of values'

    # reading metrics from a file
    # test of written data in the test file metric Loss
    path = tracking_uri + '/0/' + run.info.run_id + '/metrics/Loss'
    with open(path) as f:
        content = f.readlines()
    metrics_for_step = [float(x.split(' ')[1]) for x in content]

    assert round(metrics_for_step[0], 3) == loss['Loss'], mistake_tblogger

    # test of written data in the test file metric Accuracy
    path = tracking_uri + '/0/' + run.info.run_id + '/metrics/Accuracy'
    with open(path) as f:
        content = f.readlines()
    metrics_for_step = [float(x.split(' ')[1]) for x in content]

    assert round(metrics_for_step[0], 3) == loss['Accuracy'], mistake_tblogger

    # delete test file and folder
    shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
