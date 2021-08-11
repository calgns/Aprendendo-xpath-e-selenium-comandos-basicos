from selenium import webdriver
#abre o navegador automaticamente não se preocupe com a mensagem dizendo que ele esta sendo controlado.
# ate porque é você quem esta o controlando.
navegador = webdriver.Chrome()
# coloque o site que ele vai abrir. Exemplo: https://ri.magazineluiza.com.br/
# ou  https://www.youtube.com/ (que esta sendo usado, de forma automatizada)
# depois disso tudo escolher o site e baixar o driver, entre no site e copie seu endereço
# e o cole assim como foi feito
# o get vai entrar no site
navegador.get("https://www.youtube.com/")
# aperte as teclas ctrl + shift + c e utilizando o botão esquerdo do mouse você clica encima da biblioteca
# quando você clicar o código do lado direito vai ficar azul entoa com o lado direito do mouse você
#clica nesse azul e vai em copy depois em copy Xpath o penúltimo e pronto
#o meu deu. (de ctrl+c) //*[@id="icon"]
#sempre com aspas simples de fora com aspas duplas pode dar error
#.find_element_by_xpath vai encontrar o xpath  e click no final vai clicar
navegador.find_element_by_xpath('//*[@id="icon"]').click()
# e pronto objetivo concluído
#eu prefiro o pyautogui mas o selenium é bom, mais rapido e mais preciso.
#o pyautogui é mais facil de se pegar ja o selenium é uma leitura mais complicada
# se possível assista a um video vai ser mais facile

