

class Header():

    tag = "h"

    def __init__(self, parameters: str = ""):
        self.parameters = parameters

    def get_html(self):
        return "<{0}{params}>  </{0}>".format(self.tag, params=self.parameters)


class LargeHeader(Header):
    def __init__(self):
        Header.__init__(self, " size = 5 ")


class MediumHeader(Header):
    def __init__(self):
        Header.__init__(self, " size = 3 ")


class SmallHeader(Header):
    def __init__(self):
        Header.__init__(self, " size = 1 ")
