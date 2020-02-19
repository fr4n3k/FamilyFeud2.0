import requests
from bs4 import BeautifulSoup
from Content import Content


class TitleCrawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exception.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """Utility function to acquire string from
        BeautifulSoup object and selector. Returns empty
        if found none."""
        selectedElements = pageObj.select(selector)
        if selectedElements is not None and len(selectedElements) > 0:
            return '\n'.join(
                [elem.get_text() for elem in selectedElements])
        return ''

    def parse(self, site, url):
        """Get text from url"""
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            if title != '':
                content = Content(url, title)
                content.print()

    def save(self, site, url):
        """Get text from url"""
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            if title != '':
                content = Content(url, title)
                return content.title, content.url

