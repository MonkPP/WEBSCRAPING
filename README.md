<h1 id="portugues" align="center">RASPAGEM DE DADOS</h1>

<h3 align="center">-<a href="#english"> ENGLISH VERSION </a>-</h3>


<details>
  <summary>Indice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#ferramentas-utilizadas">Ferramentas Utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#funcionamento-do-codigo">Funcionamento do Código</a>
    </li>
    <li><a href="#como-utilizar">Como Utilizar</a></li>
    <li><a href="#observações">Observações</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>


## Sobre o Projeto

Este projeto foi desenvolvido como parte de um programa de Iniciação Científica no Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso (IFMT), intitulado "Em busca de egressos do IFMT atuantes como servidores públicos do Município de Rondonópolis/MT". O objetivo do projeto é automatizar a consulta de informações sobre servidores públicos no Portal da Transparência da Prefeitura de Rondonópolis/MT, utilizando técnicas de raspagem de dados. Os dados obtidos são comparados com os dados dos alunos do IFMT para fazer uma relação aluno-servidor e finalmente ter um arquivo que nos mostre todos os aluno do IFMT que são/foram servidores públicos em Rondonópolis. 

Resultado do projeto:<a href="https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/servidores_alunos_rondonopolis.csv"> <strong> servidores_alunos_rondonopolis »</strong></a>


### Ferramentas Utilizadas

- **Python**: A linguagem de programação principal utilizada para desenvolver este projeto.
- **Selenium**: Uma ferramenta de automação de navegador web que permite simular interações do usuário, como clicar em botões e preencher formulários. É especialmente útil quando o site alvo utiliza JavaScript extensivamente ou requer interações específicas com a página da web.
- **BeautifulSoup**: Uma biblioteca Python para análise de documentos HTML e XML. Foi utilizada para extrair e manipular dados dos elementos HTML da página web.
- **Pandas**: Uma biblioteca Python para manipulação e análise de dados. Foi utilizada para processar e manipular dados estruturados, como a junção de dataframes. Neste projeto foi usada especificamente para pegar os dados dos alunos do IFMT, que estavam separados por ano em arquivos CSV, e para juntar os dataframes com relação aluno-servidor.


## Funcionamento do Código

O código-fonte principal deste projeto é o [scraper.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/scraper.py), que implementa um script em Python responsável pela raspagem de dados do Portal da Transparência da Prefeitura de Rondonópolis/MT. Este script utiliza Selenium para automatizar a interação com o site, navegando pelas páginas e clicando nos botões de pesquisa. Em seguida, os dados são extraídos usando BeautifulSoup e organizados em um arquivo CSV.

O resultado da raspagem de dados com selenium é este: [Rondonopolis_raspagem.csv](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/Rondonopolis_raspagem.csv)

### Outros Arquivos Python no Repositório

- [alunos_df.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/alunos_df.py): Este arquivo Python junta os dados de todos os alunos em um único arquivo CSV com a ajuda da biblioteca Pandas. Ao executar o código obtemos este arquivo: [alunos_ifmt.csv](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/alunos_ifmt.csv)
- [alunos_unicode.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/alunos_unicode.py): Cria uma lista de nomes de alunos, que será importada pelo scraper para fazer a comparação.
- [juntar_dfs.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/juntar_dfs.py): Cria um arquivo CSV com os dados dos servidores e alunos com base nos nomes em comum usando Pandas. Ao executar o código obtemos este arquivo: [servidores_alunos_rondonopolis.csv](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/servidores_alunos_rondonopolis.csv)


## Como Utilizar

