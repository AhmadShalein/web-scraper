import requests
from bs4 import BeautifulSoup

url ='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    response = requests.get(url)
    # html_text = response.text
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    results_list = list(results)
    return (len(results_list))


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    result_one = soup.find('div', class_='mw-parser-output')
    result_text = []
    para = result_one.find_all('p')
    for i in para:
        k = i.find('span', string = lambda text: 'citation needed' in text)
        if k:
            result_text.append(i.text.strip())
    for a in result_text:
        print(a)
        print('-' * 15)
        return result_text

if __name__ == '__main__':
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))