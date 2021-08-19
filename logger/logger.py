from abc import ABC, abstractmethod
from typing import List

class Logger(ABC):

    @property
    @abstractmethod
    def metric_key_list(self) -> List[str]:
        pass
    
    @abstractmethod
    def log(self, metric_value_list: List[float], step: int):
        pass