import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.residentevildatabase.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,es;q=0.6',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}


def get_content(url):
    response = requests.get(url, headers=headers)
    return response

def get_basic_infos(soup):
    
    div_page = soup.find("div", class_ ="td-page-content")
    paragrafo = div_page.find_all("p")[1]
    ems = paragrafo.find_all("em")

    data = {}

    for i in ems:
        chave, valor, *_ = i.text.split(":")
        data[chave.strip(" ")] = valor.strip(" ")

    return data

def get_aparicoes(soup):
    lista = (
        soup.find("div", class_="td-page-content") 
            .find("h4")
            .find_next() 
            .find_all("li")
            )

    aparicoes = [i.text for i in lista]
    return aparicoes

def get_personagem_infos(url):
    
    response = get_content(url)
    
    if response.status_code != 200:
        print("Não foi possível obter os dados")
        return {}
    else:
        soup = BeautifulSoup(response.text)
        data = get_basic_infos(soup)
        data['aparicoes'] = get_aparicoes(soup)
        return data
    
def get_links():
    url = "https://www.residentevildatabase.com/personagens/"
    response = requests.get(url=url, headers=headers)
    soup_personagens = BeautifulSoup(response.text)
    ancoras = (soup_personagens.find("div", class_="td-page-content")
                               .find_all("a"))
    links = []
    for i in ancoras:
        links.append(i.get("href"))
    return links