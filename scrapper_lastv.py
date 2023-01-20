#encoding: utf-8
#ADRIANA GOMES DOS SANTOS
# SCRAPPER DADOS TABELA + DADOS LUPA COMPARANDO COM LISTA DE ALUNOS

#IMPORTS
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from nomes_comparacao import alunos

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


#ATRIBUINDO O BOTÃO PROXIMO
proximo = navegador.find_element(By.XPATH, '//*[@id="TB_PROXIMO_ENABLED"]/a')


#LISTAS 
servidor = []
alunos_servidores = []


#CALCULANDO A PAG
'''registros = navegador.find_element(By.XPATH, '//*[@id="span_vTOTAL_REGISTROS"]')
reg = int(registros.get_attribute('innerHTML'))

if reg % 150 == 0:
    pag = reg//150
else:
    pag = reg//150 + 1'''

pag = 10  #teste de paginas


#RASPAGEM DE DADOS           
for p in range(pag):
    print('pag:' , p+1)    
    
    tbody = navegador.find_element(By.XPATH, '//*[@id="grid"]/tbody')     
    html = tbody.get_attribute('innerHTML')                    
    
    soup = BeautifulSoup(html, 'html.parser')
    tabela = soup.find_all('tr')
    sleep(2)
    
    #ITERANDO PELAS LINHAS
    for tr in tabela:
        cont = 0    
        chave = str(tabela.index(tr)+1)
        
        #ITERANDO PELAS CEDULAS DE CADA LINHA
        for td in tr:      
            cont = cont+1
            
            if cont == 2: # or cont == 1 or cont == 5:
                c = str(td)
                
                #LIMPANDO OS DADOS                
                if c == '<td></td>':
                    c = ' - '
                d = c.replace('<td>', '')
                info = d.replace('</td>', '')   
                
                # COMPARANDO AS LISTAS E RASPANDO OS DADOS
                if info in alunos:
                    
                    print(info)
                    
                    #CLICK LUPA
                    url = '//*[@id="grid"]/tbody/tr[' + chave + ']/td[8]/a'
                    lupa = navegador.find_element(By.XPATH, url)
                    navegador.execute_script("arguments[0].click();", lupa)
                    
                    #MUDAR PRA JANELA ABERTA
                    window_before = navegador.window_handles[0]
                    window_after = navegador.window_handles[-1] 
                    navegador.switch_to.window(window_after)
                    
                
                    #PEGANDO DADO - MATRICULA
                    try:
                        mat = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_MATRICULA_CONTRATO"]') 
                        matricula = str(mat.get_attribute('innerHTML'))
                        servidor.append(matricula)
                    except:
                        servidor.append("não tem mat")
                    
                    #PEGANDO DADO - NOME
                    try:
                        nom = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_NOME"]') 
                        nome = str(nom.get_attribute('innerHTML'))
                        servidor.append(nome)
                    except:
                        servidor.append(info)
                        
                    #PEGANDO DADO - SITUAÇÃO
                    try:
                        sit = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_SITUACAO"]') 
                        situacao = str(sit.get_attribute('innerHTML'))
                        servidor.append(situacao)
                    except:
                        sit = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_SITUACAO"]') 
                        situacao = str(sit.get_attribute('innerHTML'))
                        servidor.append(situacao)
                        
                    #PEGANDO DADO - SALARIO
                    try:
                        sal = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_VALOR"]') 
                        salario = str(sal.get_attribute('innerHTML'))
                        servidor.append(salario)
                    except:
                        sal = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_VALOR"]') 
                        salario = str(sal.get_attribute('innerHTML'))
                        servidor.append(salario)
                        
                    #PEGANDO DADO - CARGO
                    try:
                        car = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_CARGO"]') 
                        cargo = str(car.get_attribute('innerHTML'))
                        servidor.append(cargo)
                    except:
                        car = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_PESSOAL_OBJETO"]') 
                        cargo = str(car.get_attribute('innerHTML'))
                        servidor.append(cargo)
                        
                    #PEGANDO DADO - LOTAÇÃO
                    lot = navegador.find_element(By.XPATH, '//*[@id="span_vSERVIDOR_LOTACAO_DESC"]') 
                    lotacao = str(lot.get_attribute('innerHTML'))
                    servidor.append(lotacao)
                    
                    #ADD A LISTA A UMA LISTA MAIOR E LIMPANDO A PRIMEIRA
                    alunos_servidores.append(servidor)
                    servidor = []
                    
                    #MUDANDO PARA A JANELA PRINCIPAL
                    navegador.switch_to.window(window_before)
                                    
    #PROXIMA PAGINA            
    if p != pag-1:
        sleep(1)
        proximo.click() 
        sleep(2)
sleep(2)

navegador.quit()

#IMPRIMINDO OS DADOS DOS ALUNO-SERVIDORES 
for li in alunos_servidores:
    print(li)