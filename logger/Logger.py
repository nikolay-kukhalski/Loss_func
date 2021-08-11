import csv

class CSVLogger:
    
    def __init__(self, file_path: str):
        self.file_path = file_path + '.csv'
    

    def log(self, metric_key: str, metric_value: float, step: int):

        dict_1 = {'epoch':step + 1, metric_key:metric_value}

        if step==0:
            with open(self.file_path, 'w', newline='') as csvfile:
                fieldnames = ['epoch', metric_key]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
    
        with open(self.file_path, 'a', newline='') as csvfile:
            fieldnames = ['epoch', metric_key]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict_1)
        #pass
