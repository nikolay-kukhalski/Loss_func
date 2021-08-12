import csv

from typing import List 

class CSVLogger:
    
    def __init__(self, file_path: str, metric_key: List[str]):
        self._file_path = file_path 
        self._metric_key = metric_key
        self._fieldnames = ['epoch'] + self._metric_key

        if not isinstance(self._file_path, str):
            raise TypeError('\nParameter "file_path" must be str')

        if self._file_path[-4:] !='.csv':
            self._file_path = file_path + '.csv'

        if not isinstance(metric_key, list):
            raise TypeError('\nParameter "metric_key" must be list')
                     
        with open(self._file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self._fieldnames)
            writer.writeheader()

    def log(self, metric_value: List[float], step: int):

        if not isinstance(metric_value, list):
            raise TypeError('\n\nParameter "metric_value" must be list')

        if len(self._metric_key) != len(metric_value):
                raise ValueError('\nThe number of metrics does not correspond to the number of values.\nLogging is not possible')
        
       
        dict_1 = {self._metric_key[i]: metric_value[i] for i in range(0, len(self._metric_key), 1)}
        dict_1['epoch'] = step + 1
            
        with open(self._file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self._fieldnames)
            writer.writerow(dict_1)
        
