from typing import Optional, Dict

from tensorflow.keras.callbacks import Callback

from logger.logger import Logger


class LoggerCallback(Callback):

    def __init__(self, logger: Logger, field_name_mapping: Optional[Dict[str, str]] = None):
        self._logger = logger
        self._field_name_mapping = field_name_mapping if field_name_mapping is not None \
            else {k: k for k in self._logger.metric_key_list}

    def on_epoch_end(self, epoch, logs: Optional[Dict[str, float]] = None):
        if logs is None:
            # Nothing to log so we just exit.
            return

        self._logger.log(
            metric_value_list=[logs[self._field_name_mapping[mk]] for mk in self._logger.metric_key_list],
            step=epoch)
