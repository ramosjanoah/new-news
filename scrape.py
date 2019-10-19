from model.content import Content
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pdb

HTML_TAG_REMOVER = re.compile('<.*?>')

def remove_html_tag(str_):
    return re.sub(HTML_TAG_REMOVER, '', str_)

def scrape_page_detik(url_string):
    """
        return content model
    """

    print("Scrapping from " + url_string)
    page = urlopen(url_string)
    content = page.read()
    soup = BeautifulSoup(content, 'html.parser')

    params = {}
    params['title'] = soup.find('title').text

    body = str(soup.find('div', {'class': 'itp_bodycontent'})).split('<br><br/>')[0]
    body = body.replace('<br/>', '\n')
    body = remove_html_tag(body)
    params['body'] = body
    params['url'] = url_string

    return Content(params)
