
<h1 id="english" align="center">WEBSCRAPING</h1>
<h3 align="center">-<a href="#portugues"> VERSÃO PORTUGUÊS </a>-</h3>



</br></br>

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

Este projeto foi desenvolvido como parte de um programa de Iniciação Científica no Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso (IFMT), intitulado "Em busca de egressos do IFMT atuantes como servidores públicos do Município de Rondonópolis/MT". O objetivo do projeto é automatizar a consulta de informações sobre servidores públicos no Portal da Transparência da Prefeitura de Rondonópolis/MT, utilizando técnicas de raspagem de dados.


### Ferramentas Utilizadas

- **Python**: A linguagem de programação principal utilizada para desenvolver este projeto.
- **Selenium**: Uma ferramenta de automação de navegador web que permite simular interações do usuário, como clicar em botões e preencher formulários. É especialmente útil quando o site alvo utiliza JavaScript extensivamente ou requer interações específicas com a página da web.
- **BeautifulSoup**: Uma biblioteca Python para análise de documentos HTML e XML. Foi utilizada para extrair e manipular dados dos elementos HTML da página web.

## Funcionamento do Código

O código-fonte principal deste projeto é o [(scraper.py)](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/scraper.py), que implementa um script em Python responsável pela raspagem de dados do Portal da Transparência da Prefeitura de Rondonópolis/MT. Este script utiliza Selenium para automatizar a interação com o site, navegando pelas páginas e clicando nos botões de pesquisa. Em seguida, os dados são extraídos usando BeautifulSoup e organizados em um arquivo CSV.

Outros Arquivos Python no Repositório
[(alunos_df.py)](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/alunos_df.py): Este arquivo Python junta os dados de todos os alunos em um único arquivo CSV.
[(alunos_unicode.py)](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/alunos_unicode.py):Cria uma lista de nomes de alunos, que será importada pelo scraper para fazer a comparação.
[(juntar_dfs.py)](https://github.com/MonykPenafor/WEBSCRAPING/blob/main/juntar_dfs.py):Cria um arquivo CSV com os dados dos servidores e alunos com base nos nomes em comum.


## Como Utilizar

1. **Requisitos de Ambiente**: É necessário ter Python, Selenium e BeautifulSoup4 instalados no ambiente local.
2. **Configuração do ChromeDriver**: Certifique-se de que a versão do ChromeDriver seja compatível com a versão do navegador Chrome instalada no seu sistema. (Se tiver dúvidas sobre o ChromeDriver ler a documentação do [selenium](https://selenium-python.readthedocs.io/))
3. **Execução do Script**: Abra o script em um ambiente Python adequado, como o Visual Studio Code (VSCode), e execute-o. O script irá iniciar um navegador Chrome em modo headless, realizar a raspagem de dados e salvar os resultados em um arquivo CSV.

## Observações

Este projeto é específico para o contexto da pesquisa mencionada e pode não ser facilmente adaptável para outros propósitos. Ele serve como um exemplo prático de como usar Python, Selenium e BeautifulSoup para realizar raspagem de dados em uma página da web.

Se você tiver alguma dúvida ou sugestão sobre o projeto, sinta-se à vontade para entrar em contato.


## Contato

Monyk Paola - monyk.penafor@gmail.com

<!-- Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->