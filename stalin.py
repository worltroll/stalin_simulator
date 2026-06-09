import json
import os
class Stalin():
    def __init__(self, pararmetrs):
        self.parametrs = pararmetrs
        self.parametrs['paranoia'] = 30
        self.parametrs['influense'] = 50
        self.parametrs['nkvd'] = 50

        self.events_names = []
        self.events = {}
    def scan(self):
        with open('events_main.json', 'r') as f:
            self.events = json.load(f)
            for i in self.events:
                self.events_names.append(i)
            f.close()
