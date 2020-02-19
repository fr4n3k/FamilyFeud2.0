class Content:
    """Common base class for all articles/pages"""

    def __init__(self, url, title):
        self.url = url
        self.title = title

    def print(self):
        print(f'{self.url}')
        print(f'{self.title}')