# IMDb Top 250 TV Shows Scraper

Este projeto foi desenvolvido para a atividade "Coleta de Dados com Selenium" da disciplina de **Coleta, Preparação e Análise de Dados**, do curso de **Ciência de Dados e Inteligência Artificial** da PUCRS.

O projeto consiste em um script Python que utiliza a biblioteca Selenium para realizar a coleta de dados (web scraping) da lista "Top 250 TV shows" do site [IMDb](https://www.imdb.com/).

O objetivo é navegar pela página, extrair informações detalhadas de cada uma das 250 séries e, ao final, consolidar todos os dados em um único arquivo JSON.

## Funcionamento

O script funciona da seguinte forma:

1. Inicializa uma instância do navegador Firefox em modo headless (sem interface gráfica), controlado pelo Selenium.
2. Acessa o lsite [IMDb](https://www.imdb.com/), navega até a página [Top 250 TV shows](https://www.imdb.com/chart/toptv/?ref_=hm_nv_menu) e extrai a lista com os 250 programas de TV mais bem avaliados.
3. Para cada item da lista, processa os metadados básicos (título, ano de estreia e encerramento, número de episódios, classificação indicativa, nota do IMDb e o link para a página de detalhes).
4. Acessa o link de cada série individualmente para buscar informações adicionais que não estão na lista principal: o ranking de popularidade e o elenco principal.
5. Consolida todos os dados em uma lista de dicionários e a exporta para um arquivo JSON

O arquivo `top_250_series.json` será gerado no mesmo diretório do script. Cada objeto na lista JSON terá a seguinte estrutura:

```json
[
    {
        "Título": "Breaking Bad",
        "Ano de estreia": "2008",
        "Ano de encerramento": "2013",
        "Número Total de Episódios": "62",
        "Classificação indicativa": "TV-MA",
        "Nota do IMDB": "9.5",
        "Link": "[https://www.imdb.com/title/tt0903747/](https://www.imdb.com/title/tt0903747/)",
        "Popularidade": "123",
        "Atores": [
            {
                "Nome Ator": "Bryan Cranston",
                "Personagem/Papel": "Walter White",
                "Quantidade de Episódios": "62"
            },
            {
                "Nome Ator": "Aaron Paul",
                "Personagem/Papel": "Jesse Pinkman",
                "Quantidade de Episódios": "62"
            }
        ]
    }
]