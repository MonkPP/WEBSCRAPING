#Material de referencia: 
#https://www.youtube.com/watch?v=CdoBcv1QmSg&t=1048s&ab_channel=WalissonSilva
#https://www.youtube.com/watch?v=_Ri-QjToQ24&t=425s&ab_channel=Codifike
#https://selenium-python.readthedocs.io/
#https://www.youtube.com/watch?v=kqvWOcPog4s&ab_channel=Programa%C3%A7%C3%A3oDin%C3%A2mica'''

#Tem que baixar o chromedriver em https://chromedriver.chromium.org/downloads 
# e colocar na mesma pasta do arquivo python


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#escolher e abrir o navegador
navegador = webdriver.Chrome()
navegador.get('http://www.rondonopolis.mt.gov.br/transparencia_rondonopolis/servlet/contrato_servidor_v3?1') # url do site 


#atribuir a variavel 'pesquisar' ao elemento html do botão 'pesquisar'
pesquisar = navegador.find_element(By.XPATH, '//*[@id="DIV_BTN_PESQUISAR"]/input') #copiar o Xpath do botão de pesquisar no html
#clicar em pesquisar  
pesquisar.click()
sleep(1) # pra dar tempo da pag carregar, ns se é necessário mesmo


# selecionar a vizualização de 150 registros, copiar o Xpath da opção 150 no html
opcao150 = navegador.find_element(By.XPATH, '//*[@id="vQTD_POR_PAGINA"]/option[7]')    
# clicar em 150                     
opcao150.click()
sleep(2) # pra dar tempo da pag carregar, ns se é necessário mesmo


#atribuindo a variavel 'próximo' ao botão de próximo 
proximo = navegador.find_element(By.XPATH, '//*[@id="TB_PROXIMO_ENABLED"]/a') # caminho copiado do html


#pegando o conteudo do elemento 'tbody' e atribuindo a variavel 'html_servidores'
tbody = navegador.find_element(By.XPATH, '//*[@id="grid"]/tbody') # caminho do tbody copiado do html
html_servidores = tbody.get_attribute('innerHTML') #pegando o conteudo


#informando a quantidade de registros e dividindo por 150 pra saber quantas pag tem
registros = 72289
#rodando dó 5 paginas de teste, o '-1' p ele não duplicar a ultima página
pag = 5-1 #(registros/150)-1


# não sei explicar essa parte, acho que ele passa pra html pra poder encontrar as 'tags'
soup = BeautifulSoup(html_servidores, 'html.parser') # passando p html
servidores = soup.find_all('tr') #encontando todos os 'tr' da pagina e atribuindo a 'servidores'
sleep(3)



#apagando os elementos "td" que contem informação javascript e colocando informações uteis em uma lista
# 
lista = []                  #lista vazia p colocar as inform
for i in range(pag):        #repetir pelo numero de paginas
  for tr in servidores:     #passando por todos os 'tr'
    cont = 0    
    for td in tr:           #passando por cada 'td'
      cont = cont + 1       #adicionando 1 ao contador
      if cont == 7:         #se for o setimo elemento não vai adicionar na lista
        continue
      if cont == 8:         #se for o oitavo elemento não vai adicionar na lista e vai resetar o contador
        cont = 0
        continue
      lista.append(td)      #add os 'td' a lista
      
  proximo.click()           #clicar em proximo
  sleep(2)
  
  tbody = navegador.find_element(By.XPATH, '//*[@id="grid"]/tbody')     #repetir os processos de copiar o conteudo do tbody 
  html_servidores = tbody.get_attribute('innerHTML')                    #e passar pra variavel 'soup'
  
  soup = BeautifulSoup(html_servidores, 'html.parser')
  servidores = soup.find_all('tr')
  sleep(3)
    
    
#separando cada 5 elemento e colocando em uma sublista, tods as sublistas estão na lista 'New'   
new = []
for i in range(0, len(lista), 5):
    new.append(lista[i : i+5])
    
    
# limpando a lista
nova = []  
for a in new:
  for b in a:
    c = str(b)              #convertendo os elementos da lista em Strings (são bs4.element.tag por enquanto)
    if c == '<td></td>':    # se não tiver nada entre as tags, reatribuir ' - ' ao elemento
      c = ' - '
    d = c.replace("<td>", '')       #tirar os  '<td></td>'
    e = d.replace('</td>', '')
    nova.append(e)                  # add a uma lista nova
    
    
    
#separando cada 5 elemento e colocando em uma sublista, tods as sublistas estão na lista 'lista_servidores'
lista_servidores = []
for i in range(0, len(nova), 6):
    lista_servidores.append(nova[i : i+5])
    
    
#imprimindo a lista dos servidores, que agora é uma lista de varias listas de Strings
print(lista_servidores)

navegador.close()
