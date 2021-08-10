# necessário baixar o webdriver atual
# link = https://chromedriver.chromium.org/downloads
# para você ver o Xpath voce pode usar a tecla f12 e depois ctrl + shift + c
# ou ctrl + shift + i, porém, a melhor opção é ctrl + shift + c pois
# ja coloca  as informações no mouse facilitando na hora de procurar o xpath
from selenium import webdriver
#abre o navegador
navegador = webdriver.Chrome()
# coloque o site que ele vai abrir. Exemplo: https://www.youtube.com/
# ou https://ri.magazineluiza.com.br/ (que esta send usado)
# depois disso tudo escolher o site e baixar o driver, entre no site e copie seu endereço
# e o cole assim como foi feito
# isso vai abrir o site
navegador.get("https://ri.magazineluiza.com.br/")
