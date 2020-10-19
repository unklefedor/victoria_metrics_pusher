import logging
import time
import requests
from requests.auth import HTTPBasicAuth


class MetricsPusher:
    def __init__(self, enabled: bool, url: str, user: str, password: str, component: str, dump: bool):
        self.enabled = enabled
        self.dump = dump

        self.url = url
        self.user = user
        self.password = password
        self.component = component

    def push_metric(self, name: str, metric: str, value: float):
        event = Event(self.component, name, metric, value, round(time.time() * 1000))

        if self.dump:
            self.__dump(event)
        else:
            self.__send(event)

    def __dump(self, event):
        logging.debug(event.serialize())

    def __send(self, event):
        if not self.enabled:
            return

        x = requests.post(self.url, json=event.get_obj(), auth=HTTPBasicAuth(self.user, self.password))
        if x.status_code != 200 and x.status_code != 204:
            logging.error("Metrics send failed, status code {:d}".format(x.status_code))
