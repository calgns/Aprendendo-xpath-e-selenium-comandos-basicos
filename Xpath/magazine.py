from selenium import webdriver
#abre o navegador automaticamente não se preucupe com a mensagem dizendo que ele estasendo controlado ate
#porque é você quem esta o controlando.
navegador = webdriver.Chrome()
# coloque o site que ele vai abrir. Exemplo: https://www.youtube.com/
# ou https://ri.magazineluiza.com.br/ (que esta sendo usado,
# basicamente você vai pegar uma planilha, porem, forma automatizada)
# depois disso tudo escolher o site e baixar o driver, entre no site e copie seu endereço
# e o cole assim como foi feito
# o get vai entrar no site
navegador.get("https://ri.magazineluiza.com.br/")
# aperte as teclas ctrl + shift + c e
# utilizando o botão esquerdo do mouse você
# clica encima do ( "x" ) para obter o caminho para fechar o anuncio
# o meu deu
# (de ctrl+c) //*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img
#esse código ja no seu pode ser diferente principalmente se o site ja atualizou
# então faça o favor de clicar
#sempre com aspas simples de fora
# com aspas duplas pode dar error
#.find_element_by_xpath vai encontrar o xpath  e click no final va
navegador.find_element_by_xpath('//*[@id="banner"]/a[1]/img').click() #lembrete.voce deve fechar o ANUNCIO para
# continuar
