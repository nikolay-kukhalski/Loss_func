from typing import List
from tensorboard.summary import Writer

# importing the parent logger class
from logger_metric.loggers.baselog import Logger


class TBLogger(Logger):
    _STEP_KEY = 'step'

    def __init__(self, dir_path: str, metric_key_list: List[str]):
        self._dir_path = dir_path
        self._metric_key_list = metric_key_list

        # input data types checking
        if not isinstance(self._dir_path, str):
            raise TypeError('Parameter "dir_path" must be str')

        # input data types checking
        if not isinstance(metric_key_list, list):
            raise TypeError('Parameter "metric_key" must be list')

    @property
    def metric_key_list(self) -> List[str]:
        return self._metric_key_list

    def log(self, metric_value_list: List[float], step: int):

        # input data types checking
        if not isinstance(metric_value_list, list):
            raise TypeError('Parameter "metric_value" must be list')

        # checking the accordance of the number of metrics and values
        if len(self._metric_key_list) != len(metric_value_list):
            raise ValueError(
                'The number of metrics does not correspond'
                ' to the number of values.'
                ' Logging is not possible'
                )

        # packaging metrics and their values into a dictionary
        row = {self._metric_key_list[i]: metric_value_list[i]
               for i in range(len(self._metric_key_list))}
        row[self._STEP_KEY] = step

        # creating and writing data to the tensorboard file
        writer = Writer(self._dir_path)
        for k, v in row.items():
            writer.add_scalar(k, v, step)
        writer.close()
