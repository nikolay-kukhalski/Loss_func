import csv

class CSVLogger:
    
    def __init__(self, file_path: str):
        self.file_path = file_path + '.csv'
    

    def log(self, metric_key: list, metric_value: list, step: int):

        dict_1 = {metric_key[i]: metric_value[i] for i in range(0, len(metric_key), 1)}
        dict_1['epoch'] = step + 1
        
        if step==0:
            with open(self.file_path, 'w', newline='') as csvfile:
                fieldnames = ['epoch'] + metric_key
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
    
        with open(self.file_path, 'a', newline='') as csvfile:
            fieldnames = ['epoch'] + metric_key
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict_1)
        
