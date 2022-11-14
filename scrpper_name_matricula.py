# SCRAPPER REDUZIDO - RASPA MATRICULA E NOME (cria um arquivo txt com o output)

import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
# chrome_options.headless = True # also works'''

navegador = webdriver.Chrome(options=chrome_options)
navegador.get('http://www.rondonopolis.mt.gov.br/transparencia_rondonopolis/servlet/contrato_servidor_v3?1')

pesquisar = navegador.find_element(By.XPATH, '//*[@id="DIV_BTN_PESQUISAR"]/input')
pesquisar.click()
sleep(1)

opcao150 = navegador.find_element(By.XPATH, '//*[@id="vQTD_POR_PAGINA"]/option[7]')    
opcao150.click()
sleep(1)

proximo = navegador.find_element(By.XPATH, '//*[@id="TB_PROXIMO_ENABLED"]/a')

registros = 72289
pag = 482 #int(registros/150)  

lista = []                 
for i in range(pag):    
  tbody = navegador.find_element(By.XPATH, '//*[@id="grid"]/tbody')     
  html_servidores = tbody.get_attribute('innerHTML')    
                  
  soup = BeautifulSoup(html_servidores, 'html.parser')
  servidores = soup.find_all('tr')
  sleep(2)
  
  for tr in servidores:
    cont = 0
    for td in tr:
      cont = cont +1
      if cont == 1:         
        lista.append(td)
      if cont == 2:         
        lista.append(td)    
  
  if i != 481:
    print(i)
    proximo.click()          
  
  sleep(2)
  
  
sleep(5)  

lista_limpa = []  
for a in lista:
  c = str(a)   
  d = c.replace("<td>", '')       
  e = d.replace('</td>', '')
  lista_limpa.append(e)               
    

lista_servidores = []
for i in range(0, len(lista_limpa), 2):
  lista_servidores.append(lista_limpa[i : i+2]) 
    
original_stdout = sys.stdout # Save a reference to the original standard output

with open('nomes_servidores.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(lista_servidores)
    sys.stdout = original_stdout # Reset the standard output to its original value
    
navegador.quit()