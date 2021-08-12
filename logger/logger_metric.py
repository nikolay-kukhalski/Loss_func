import csv
import sys


class CSVLogger:
    
    def __init__(self, file_path: str, metric_key: list):
        self.file_path = file_path + '.csv'
        self.metric_key = metric_key
    

    def log(self, metric_value: list, step: int):
        
        if len(self.metric_key) != len(metric_value):
            print('\n')
            print('The number of metrics does not correspond to the number of values.\nLogging is not possible')
            print('\n')
            sys.exit()

        else:

            dict_1 = {self.metric_key[i]: metric_value[i] for i in range(0, len(self.metric_key), 1)}
            dict_1['epoch'] = step + 1
        
            if step==0:
                with open(self.file_path, 'w', newline='') as csvfile:
                    fieldnames = ['epoch'] + self.metric_key
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
    
            with open(self.file_path, 'a', newline='') as csvfile:
                fieldnames = ['epoch'] + self.metric_key
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(dict_1)
        
