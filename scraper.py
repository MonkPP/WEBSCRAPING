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
from alunos import lista_alunos

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

#pag = 15  #teste de paginas

#FUNÇÃO PEGAR O CONTEUDO DA CEDULA
def limpar(td):
    c = str(td)
    if c == '<td></td>':
        c = ' - '
    d = c.replace('<td>', '')
    e = d.replace('</td>', '')  
    return e


#FUNÇÃO UNICODIZAR
def unicodizar(string):
    a = ['a', 'á', 'à', 'ã', 'A', 'Á', 'À', 'Ã']
    e = ['e', 'é', 'ê', 'è', 'ẽ', 'E', 'É', 'Ê', 'È', 'Ẽ']
    i = ['i', 'í', 'î', 'ì', 'ĩ', 'I', 'Í', 'Î', 'Ì', 'Ĩ']
    u = ['u', 'ú', 'û', 'ù', 'ũ', 'U', 'Ú', 'Û', 'Ù', 'Ũ']
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
                info = limpar(td)   
                
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
                    servidor.append(matricula)
                    
                    try:
                        nom = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_NOME"]') 
                        nome = str(nom.get_attribute('innerHTML'))
                        servidor.append(nome)
                    except:
                        servidor.append(info)
                        
                    try:
                        sit = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_SITUACAO"]') 
                    except:
                        sit = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_SITUACAO"]') 
                    situacao = str(sit.get_attribute('innerHTML'))
                    servidor.append(situacao)
                        
                    try:
                        sal = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_VALOR"]')
                    except:
                        sal = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_VALOR"]') 
                    salario = str(sal.get_attribute('innerHTML'))
                    servidor.append(salario)
                        
                    try:
                        car = navegador.find_element(By.XPATH, '//*[@id="span_vSERV_CARGO"]') 
                    except:
                        car = navegador.find_element(By.XPATH, '//*[@id="span_vCONTRATO_PESSOAL_OBJETO"]') 
                    cargo = str(car.get_attribute('innerHTML'))
                    servidor.append(cargo)
                        
                    lot = navegador.find_element(By.XPATH, '//*[@id="span_vSERVIDOR_LOTACAO_DESC"]') 
                    lotacao = str(lot.get_attribute('innerHTML'))
                    servidor.append(lotacao)
                    
                    #ADD A LISTA A UMA LISTA MAIOR E LIMPANDO A PRIMEIRA
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


# Open a new CSV file for writing
with open(nome_arquivo, mode='w', newline='', encoding="utf-8") as file:
    # Create a CSV writer object
    writer = csv.writer(file, delimiter=',')
    
    # Write the header row
    writer.writerow(['Matricula', 'Nome', 'Situação', 'Salario', 'Cargo', 'Lotação'])
    
    # Write the data rows
    for row in alunos_servidores:
        writer.writerow(row)



'''original_stdout = sys.stdout 
with open(nome_arquivo, 'w', encoding="utf-8") as f:  
    sys.stdout = f # Change the standard output to the file we created.
    print('alunos_python = ', alunos_servidores)
    sys.stdout = original_stdout # Reset the standard output to its original value'''
    