import json
import os
import random


class Stalin():
    def __init__(self):
        self.parameters = {}

        self.events = []
        self.scan_events()
        self.scan_parameters()

    def scan_events(self):
        with open('saves/events_main.json', 'r') as f:
            self.events = json.load(f)

    def scan_parameters(self):
        with open('saves/parameters.json', 'r') as p:
            self.parameters = json.load(p)

    def r_event(self):
        event = self.events[random.randint(0, len(self.events) - 1)]
        return event

    def save_parameters(self):
        with open('saves/parameters.json', 'w') as f:
            json.dump(self.parameters, f)
