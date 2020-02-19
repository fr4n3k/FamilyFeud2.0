from Content import Content
from Website import Website
from TitleCrawler import TitleCrawler
from CategoryCrawler import CategoryCrawler

def main():
    url = 'https://www.thetoptens.com/lists/'
    category_crawler = CategoryCrawler()
    bs = category_crawler.get_usable_bs(url)
    list_of_links = category_crawler.get_internal_links(bs, url)
    title_crawler = TitleCrawler()

    site_data = ['thetoptens',
                 'http://www.thetoptens.com/lists/',
                 'h1']
    TITLE = 0
    SITE_URL = 1
    TITLETAG = 2

    websites = {}
    for link in list_of_links:
        websites[link] = Website(site_data[TITLE], site_data[SITE_URL], site_data[TITLETAG])

    title_url_dict = {}
    for link, website in websites.items():
        title_url_tuple = title_crawler.save(website, link)
        title_url_dict[title_url_tuple[0]] = title_url_tuple[1]

    return title_url_dict


if __name__ == '__main__':
    main()
