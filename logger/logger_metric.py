import csv

class CSVLogger:
    
    def __init__(self, file_path: str, metric_key: list):
        self._file_path = file_path 
        self._metric_key = metric_key
        self._fieldnames = ['epoch'] + self._metric_key

        if(type(self._file_path)!=str):
            raise Exception('\nParameter "file_path" must be str')

        if self._file_path[-4:] !='.csv':
            self._file_path = file_path + '.csv'

        if(type(metric_key)!=list):
            raise Exception('\nParameter "metric_key" must be list')
                     
        with open(self._file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self._fieldnames)
            writer.writeheader()

    def log(self, metric_value: list, step: int):

        if(type(metric_value)!=list):
            raise Exception('\n\nParameter "metric_value" must be list')

        if len(self._metric_key) != len(metric_value):
                raise Exception('\nThe number of metrics does not correspond to the number of values.\nLogging is not possible')
        
       
        dict_1 = {self._metric_key[i]: metric_value[i] for i in range(0, len(self._metric_key), 1)}
        dict_1['epoch'] = step + 1
            
        with open(self._file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self._fieldnames)
            writer.writerow(dict_1)
        
