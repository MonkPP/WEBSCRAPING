# SCRAPPER REDUZIDO - RASPA MATRICULA E NOME 

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

#CALCULANDO A PAG
'''
registros = navegador.find_element(By.XPATH, '//*[@id="span_vTOTAL_REGISTROS"]')
reg = int(registros.get_attribute('innerHTML'))

if reg % 150 == 0:
    pag = reg//150
else:
    pag = reg//150 + 1
'''

pag = 1

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
      c = str(td)   
      d = c.replace("<td>", '')       
      e = d.replace('</td>', '')
      cont = cont +1
      if cont == 1:         
        lista.append(e)
      if cont == 2:         
        lista.append(e)    
  
  if i != pag-1:
    print(i)
    proximo.click()          
  
  sleep(2)
sleep(3)  

lista_servidores = []
for i in range(0, len(lista), 2):
  lista_servidores.append(lista[i : i+2]) 
  
  
print(lista_servidores)
  
# CRIA UM ARQUIVO PY COM O OUTPUT
'''
original_stdout = sys.stdout # Save a reference to the original standard output
#encoding='utf8'
with open('nomes_servidores.py', 'w') as f:  #pode mudar o tipo de arquivo aqui, vou colocar python pq já tenho o txt 
    sys.stdout = f # Change the standard output to the file we created.
    print(lista_servidores)
    sys.stdout = original_stdout # Reset the standard output to its original value
'''  
navegador.quit()