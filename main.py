import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def iniciar_driver() -> webdriver.Firefox:
    options = Options()
    options.add_argument('--headless')
    return webdriver.Firefox(options=options)

def coletar_html_250_series(url: str, driver: webdriver.Firefox):
    driver.get(url)
    time.sleep(1.5)

    menu_btn = driver.find_element(By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]')
    menu_btn.click()
    print('OK | Menu acessado.')

    time.sleep(1.5)
    top250_series = menu_btn.find_element(By.XPATH, '/html/body/div[2]/nav/div/aside[1]/div/div[2]/div/div[2]/div[1]/span/div/div/ul/a[2]/span')
    top250_series.click()
    print('OK | Top 250 TV Shows acessado.')
    
    time.sleep(1.5)
    lista_series = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul') 

    return lista_series 

def processar_dados(lista_elementos) -> list:
    series = []

    lista_series = lista_elementos.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
    total = len(lista_series)
    print('>> Iniciando coleta das séries.')

    for idx, serie in enumerate(lista_series, start=1):
        print(f"{idx}/{total}")
        
        metadados = []
        for meta in serie.find_elements(By.CLASS_NAME, 'cli-title-metadata-item'):
            metadados.append(meta.text)
            data = metadados[0].split('–')

        series_dict = {
            'Título': " ".join(serie.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper').text.split()[1:]),
            'Ano de estreia': data[0],
            'Ano de encerramento': data[1] if len(data) > 1 else None,
            'Número Total de Episódios': metadados[1].split()[0],
            'Classificação indicativa': metadados[2] if len(metadados) > 2 else None,
            'Nota do IMDB': serie.find_element(By.CLASS_NAME, 'ipc-rating-star--rating').text,
            'Link': serie.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper').get_attribute("href"),
            'Popularidade': None,
            'Atores': []
        }

        series.append(series_dict)

    return series

def coletar_atores(driver: webdriver.Firefox, dados_series: list) -> list:
    for serie in dados_series:
        print(f">> Coletando dados da série: {serie['Título']}")
        driver.get(serie['Link'])
        time.sleep(1.5)

        popularidade = driver.find_element(By.CSS_SELECTOR, '[data-testid="hero-rating-bar__popularity__score"]')
        serie['Popularidade'] = popularidade.text

        elenco = driver.find_element(By.CSS_SELECTOR, '[data-testid="title-cast"]')
        atores = elenco.find_elements(By.CSS_SELECTOR, '[data-testid="title-cast-item"]')

        for ator in atores:
            metadados = ator.text.split('\n')
            ator_dict = {
                'Nome Ator': metadados[0],
                'Personagem/Papel': metadados[1] if len(metadados) > 1 else None,
                'Quantidade de Episódios': metadados[2].split()[0] if len(metadados) > 2 else None
            }
            
            serie['Atores'].append(ator_dict)

    return dados_series

def exportar_para_json(dados_series: list) -> json:
    with open('top_250_series.json', "w", encoding='utf8') as file:
        json.dump(dados_series, file, indent=4, ensure_ascii=False)

    print("OK | Arquivo JSON exportado com sucesso.")

if __name__ == '__main__':
    driver = iniciar_driver()
    try: 
        lista_series = coletar_html_250_series(url='https://www.imdb.com/', driver=driver)
        dados = processar_dados(lista_elementos=lista_series)
        dados_consolidados = coletar_atores(driver=driver, dados_series=dados)
        exportar_para_json(dados_series=dados_consolidados)
    finally:
        driver.quit()