import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import csv

DOWNLOAD_DIRECTORY = "categories/"
BASE_URL = "https://www.thetoptens.com/"


def get_category_name():
    category_name = input('What category would You like to download?')
    return category_name


def get_category_url(category_name):
    category_url = BASE_URL + category_name + '/'
    return category_url


def check_if_category_exists(category_url):
    request = requests.get(category_url)
    return request.status_code == 200


def download_category_html(category_url):
    req = Request(category_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    answers_html = bs.find_all('div', class_="i")
    return answers_html


def extract_category_answers(answers_html):
    max_answers = 10
    answers_list = []
    for html in answers_html[:max_answers]:
        answers_list.append(html.find('b').text)
    return answers_list


def save_category_in_csv(category_name, answer_list):
    file_name = DOWNLOAD_DIRECTORY+category_name+'.csv'
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(answer_list)


def main():
    category_name = get_category_name()
    url = get_category_url(category_name)

    if check_if_category_exists(url):
        html = download_category_html(url)
        list_of_answers = extract_category_answers(html)
        save_category_in_csv(category_name, list_of_answers)
    else:
        print("There is no such category")
