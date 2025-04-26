# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação 

import requests
from bs4 import BeautifulSoup

url = "http://localhost:3333/"
response = requests.get(url)
texto_html = response.text
parsed_html = BeautifulSoup(texto_html, "html.parser") # converto o html que estava cru, em objeto pro meu python

print(parsed_html.title.text)

# ir na pagina, selecionar algo que queira mostrar aqui (um titulo por exemplo)
# clicar com o botão direito e inspecionar elemento, nisso ir no codigo dele do html
# ir nas opções de copiar, e copiar selector, nisso você faz a semantica igual abaixo
# para pegar exatamente aquele objeto que você deseja no site

# lembrando que parsed_html.select_one ( eu estou selecionando um, do meu codigo CONVERTIDO para python)
# com o beautifulsoup
top_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")
print(top_jobs_heading)
print(top_jobs_heading.text) # a função text, me mostra oq esta dentro do html

# agora vamos pegar todo o texto do que está acompanhado com esse h2

article = top_jobs_heading.parent

print(article.text)


# RESUMÃO DE WEB SCRAPPING:
# basicamente você escolhe um site, pega seu URL, com o metodo request você pega o HTML desse site
# depois convertemos o HTML do site com beautifulsoup para que ele fique no metodo de python
# e assim a gente pode selecionar coisas especificas dentro do site, que eu queira mostrar aqui no codigo
# textos, noticias, sei la qualquer coisa OBS: pode ser usado para o mal tambem kkkkkkk
