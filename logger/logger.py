import csv

from abc import ABC, abstractmethod
from tensorflow import summary
from typing import List

class Logger(ABC):

    @property
    @abstractmethod
    def metric_key_list(self) -> List[str]:
        pass
    
    @abstractmethod
    def log(self, metric_value_list: List[float], step: int):
        pass


class CSVLogger(Logger):
    _STEP_KEY = 'step'

    def __init__(self, file_path: str, metric_key_list: List[str]):
        self._file_path = file_path 
        self._metric_key_list = metric_key_list

        if not isinstance(self._file_path, str):
            raise TypeError('Parameter "file_path" must be str')

        if self._file_path[-4:] !='.csv':
            self._file_path = file_path + '.csv'

        if not isinstance(metric_key_list, list):
            raise TypeError('Parameter "metric_key" must be list')
                     
        with open(self._file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[self._STEP_KEY] + metric_key_list)
            writer.writeheader()

    @property
    def metric_key_list(self) -> List[str]:
        return self._metric_key_list
 
    def log(self, metric_value_list: List[float], step: int):
        if not isinstance(metric_value_list, list):
            raise TypeError('Parameter "metric_value" must be list')

        if len(self._metric_key_list) != len(metric_value_list):
                raise ValueError('The number of metrics does not correspond to the number of values. Logging is not possible')
       
        row = {self._metric_key_list[i]: metric_value_list[i] for i in range(len(self._metric_key_list))}
        row[self._STEP_KEY] = step
            
        with open(self._file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[self._STEP_KEY] + self._metric_key_list)
            writer.writerow(row)


class TBLogger(Logger):
    _STEP_KEY = 'step'

    def __init__(self, dir_path: str, metric_key_list: List[str]):
        self._dir_path = dir_path 
        self._metric_key_list = metric_key_list

        if not isinstance(self._dir_path, str):
            raise TypeError('Parameter "dir_path" must be str')

        if not isinstance(metric_key_list, list):
            raise TypeError('Parameter "metric_key" must be list')

    @property
    def metric_key_list(self) -> List[str]:
        return self._metric_key_list
 
    def log(self, metric_value_list: List[float], step: int):
        if not isinstance(metric_value_list, list):
            raise TypeError('Parameter "metric_value" must be list')

        if len(self._metric_key_list) != len(metric_value_list):
                raise ValueError('The number of metrics does not correspond to the number of values. Logging is not possible')
       
        row = {self._metric_key_list[i]: metric_value_list[i] for i in range(len(self._metric_key_list))}
        row[self._STEP_KEY] = step
        
        test_summary_writer = summary.create_file_writer(self._dir_path)
        for k,v in row.items():
            with test_summary_writer.as_default():
                summary.scalar(k, v, step)