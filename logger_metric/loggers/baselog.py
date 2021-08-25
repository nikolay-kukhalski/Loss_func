from abc import ABC, abstractmethod
from typing import List


class Logger(ABC):

    # getting a list of metrics
    @property
    @abstractmethod
    def metric_key_list(self) -> List[str]:
        pass

    # logging metric values at each step
    @abstractmethod
    def log(self, metric_value_list: List[float], step: int):
        pass
