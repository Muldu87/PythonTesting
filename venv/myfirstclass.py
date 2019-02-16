from myfirstclass import MyFirstClass


class MyFirstClass(object):
    def __init__(self, first_val: str, post: int):
        self.first_val = first_val
        self.port = post

    def create(self) -> Myfirst:
        return Myfirst(
            [{'first_val': self.first_val, 'post': self.post}]
        )



