from bs4 import BeautifulSoup
import requests

def file_save():
    with open('rc_pars.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price: {comp["ad-price"]} -> Link: {comp["link"]}\n')
def rc_pars():
    url = 'type_name_of_categori'
    headers = {
        'User-Agent':'your_user-agent',
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

def main():
    rc_pars()

if __name__ == "__main__":
    main()
