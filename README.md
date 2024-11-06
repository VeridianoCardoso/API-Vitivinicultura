# API-Vitivinicultura
API que faz consultas no banco dados do site Vitibrasil através de scraping. A API permite consultar dados relacionados ao cultivo de uvas, produção de vinhos e derivados, além de outras informações do setor vitivinícola brasileiro.

## Sobre o Projeto
Este projeto faz parte do meu 1º Tech Challenger da Pós Tech Machine Learning Engineering da FIAP.
A aplicação consistem em fazer uma Restful API em Python que faça, inicialmente, consultas nos dados do site http://vitibrasil.cnpuv.embrapa.br/index.php, nas abas de Produção, Processamento, Comercialização, Importação e Exportação. 

## Overview da Documentação 
![Documentacao API1](https://github.com/user-attachments/assets/df59fe42-5a6b-431b-89da-fb7390825121)
![image](https://github.com/user-attachments/assets/0138a713-6594-4fc7-b545-ef7d6c7f9349)

## Fluxograma Simplicidado da API
![image](https://github.com/user-attachments/assets/6782a9ae-ce63-45b7-bed1-f0238e4a4559)

## Técnologias Utilizadas
* Python
* Flask
* BeautifulSoup
* Swagger
* Flask-CORS

## Como executar o projeto
1. Clone o repositório para a sua máquina local:
   ~~~python
   git clone https://github.com/VeridianoCardoso/API-Vitivinicultura.git 
   cd API-Vitivinicultura

2. Instale as dependências. O uso de ambiente virtual (venv) é recomendado.
   ~~~python
     pip install -r requirements.txt
3. Após instalar todas as dependências, executar:
    ~~~python
    app.py
4. Para acessar o servidor Flask:
  ~~~python
  http://127.0.0.1:5000/
~~~
  A API tem os seguintes endpoints:
 ~~~python
   /api/producao
   /api/processamento
   /api/comercializacao
   /api/importacao
   /api/exportacao
~~~

## Algumas Considerações
Essa foi a primeira vez que programei uma API na vida, bem como um readme aqui no GitHub. Ficou bem simples e definitivamente poderia fazer um código mais eficiente e limpo,mas com as habilidades desenvolvidas até este momento (começo do curso), por hora, me dou por satisfeito. Ao meu ver, esse Tech Challenger cumpriu muito bem em propor o desafio, me instigando e aprender cada vez mais. 










