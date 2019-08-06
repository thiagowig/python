
class Client():

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @staticmethod
    def from_dict(source):
        client = Client(source[u'first'], source[u'last'])

        return client


    def to_dict(self):
        dest = {
            u'first': self.first,
            u'last': self.last
        }

    def __repr__(self):
        return (
            u'City(first={}, last={}'.format(self.first, self.last)
        )