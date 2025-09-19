# IMDb Top 250 TV Shows Scraper

Este é um script em Python que utiliza a biblioteca Selenium para realizar a coleta de dados (web scraping) da lista de "Top 250 TV Shows" do site [IMDb](https://www.imdb.com/). O script coleta informações detalhadas de cada série, incluindo título, ano de estreia, ano de encerramento, número de episódios, classificação indicativa, nota do imdb, popularidade e elenco, e exporta os dados consolidados para um arquivo JSON.

## Funcionalidades

- **Navegação Automatizada**: Acessa o site do IMDb, navega pelo menu e chega até a página do Top 250 Séries.
- **Coleta de Dados em Duas Fases**:
    1.  Extrai a lista inicial com os dados básicos de todas as 250 séries.
    2.  Visita a página individual de cada série para coletar informações adicionais como popularidade e elenco principal.
- **Processamento de Dados**: Estrutura as informações coletadas em um formato limpo e organizado.
- **Exportação para JSON**: Salva todos os dados em um único arquivo `top_250_series.json`, formatado para fácil leitura e utilização posterior.
- **Operação Headless**: O navegador é executado em modo "headless" (sem interface gráfica), permitindo que o script rode em segundo plano ou em servidores.
- **Feedback em Tempo Real**: Exibe o progresso da coleta no terminal.

## Estrutura do JSON de Saída

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