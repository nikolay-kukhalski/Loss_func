import csv

from typing import List

# importing the parent logger class
from logger_metric.loggers.baselog import Logger


class CSVLogger(Logger):
    _STEP_KEY = 'step'

    def __init__(self, file_path: str, metric_key_list: List[str]):
        self._file_path = file_path
        self._metric_key_list = metric_key_list

        # input data types checking
        if not isinstance(self._file_path, str):
            raise TypeError('Parameter "file_path" must be str')

        # checking whether the file has an extension for logging
        if self._file_path[-4:] != '.csv':
            self._file_path = file_path + '.csv'

        # input data types checking
        if not isinstance(metric_key_list, list):
            raise TypeError('Parameter "metric_key" must be list')

        # creating and writing data to the csv-file
        with open(self._file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=[self._STEP_KEY] + metric_key_list
                )
            writer.writeheader()

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

        # adding data to the csv-file
        with open(self._file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=[self._STEP_KEY] + self._metric_key_list
                )
            writer.writerow(row)
