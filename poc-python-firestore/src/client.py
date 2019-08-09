import json
from dataclasses import dataclass

@dataclass
class Client():

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


    @staticmethod
    def from_dict(source):
        client = Client(source[u'first'], source[u'last'], source[u'age'])

        return client


    @staticmethod
    def to_dict(id, source):
        dest = {
            u'id': id,
            u'first': source.first,
            u'last': source.last,
            u'age': source.age
        }

        return dest


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


    def __repr__(self):
        return (
            u'Client(first={}, last={}'.format(self.first, self.last)
        )