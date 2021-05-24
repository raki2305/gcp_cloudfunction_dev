"""
Sample class for the context object of the cloud function. Please instantiate in main_local.py if needed.
"""


class Context:
    def __init__(self, event_Id, timestamp, event_type, resource):
        self.event_Id = event_Id
        self.timestamp = timestamp
        self.event_type = event_type
        self.resource = resource
