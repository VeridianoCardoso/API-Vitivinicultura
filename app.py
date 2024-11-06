from flask import Flask, jsonify, make_response
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route("/api/producao")
def aba_producao():
    link = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, "html.parser")
    tbody = site.find("tbody")  # seleciona a tabela
    linhas_tr = tbody.find_all("tr")  # extrai todas as linhas da tabela
    dados = []
    dicionario = {}

    for linha in linhas_tr:
        celulas = [celula.get_text(strip=True) for celula in linha.find_all("td")]
        dados.append(celulas)

    return make_response(jsonify(
                            Nota = "Linha 1 = Produto Linha 2 = Quantidade Produzida",
                            Dados = dados))

@app.route("/api/processamento")
def aba_processamento():
    link = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, "html.parser")
    tbody = site.find("tbody")  # seleciona a tabela
    linhas_tr = tbody.find_all("tr")  # extrai todas as linhas da tabela
    dados = []
    dicionario = {}

    for linha in linhas_tr:
        celulas = [celula.get_text(strip=True) for celula in linha.find_all("td")]
        dados.append(celulas)

    return make_response(jsonify(
        Nota="Linha 1 = Tipo de Uva Processada Linha 2 = Quantidade Processada",
        Dados=dados))

@app.route("/api/comercializacao")
def aba_comercializacao():
    link = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, "html.parser")
    tbody = site.find("tbody")  # seleciona a tabela
    linhas_tr = tbody.find_all("tr")  # extrai todas as linhas da tabela
    dados = []
    dicionario = {}

    for linha in linhas_tr[1:]:
        celulas = [celula.get_text(strip=True) for celula in linha.find_all("td")]
        dados.append(celulas)

    return make_response(jsonify(
        Nota="Linha 1 = Produto Comercializado Linha 2 = Quantidade Comercializada",
        Dados=dados))

@app.route("/api/importacao")
def aba_importacao():
    link = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, "html.parser")
    tbody = site.find("tbody")  # seleciona a tabela
    linhas_tr = tbody.find_all("tr")  # extrai todas as linhas da tabela
    dados = []
    dicionario = {}

    for linha in linhas_tr[1:]:
        celulas = [celula.get_text(strip=True) for celula in linha.find_all("td")]
        dados.append(celulas)

    return make_response(jsonify(
        Nota="Linha 1 = País da Importacção Linha 2 = Quantidade Importada Linha 3 = Valor Importado",
        Dados=dados))

@app.route("/api/exportacao")
def aba_exportacao():
    link = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, "html.parser")
    tbody = site.find("tbody")  # seleciona a tabela
    linhas_tr = tbody.find_all("tr")  # extrai todas as linhas da tabela
    dados = []
    dicionario = {}

    for linha in linhas_tr[1:]:
        celulas = [celula.get_text(strip=True) for celula in linha.find_all("td")]
        dados.append(celulas)

    return make_response(jsonify(
        Nota="Linha 1 = País da Exportação Linha 2 = Quantidade Exportada Linha 3 = Valor Exportado",
        Dados=dados))

app.run()