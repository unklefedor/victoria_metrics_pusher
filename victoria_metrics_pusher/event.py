import json


class Event:
    def __init__(self, component: str, task: str, name: str, value: float, time: int):
        self.event = {
            "metric": {
                "__name__": 'ml_py_{:s}'.format(component),
                "job": task,
                "metric": name
            },
            "values": [
                value
            ],
            "timestamps": [
                time
            ]
        }

    def serialize(self):
        return json.dumps(self.event)

    def get_obj(self):
        return self.event
