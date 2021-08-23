import mlflow
from typing import List
from logger_metric.loggers.baselog import Logger


class MLFLogger(Logger):
    _STEP_KEY = 'step'

    def __init__(self, dir_path: str, metric_key_list: List[str]):
        self._dir_path = dir_path
        self._metric_key_list = metric_key_list

        if not isinstance(self._dir_path, str):
            raise TypeError('Parameter "dir_path" must be str')

        if not isinstance(metric_key_list, list):
            raise TypeError('Parameter "metric_key" must be list')

        mlflow.set_tracking_uri("file:///" + self._dir_path)
        mlflow.create_experiment(
            name=self._dir_path + '_Project',
            artifact_location=self._dir_path
            )

    @property
    def metric_key_list(self) -> List[str]:
        return self._metric_key_list

    def log(self, metric_value_list: List[float], step: int):
        if not isinstance(metric_value_list, list):
            raise TypeError('Parameter "metric_value" must be list')

        if len(self._metric_key_list) != len(metric_value_list):
            raise ValueError(
                'The number of metrics does not correspond'
                ' to the number of values.'
                ' Logging is not possible'
                )

        row = {self._metric_key_list[i]: metric_value_list[i]
               for i in range(len(self._metric_key_list))}

        mlflow.log_metrics(row, step=step)
