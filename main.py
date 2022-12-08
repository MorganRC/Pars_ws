from bs4 import BeautifulSoup
import requests

def file_save():
    with open('kz_pars.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price: {comp["ad-price"]} -> Link: {comp["link"]}\n')
def kz_pars():
    url = 'https://www.olx.kz/d/elektronika/noutbuki-i-aksesuary/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
        'Accept':'*/*'
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all('div', class_='css-19ucd76')
    comps = []


    for item in items:
        if item is None:
            continue
        comps.append({
            'title': item.find('a', class_='css-1bbgabe').get_text(strip=True) if item.find('a',
                                                                                            class_='css-1bbgabe') is not None else 'None',
            'ad-price': item.find('p', class_='css-1q7gvpp-Text eu5v0x0').get_text(strip=True) if item.find('p',
                                                                                                            class_='css-1q7gvpp-Text eu5v0x0') is not None else 'None',
            'link': item.find('a', class_='css-1bbgabe').get('href') if item.find('a',
                                                                                  class_='css-1bbgabe') is not None else 'None'
        })
        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["ad-price"]} -> Link: {comp["link"]}')
            file_save()

kz_pars()
