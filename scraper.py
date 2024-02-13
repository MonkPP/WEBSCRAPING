#*************RASPAGEM DE SERVIDORES QUE FORAM ALUNOS DO IFMT***************
#cria um arquivo csv com os servidores que estiverem na lista de alunos do ifmt

#*************VERSÃO DO CHROMEDRIVER DEVE SER A MESMA DO COMPUTADOR***************
#CIDADE E LINK
cidade = 'Rondonopolis'
link_portal = 'http://www.rondonopolis.mt.gov.br/transparencia_rondonopolis/servlet/contrato_servidor_v3?1'

#IMPORTS
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
from time import sleep
from alunos_unicode import lista_alunos

# HEADLESS
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument('--disable-features=DefaultPassthroughCommandDecoder')

#ABRINDO O SITE
navegador = webdriver.Chrome(options=chrome_options)
navegador.get(link_portal)
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
registros = navegador.find_element(By.XPATH, '//*[@id="span_vTOTAL_REGISTROS"]')
reg = int(registros.get_attribute('innerHTML'))

if reg % 150 == 0:
    pag = reg//150
else:
    pag = reg//150 + 1

#FUNÇÃO PEGAR O CONTEUDO DA CEDULA
def limpar(td):
    c = str(td)
    if c == '<td></td>':
        c = ' - '
    d = c.replace('<td>', '')
    e = d.replace('</td>', '')  
    return e
         
def unicodizar(string):
    a = ['a', 'á', 'à', 'ã', 'A', 'Á', 'À', 'Ã']
    e = ['e', 'é', 'ê', 'è', 'ẽ', 'E', 'É', 'Ê', 'È', 'Ẽ']
    i = ['i', 'í', 'î', 'ì', 'ĩ', 'I', 'Í', 'Î', 'Ì', 'Ĩ']
    u = ['u', 'ú', 'û', 'ù', 'ũ', 'U', 'Ú', 'Û', 'Ù', 'Ũ']
    o = ['o','ó', 'ò', 'ô', 'õ', 'O', 'Ó', 'Ò', 'Ô', 'Õ']
    c = ['c', 'ç', 'C', 'Ç']
    n = ['n', 'ñ', 'N', 'Ñ']
    
    nova_string = ""
    for letra in string:
        if letra in a:
            nova_string += 'A'
        elif letra in e:
            nova_string += 'E'
        elif letra in i:
            nova_string += 'I'
        elif letra in u:
            nova_string += 'U'
        elif letra in o:
            nova_string += 'O'    
        elif letra in c:
            nova_string += 'C'
        elif letra in n:
            nova_string += 'N'
        else:
            nova_string += letra
    return nova_string
      
      
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
            if cont == 1:
                matri = limpar(td)  
                
            if cont == 2: 
                infor = limpar(td)   
                info = unicodizar(infor)
                
                # COMPARANDO AS LISTAS E RASPANDO OS DADOS
                if info in lista_alunos:
                    
                    print(info)
                    
                    #CLICK LUPA
                    url = '//*[@id="grid"]/tbody/tr[' + chave + ']/td[8]/a'
                    lupa = navegador.find_element(By.XPATH, url)
                    navegador.execute_script("arguments[0].click();", lupa)
                    
                    #MUDAR PRA JANELA ABERTA
                    window_before = navegador.window_handles[0]
                    window_after = navegador.window_handles[-1] 
                    navegador.switch_to.window(window_after)
                    
                    #PEGANDO DADOS
                    try:
                        mat = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_MATRICULA_CONTRATO"]') 
                        matricula = str(mat.get_attribute('innerHTML'))
                    except:
                        matricula = matri
                                            
                    try:
                        sit = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_SITUACAO"]') 
                    except:
                        sit = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_SITUACAO"]') 
                    situacao = str(sit.get_attribute('innerHTML'))
                    
                    try:
                        sal = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_VALOR"]')
                    except:
                        sal = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_VALOR"]') 
                    salario = str(sal.get_attribute('innerHTML'))
                    
                    try:
                        car = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_CARGO"]') 
                    except:
                        car = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_PESSOAL_OBJETO"]') 
                    cargo = str(car.get_attribute('innerHTML'))
                    
                    lot = navegador.find_element(By.XPATH, '//*[@id="span_vSERVIDOR_LOTACAO_DESC"]') 
                    lotacao = str(lot.get_attribute('innerHTML'))
                    
                    
                    #ADD A LISTA A UMA LISTA MAIOR E LIMPANDO A PRIMEIRA
                    servidor = [matricula, info, situacao, salario, cargo, lotacao]
                    alunos_servidores.append(servidor)
                    servidor = []
                    
                    
                    #VOLTANDO PARA A JANELA PRINCIPAL
                    navegador.switch_to.window(window_before)
                                    
    #PROXIMA PAGINA            
    if p != pag-1:
        sleep(1)
        proximo.click() 
        sleep(2)
sleep(2)


navegador.quit()


#CRIAR UM ARQUIVO COM OS DADOS RASPADOS
nome_arquivo = cidade + '_raspagem.csv' #pode mudar o tipo de arquivo aqui

with open(nome_arquivo, mode='w', newline='', encoding="utf-8") as file:

    writer = csv.writer(file, delimiter=',')
    writer.writerow(['matricula', 'nome', 'situacao', 'salario', 'cargo', 'lotacao'])
    
    for row in alunos_servidores:
        writer.writerow(row)