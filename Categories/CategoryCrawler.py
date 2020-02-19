import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen, Request
import re
from Content import Content


class CategoryCrawler:

    def get_internal_links(self, bs, include_url):
        include_url = f'{urlparse(include_url).scheme}://{urlparse(include_url).netloc}'
        internal_links = []

        # search all links starting with '/'
        for link in bs.find('div', id="catgrid").find_all('a',
                                href=re.compile('^(/|.*' + include_url + ')')):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in internal_links:
                    if link.attrs['href'].startswith('/'):
                        internal_links.append(
                            include_url + link.attrs['href'])
                    else:
                        internal_links.append(link.attrs['href'])
        return internal_links

    def get_usable_bs(self, url):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req)
        return BeautifulSoup(html, 'html.parser')
