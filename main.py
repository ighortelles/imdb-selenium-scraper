from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = 'https://www.imdb.com/'

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(link)

menu = driver.find_element(By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]')
menu.click()

top_250_series = menu.find_element(By.XPATH, '/html/body/div[2]/nav/div/aside[1]/div/div[2]/div/div[2]/div[1]/span/div/div/ul/a[2]/span')
top_250_series.click()

tabela_series = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul')

series = []

lista_series = tabela_series.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
tam = len(lista_series)
i = 1
for serie in lista_series:
    print(f"{i}/{tam}")
    
    metadados = []
    for meta in serie.find_elements(By.CLASS_NAME, 'cli-title-metadata-item'):
        metadados.append(meta.text)
        data = metadados[0].split('–')

    dicionario_series = {
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

    series.append(dicionario_series)
    i += 1

for s in series[:5]:
    print(f"Coletando dados da série: {s['Título']}")
    link = s['Link']
    
    driver.get(link)

    rating_bar_pop = driver.find_element(By.CSS_SELECTOR, '[data-testid="hero-rating-bar__popularity__score"]')
    s['Popularidade'] = rating_bar_pop.text

    cast = driver.find_element(By.CSS_SELECTOR, '[data-testid="title-cast"]')
    cast_actors = cast.find_elements(By.CSS_SELECTOR, '[data-testid="title-cast-item"]')

    for actor in cast_actors:
        metadados = actor.text.split('\n')
        dict_ator = {
            'Nome Ator': metadados[0],
            'Personagem/Papel': metadados[1],
            'Quantidade de Episódios': metadados[2].split()[0]
        }
        
        s['Atores'].append(dict_ator)
