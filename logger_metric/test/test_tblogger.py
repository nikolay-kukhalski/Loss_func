import shutil
from tensorboard.backend.event_processing import event_accumulator
from logger_metric.loggers import tblog


def test_tblog():
    # test variables
    dir_path = 'TB_metric'
    step = 1

    # importing a module for a test
    logger = tblog.TBLogger(dir_path='TB_metric',
                            metric_key_list=['Loss', 'Accuracy'])

    # simulation of the values of the model training metrics
    loss = {'Loss': 0.123, 'Accuracy': 0.987}
    logger.log(metric_value_list=[loss['Loss'],
               loss['Accuracy']],
               step=step
               )

    # reading metrics from a file
    ea = event_accumulator.EventAccumulator(dir_path)
    ea.Reload()

    mistake_tblogger = 'data type mismatch or the inequality of values'

    # test of written data in the test file
    assert round(ea.Tensors('Loss')[0][2].float_val[0], 3) == loss['Loss'], mistake_tblogger
    assert round(ea.Tensors('Accuracy')[0][2].float_val[0], 3) == loss['Accuracy'], mistake_tblogger
    assert round(ea.Tensors('step')[0][2].float_val[0], 0) == step, mistake_tblogger

    # delete test file and folder
    shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