1. **Requisitos de Ambiente**: É necessário ter Python, Selenium e BeautifulSoup4 instalados no ambiente local.
2. **Configuração do ChromeDriver**: Certifique-se de que a versão do ChromeDriver seja compatível com a versão do navegador Chrome instalada no seu sistema. (Dúvidas sobre o ChromeDriver ler a documentação do [selenium](https://selenium-python.readthedocs.io/))
3. **Execução do Script**: Abra o script em um ambiente Python adequado, como o Visual Studio Code (VSCode), e execute-o. O script irá iniciar um navegador Chrome em modo headless, realizar a raspagem de dados e salvar os resultados em um arquivo CSV.

## Observações

Este projeto é específico para o contexto da pesquisa mencionada e pode não ser facilmente adaptável para outros propósitos. Ele serve como um exemplo prático de como usar Python, Selenium e BeautifulSoup para realizar raspagem de dados em uma página da web.

Se você tiver alguma dúvida ou sugestão sobre o projeto, sinta-se à vontade para entrar em contato.


## Contato

Monyk Paola - monyk.penafor@gmail.com

<!-- Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->


<br /><br /><br /><br />

<h1 id="english" align="center">WEBSCRAPING</h1>
<h3 align="center">-<a href="#portugues"> VERSÃO EM PORTUGUÊS </a>-</h3>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#tools-used">Tools Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#code-functionality">Code Functionality</a>
    </li>
    <li><a href="#how-to-use">How to Use</a></li>
    <li><a href="#observations">Observations</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## About the Project

This project was developed as part of a Scientific Initiation program at the Federal Institute of Education, Science and Technology of Mato Grosso (IFMT), entitled "In search of IFMT graduates working as public servants in the Municipality of Rondonópolis/MT". The project's objective is to automate the search for information about public servants on the Transparency Portal of the City Hall of Rondonópolis/MT, using web scraping techniques. The obtained data is compared with the data of IFMT students to establish a student-servant relationship and finally produce a file showing all IFMT students who are/were public servants in Rondonópolis. Project Result:<a href="https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/servidores_alunos_rondonopolis.csv">  <strong>servidores_alunos_rondonopolis</strong></a>


### Tools Used

- **Python**: The main programming language used to develop this project.
- **Selenium**: A web browser automation tool that allows simulating user interactions, such as clicking buttons and filling out forms. It is especially useful when the target site extensively uses JavaScript or requires specific interactions with the web page.
- **BeautifulSoup**: A Python library for HTML and XML parsing. It was used to extract and manipulate data from HTML elements on the web page.
- **Pandas**: A Python library for data manipulation and analysis. It was used to process and manipulate structured data, such as joining dataframes. In this project, it was specifically used to retrieve data from IFMT students, which were separated by year in CSV files, and to merge the dataframes with student-servant relationships.


## Code Functionality

The main source code of this project is [scraper.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/scraper.py), which implements a Python script responsible for scraping data from the Transparency Portal of the City Hall of Rondonópolis/MT. This script uses Selenium to automate interaction with the website, navigating through pages and clicking on search buttons. Then, the data is extracted using BeautifulSoup and organized into a CSV file.

The result of data scraping with Selenium is this: [Rondonopolis_raspagem.csv](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/Rondonopolis_raspagem.csv)

### Other Python Files in the Repository

- [alunos_df.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/alunos_df.py): This Python file joins the data of all students into a single CSV file with the help of the Pandas library. By running the code, we obtain this file: [alunos_ifmt.csv](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/alunos_ifmt.csv)
- [alunos_unicode.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/alunos_unicode.py): Creates a list of student names, which will be imported by the scraper for comparison.
- [juntar_dfs.py](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/juntar_dfs.py): Creates a CSV file with data of servants and students based on common names using Pandas. By running the code, we obtain this file: [servidores_alunos_rondonopolis.csv](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/DADOS%20OBTIDOS/servidores_alunos_rondonopolis.csv)


## How to Use

1. **Environment Requirements**: Python, Selenium, and BeautifulSoup4 need to be installed in the local environment.
2. **ChromeDriver Configuration**: Ensure that the ChromeDriver version is compatible with the installed Chrome browser version on your system. (For doubts about ChromeDriver, refer to the [selenium documentation](https://selenium-python.readthedocs.io/))
3. **Script Execution**: Open the script in a suitable Python environment, such as Visual Studio Code (VSCode), and execute it. The script will start a Chrome browser in headless mode, perform data scraping, and save the results in a CSV file.

## Observations

This project is specific to the mentioned research context and may not be easily adaptable for other purposes. It serves as a practical example of using Python, Selenium, and BeautifulSoup for web scraping.

If you have any questions or suggestions about the project, feel free to contact.

## Contact

Monyk Paola - monyk.penafor@gmail.com

<!-- Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->

