# SCRAPPER DADOS TABELA + DADOS LUPA COMPARANDO COM LISTA DE ALUNOS

#IMPORTS
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import re


# HEADLESS
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument('--disable-features=DefaultPassthroughCommandDecoder')


#ABRINDO O SITE
navegador = webdriver.Chrome(options=chrome_options)
navegador.get('http://www.rondonopolis.mt.gov.br/transparencia_rondonopolis/servlet/contrato_servidor_v3?1')
navegador.window_handles


#CLICANDO EM PESQUISAR E OPÇÃO 150
pesquisar = navegador.find_element(By.XPATH, '//*[@id="DIV_BTN_PESQUISAR"]/input')
pesquisar.click()
sleep(1)

opcao150 = navegador.find_element(By.XPATH, '//*[@id="vQTD_POR_PAGINA"]/option[7]')    
opcao150.click()
sleep(2)


#ACHANDO O BOTÃO PROXIMO
proximo = navegador.find_element(By.XPATH, '//*[@id="TB_PROXIMO_ENABLED"]/a')


#LISTA DOS ALUNOS PARA COMPARAÇÃO E LISTA VAZIA PRA COLOCAR OS DADOS DOS ALUNO-SERVIDORES
alunos = ['ABADIA COSTA REIS', 'paola', 'ABADIAS ELZA RIBEIRO PAULINO','raysa', 'ADEMILSON RIBEIRO DA SILVA', 'ZULMIRA SILVA', 'ZULEME MARIA FREITAS PEREIRA', 'amanda']
alunos_servidores = []
dados_tabela = []

#CALCULANDO A PAG
#'''
registros = navegador.find_element(By.XPATH, '//*[@id="span_vTOTAL_REGISTROS"]')
reg = int(registros.get_attribute('innerHTML'))

if reg % 150 == 0:
    pag = reg//150
else:
    pag = reg//150 + 1
#'''
#pag = 2  #teste de paginas


#RASPAGEM DE DADOS           
for p in range(pag):
        
    tbody = navegador.find_element(By.XPATH, '//*[@id="grid"]/tbody')     
    html_servidores = tbody.get_attribute('innerHTML')                    
    
    soup = BeautifulSoup(html_servidores, 'html.parser')
    servidores = soup.find_all('tr')
    sleep(2)
    
    for tr in servidores:
        cont = 0    
        chave = str(servidores.index(tr)+1)
        
        for td in tr:      
            cont = cont+1
            
            if cont == 1 or cont == 2 or cont == 5:
                c = str(td)
                
                #LIMPANDO OS DADOS                
                if c == '<td></td>':
                    c = ' - '
                d = c.replace('<td>', '')
                info = d.replace('</td>', '')    
                #dados_tabela.append(info)
                
                # COMPARANDO AS LISTAS E RASPANDO OS DADOS
                if info in alunos:
                    
                    #CLICK LUPA
                    url = '//*[@id="grid"]/tbody/tr[' + chave + ']/td[8]/a'
                    lupa = navegador.find_element(By.XPATH, url)
                    navegador.execute_script("arguments[0].click();", lupa)
                    
                    #MUDAR PRA JANELA ABERTA
                    window_before = navegador.window_handles[0]
                    window_after = navegador.window_handles[-1] 
                    navegador.switch_to.window(window_after)
                
                    #PEGANDO DADO - MATRICULA
                    mat = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_MATRICULA_CONTRATO"]') 
                    matricula = str(mat.get_attribute('innerHTML'))
                    alunos_servidores.append(matricula)
                    
                    #PEGANDO DADO - NOME
                    nom = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_NOME"]') 
                    nome = str(nom.get_attribute('innerHTML'))
                    alunos_servidores.append(nome)
                    
                    #PEGANDO DADO - SITUAÇÃO
                    sit = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_SITUACAO"]') 
                    situacao = str(sit.get_attribute('innerHTML'))
                    alunos_servidores.append(situacao)
                    
                    #PEGANDO DADO - SALARIO
                    sal = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_VALOR"]') 
                    salario = str(sal.get_attribute('innerHTML'))
                    alunos_servidores.append(salario)
                    
                    #PEGANDO DADO - CARGO
                    car = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_CARGO"]') 
                    cargo = str(car.get_attribute('innerHTML'))
                    alunos_servidores.append(cargo)
                    
                    #PEGANDO DADO - LOTAÇÃO
                    lot = navegador.find_element(By.XPATH, '//*[@id="span_vSERVIDOR_LOTACAO_DESC"]') 
                    lotacao = str(lot.get_attribute('innerHTML'))
                    alunos_servidores.append(lotacao)
                    
                    #MUDANDO PARA A JANELA PRINCIPAL
                    navegador.switch_to.window(window_before)
                                    
    #PROXIMA PAGINA            
    if p != pag-1:
        sleep(1)
        print('pag:' , p)
        proximo.click() 
        sleep(2)
sleep(2)

navegador.quit()

#print(dados_tabela)

#IMPRIMINDO OS DADOS DOS ALUNO-SERVIDORES 
print(alunos_servidores)